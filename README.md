# daily-radar

A small bot that keeps a daily log of what is happening in tech: the Hacker News
front page, fast-rising new GitHub repositories, and fresh arXiv papers. Each run
picks a random subset of sources, so coverage varies from day to day.

**4** daily digests so far · snapshots: hn 4, github 3, arxiv 4

## Recent digests

- [2026-11-13](digests/2026/2026-11-13.md)
- [2026-11-12](digests/2026/2026-11-12.md)
- [2026-11-11](digests/2026/2026-11-11.md)
- [2026-11-10](digests/2026/2026-11-10.md)

## Trending on Hacker News this week

`agents` ×6 · `claude` ×5 · `models` ×4 · `ground` ×4 · `all` ×4 · `live` ×4 · `street` ×4 · `apple` ×4 · `code` ×3 · `security` ×3 · `general` ×3 · `nvidia` ×3 · `found` ×3 · `support` ×3 · `issues` ×3

## How it works

`radar.py` (standard library only) is run by a scheduled GitHub Actions workflow
a few times a day. Tune sources and randomness in `config.json`.
Run it yourself with `python3 radar.py --force --no-commit`.
