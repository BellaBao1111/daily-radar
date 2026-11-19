# daily-radar

A small bot that keeps a daily log of what is happening in tech: the Hacker News
front page, fast-rising new GitHub repositories, and fresh arXiv papers. Each run
picks a random subset of sources, so coverage varies from day to day.

**10** daily digests so far · snapshots: hn 7, github 6, arxiv 10

## Recent digests

- [2026-11-19](digests/2026/2026-11-19.md)
- [2026-11-18](digests/2026/2026-11-18.md)
- [2026-11-17](digests/2026/2026-11-17.md)
- [2026-11-16](digests/2026/2026-11-16.md)
- [2026-11-15](digests/2026/2026-11-15.md)
- [2026-11-14](digests/2026/2026-11-14.md)
- [2026-11-13](digests/2026/2026-11-13.md)
- [2026-11-12](digests/2026/2026-11-12.md)
- [2026-11-11](digests/2026/2026-11-11.md)
- [2026-11-10](digests/2026/2026-11-10.md)

## Trending on Hacker News this week

`code` ×12 · `security` ×6 · `nvidia` ×6 · `agents` ×6 · `ground` ×6 · `stop` ×5 · `down` ×5 · `all` ×5 · `models` ×5 · `engineering` ×5 · `apple` ×4 · `live` ×4 · `national` ×4 · `stopped` ×4 · `coding` ×4

## How it works

`radar.py` (standard library only) is run by a scheduled GitHub Actions workflow
a few times a day. Tune sources and randomness in `config.json`.
Run it yourself with `python3 radar.py --force --no-commit`.
