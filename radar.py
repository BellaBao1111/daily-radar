#!/usr/bin/env python3
"""daily-radar: collect a small, randomised slice of tech news every day.

Each run picks a random subset of collectors (Hacker News, new GitHub repos,
arXiv), merges what they find into that day's JSON snapshot, re-renders the
day's Markdown digest and commits each collector's result separately.

Standard library only, so it runs on a bare GitHub Actions runner.
"""
from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import os
import random
import re
import subprocess
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent
CONFIG = json.loads((ROOT / "config.json").read_text())
TZ = ZoneInfo(CONFIG["timezone"])
UA = "daily-radar/1.0"


# ---------------------------------------------------------------- helpers

def today() -> dt.date:
    return dt.datetime.now(TZ).date()


def fetch(url: str, headers: dict | None = None) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def data_path(source: str, day: dt.date) -> Path:
    return ROOT / "data" / source / str(day.year) / f"{day.isoformat()}.json"


def load(path: Path, default):
    return json.loads(path.read_text()) if path.exists() else default


def save(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False, sort_keys=True) + "\n")


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, check=True,
                          capture_output=True, text=True).stdout.strip()


def commit(message: str, enabled: bool) -> bool:
    """Commit everything that changed. Returns True if there was a change."""
    if not git("status", "--porcelain"):
        return False
    if enabled:
        git("add", "-A")
        git("commit", "-m", message)
    print(f"  commit: {message}")
    return True


# ------------------------------------------------------------- collectors
# Each collector merges into the day's snapshot and returns a commit message
# describing what actually changed (or None when nothing new was found).

def collect_hn(day: dt.date, rng: random.Random) -> str | None:
    """Front-page Hacker News stories; keeps the peak score seen during the day."""
    raw = json.loads(fetch("https://hn.algolia.com/api/v1/search?tags=front_page&hitsPerPage=30"))
    path = data_path("hn", day)
    stories = load(path, {})
    new = 0
    for hit in raw["hits"]:
        sid = str(hit["objectID"])
        prev = stories.get(sid)
        new += prev is None
        stories[sid] = {
            "title": hit.get("title") or "",
            "url": hit.get("url") or f"https://news.ycombinator.com/item?id={sid}",
            "points": max(hit.get("points") or 0, (prev or {}).get("points", 0)),
            "comments": max(hit.get("num_comments") or 0, (prev or {}).get("comments", 0)),
            "author": hit.get("author") or "",
        }
    save(path, stories)
    return f"hn: {day} front page (+{new} new, {len(stories)} tracked)"


def collect_github(day: dt.date, rng: random.Random) -> str | None:
    """Most-starred repos created in the last week, for a few random languages."""
    langs = rng.sample(CONFIG["github_languages"], k=rng.randint(1, 3))
    since = (day - dt.timedelta(days=7)).isoformat()
    headers = {"Accept": "application/vnd.github+json"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
    path = data_path("github", day)
    snapshot = load(path, {})
    for lang in langs:
        q = urllib.parse.quote(f"created:>{since} language:{lang}")
        url = f"https://api.github.com/search/repositories?q={q}&sort=stars&order=desc&per_page=10"
        items = json.loads(fetch(url, headers))["items"]
        snapshot[lang] = [{
            "name": r["full_name"],
            "url": r["html_url"],
            "stars": r["stargazers_count"],
            "description": (r.get("description") or "").strip()[:200],
            "created": r["created_at"][:10],
        } for r in items]
    save(path, snapshot)
    return f"github: {day} rising repos ({', '.join(sorted(langs))})"


def collect_arxiv(day: dt.date, rng: random.Random) -> str | None:
    """Latest arXiv submissions in one or two random categories."""
    cats = rng.sample(CONFIG["arxiv_categories"], k=rng.randint(1, 2))
    ns = {"a": "http://www.w3.org/2005/Atom"}
    path = data_path("arxiv", day)
    papers = load(path, {})
    new = 0
    for cat in cats:
        url = ("http://export.arxiv.org/api/query?search_query=cat:" + cat +
               "&sortBy=submittedDate&sortOrder=descending&max_results=15")
        for entry in ET.fromstring(fetch(url)).findall("a:entry", ns):
            link = entry.findtext("a:id", "", ns).strip()
            pid = link.rsplit("/", 1)[-1]
            new += pid not in papers
            papers[pid] = {
                "title": " ".join(entry.findtext("a:title", "", ns).split()),
                "url": link,
                "category": cat,
                "authors": [a.findtext("a:name", "", ns) for a in entry.findall("a:author", ns)][:5],
                "summary": " ".join(entry.findtext("a:summary", "", ns).split())[:400],
            }
    save(path, papers)
    return f"arxiv: {day} new papers in {', '.join(sorted(cats))} (+{new})"


COLLECTORS = {"hn": collect_hn, "github": collect_github, "arxiv": collect_arxiv}


# -------------------------------------------------------------- rendering

def render_digest(day: dt.date) -> None:
    """Rebuild digests/<year>/<date>.md from whatever snapshots exist for the day."""
    out = [f"# Radar for {day:%A, %B %-d, %Y}", ""]
    hn = load(data_path("hn", day), {})
    if hn:
        out += ["## Hacker News", ""]
        for s in sorted(hn.values(), key=lambda s: -s["points"])[:20]:
            out.append(f"- [{s['title']}]({s['url']}) — {s['points']} points, {s['comments']} comments")
        out.append("")
    gh = load(data_path("github", day), {})
    if gh:
        out += ["## Rising GitHub repos (created this week)", ""]
        for lang in sorted(gh):
            out += [f"### {lang}", ""]
            for r in gh[lang]:
                desc = f" — {r['description']}" if r["description"] else ""
                out.append(f"- [{r['name']}]({r['url']}) ★{r['stars']}{desc}")
            out.append("")
    ax = load(data_path("arxiv", day), {})
    if ax:
        out += ["## arXiv", ""]
        by_cat = collections.defaultdict(list)
        for p in ax.values():
            by_cat[p["category"]].append(p)
        for cat in sorted(by_cat):
            out += [f"### {cat}", ""]
            for p in by_cat[cat]:
                out.append(f"- [{p['title']}]({p['url']}) — {', '.join(p['authors'])}")
            out.append("")
    path = ROOT / "digests" / str(day.year) / f"{day.isoformat()}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(out).rstrip() + "\n")


STOPWORDS = set("""a an and are as at be by for from has have how i in is it its my new not of on
or our show hn ask the this to was we what when why with you your your can will do does using use
vs via into after about more than that i'm it's""".split())


def render_readme(day: dt.date) -> None:
    """Rebuild the README index: recent digests, totals, and trending HN title words."""
    digests = sorted((ROOT / "digests").glob("*/*.md"), reverse=True)
    counts = {src: len(list((ROOT / "data" / src).glob("*/*.json"))) for src in COLLECTORS}
    words = collections.Counter()
    for i in range(7):
        for s in load(data_path("hn", day - dt.timedelta(days=i)), {}).values():
            words.update(w for w in re.findall(r"[a-z][a-z0-9+#.-]{2,}", s["title"].lower())
                         if w not in STOPWORDS)
    out = [
        "# daily-radar",
        "",
        "A small bot that keeps a daily log of what is happening in tech: the Hacker News",
        "front page, fast-rising new GitHub repositories, and fresh arXiv papers. Each run",
        "picks a random subset of sources, so coverage varies from day to day.",
        "",
        f"**{len(digests)}** daily digests so far · snapshots: " +
        ", ".join(f"{src} {n}" for src, n in counts.items()),
        "",
        "## Recent digests",
        "",
    ]
    out += [f"- [{p.stem}]({p.relative_to(ROOT).as_posix()})" for p in digests[:14]]
    if words:
        out += ["", "## Trending on Hacker News this week", "",
                " · ".join(f"`{w}` ×{n}" for w, n in words.most_common(15) if n > 1) or "_not enough data yet_"]
    out += ["", "## How it works", "",
            "`radar.py` (standard library only) is run by a scheduled GitHub Actions workflow",
            "a few times a day. Tune sources and randomness in `config.json`.",
            "Run it yourself with `python3 radar.py --force --no-commit`.", ""]
    (ROOT / "README.md").write_text("\n".join(out))


# ------------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--force", action="store_true", help="never skip this run")
    ap.add_argument("--no-commit", action="store_true", help="write files but do not git commit")
    ap.add_argument("--only", choices=COLLECTORS, nargs="+", help="run exactly these collectors")
    ap.add_argument("--seed", type=int, help="seed the random choices (for reproducing a run)")
    args = ap.parse_args()

    rng = random.Random(args.seed)
    day = today()
    rnd = CONFIG["randomness"]
    # Every day must end up with at least one commit: once it is late enough in
    # the day and nothing has been collected yet, the run can no longer skip.
    digest = ROOT / "digests" / str(day.year) / f"{day.isoformat()}.md"
    must_run = (not digest.exists()
                and dt.datetime.now(TZ).hour >= rnd["guarantee_after_hour"])
    if must_run:
        print(f"{day}: nothing collected yet today; this run will not skip")
    elif not args.force and not args.only and rng.random() < rnd["skip"]:
        print(f"{day}: rolled a skip (p={rnd['skip']}); nothing to do")
        return 0

    if args.only:
        chosen = args.only
    else:
        k = rng.choices([1, 2, 3], weights=rnd["collector_count_weights"])[0]
        chosen = rng.sample(list(COLLECTORS), k=k)
    print(f"{day}: running {', '.join(chosen)}")

    # On a must-run, fall back to the remaining collectors if the chosen ones fail.
    fallback = [n for n in COLLECTORS if n not in chosen] if must_run else []
    changed = False
    for name in chosen + fallback:
        if name in fallback and changed:
            break
        try:
            message = COLLECTORS[name](day, rng)
        except Exception as exc:  # one flaky API must not sink the whole run
            print(f"  {name} failed: {exc}", file=sys.stderr)
            if not args.no_commit:
                git("checkout", "--", ".")  # drop any half-written snapshot
            continue
        render_digest(day)
        if message:
            changed |= commit(message, not args.no_commit)

    if changed:
        render_readme(day)
        commit(f"index: refresh for {day}", not args.no_commit)
    return 0


if __name__ == "__main__":
    sys.exit(main())
