# daily-radar

A small bot that keeps a daily log of what is happening in tech: the Hacker News
front page, fast-rising new GitHub repositories, and fresh arXiv papers. Each run
picks a random subset of sources, so coverage varies from day to day.

**3** daily digests so far · snapshots: hn 3, github 2, arxiv 2

## Recent digests

- [2026-11-12](digests/2026/2026-11-12.md)
- [2026-11-11](digests/2026/2026-11-11.md)
- [2026-11-10](digests/2026/2026-11-10.md)

## Trending on Hacker News this week

`agents` ×5 · `street` ×4 · `apple` ×4 · `claude` ×4 · `agent` ×3 · `live` ×3 · `work` ×3 · `jane` ×3 · `died` ×3 · `gemini` ×3 · `local` ×3 · `inference` ×3 · `jensen` ×3 · `huang` ×3 · `making` ×2

## How it works

`radar.py` (standard library only) is run by a scheduled GitHub Actions workflow
a few times a day. Tune sources and randomness in `config.json`.
Run it yourself with `python3 radar.py --force --no-commit`.
