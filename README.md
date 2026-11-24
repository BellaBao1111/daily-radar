# daily-radar

A small bot that keeps a daily log of what is happening in tech: the Hacker News
front page, fast-rising new GitHub repositories, and fresh arXiv papers. Each run
picks a random subset of sources, so coverage varies from day to day.

**15** daily digests so far · snapshots: hn 11, github 11, arxiv 13

## Recent digests

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
- [2026-11-13](digests/2026/2026-11-13.md)
- [2026-11-12](digests/2026/2026-11-12.md)
- [2026-11-11](digests/2026/2026-11-11.md)

## Trending on Hacker News this week

`models` ×6 · `code` ×6 · `without` ×5 · `now` ×5 · `built` ×4 · `coding` ×4 · `microsoft` ×4 · `graphql` ×4 · `open-source` ×4 · `github` ×4 · `agents` ×4 · `gemini` ×4 · `again` ×3 · `network` ×3 · `archive` ×3

## How it works

`radar.py` (standard library only) is run by a scheduled GitHub Actions workflow
a few times a day. Tune sources and randomness in `config.json`.
Run it yourself with `python3 radar.py --force --no-commit`.
