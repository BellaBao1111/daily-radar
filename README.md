# daily-radar

A small bot that keeps a daily log of what is happening in tech: the Hacker News
front page, fast-rising new GitHub repositories, and fresh arXiv papers. Each run
picks a random subset of sources, so coverage varies from day to day.

**18** daily digests so far · snapshots: hn 12, github 13, arxiv 14

## Recent digests

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
- [2026-11-14](digests/2026/2026-11-14.md)

## Trending on Hacker News this week

`security` ×6 · `windows` ×5 · `models` ×5 · `rust` ×5 · `shit` ×5 · `now` ×5 · `without` ×5 · `llms` ×4 · `getting` ×4 · `again` ×4 · `c++` ×4 · `hiring` ×4 · `lean` ×4 · `holy` ×4 · `built` ×4

## How it works

`radar.py` (standard library only) is run by a scheduled GitHub Actions workflow
a few times a day. Tune sources and randomness in `config.json`.
Run it yourself with `python3 radar.py --force --no-commit`.
