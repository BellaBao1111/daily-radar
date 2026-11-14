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

`agents` ×6 · `ground` ×6 · `claude` ×5 · `nvidia` ×5 · `found` ×5 · `stop` ×5 · `all` ×5 · `live` ×5 · `security` ×4 · `models` ×4 · `faa` ×4 · `issues` ×4 · `nationwide` ×4 · `system` ×4 · `jensen` ×4

## How it works

`radar.py` (standard library only) is run by a scheduled GitHub Actions workflow
a few times a day. Tune sources and randomness in `config.json`.
Run it yourself with `python3 radar.py --force --no-commit`.
