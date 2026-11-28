# daily-radar

A small bot that keeps a daily log of what is happening in tech: the Hacker News
front page, fast-rising new GitHub repositories, and fresh arXiv papers. Each run
picks a random subset of sources, so coverage varies from day to day.

**19** daily digests so far · snapshots: hn 13, github 13, arxiv 15

## Recent digests

- [2026-11-28](digests/2026/2026-11-28.md)
- [2026-11-27](digests/2026/2026-11-27.md)
- [2026-11-26](digests/2026/2026-11-26.md)
- [2026-11-25](digests/2026/2026-11-25.md)
- [2026-11-24](digests/2026/2026-11-24.md)
- [2026-11-23](digests/2026/2026-11-23.md)
- [2026-11-22](digests/2026/2026-11-22.md)
- [2026-11-21](digests/2026/2026-11-21.md)
- [2026-11-20](digests/2026/2026-11-20.md)
- [2026-11-19](digests/2026/2026-11-19.md)
- [2026-11-18](digests/2026/2026-11-18.md)
- [2026-11-17](digests/2026/2026-11-17.md)
- [2026-11-16](digests/2026/2026-11-16.md)
- [2026-11-15](digests/2026/2026-11-15.md)

## Trending on Hacker News this week

`one` ×6 · `security` ×6 · `first` ×5 · `again` ×5 · `models` ×5 · `shit` ×5 · `now` ×5 · `send` ×4 · `over` ×4 · `rust` ×4 · `fun` ×4 · `browser` ×4 · `without` ×4 · `getting` ×4 · `coding` ×4

## How it works

`radar.py` (standard library only) is run by a scheduled GitHub Actions workflow
a few times a day. Tune sources and randomness in `config.json`.
Run it yourself with `python3 radar.py --force --no-commit`.
