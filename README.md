# daily-radar

A small bot that keeps a daily log of what is happening in tech: the Hacker News
front page, fast-rising new GitHub repositories, and fresh arXiv papers. Each run
picks a random subset of sources, so coverage varies from day to day.

**5** daily digests so far · snapshots: hn 5, github 4, arxiv 5

## Recent digests

- [2026-11-14](digests/2026/2026-11-14.md)
- [2026-11-13](digests/2026/2026-11-13.md)
- [2026-11-12](digests/2026/2026-11-12.md)
- [2026-11-11](digests/2026/2026-11-11.md)
- [2026-11-10](digests/2026/2026-11-10.md)

## Trending on Hacker News this week

`agents` ×7 · `all` ×6 · `nvidia` ×6 · `live` ×6 · `ground` ×6 · `code` ×5 · `security` ×5 · `claude` ×5 · `found` ×5 · `stop` ×5 · `engineering` ×4 · `side` ×4 · `models` ×4 · `faa` ×4 · `issues` ×4

## How it works

`radar.py` (standard library only) is run by a scheduled GitHub Actions workflow
a few times a day. Tune sources and randomness in `config.json`.
Run it yourself with `python3 radar.py --force --no-commit`.
