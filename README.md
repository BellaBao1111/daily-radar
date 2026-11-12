# daily-radar

A small bot that keeps a daily log of what is happening in tech: the Hacker News
front page, fast-rising new GitHub repositories, and fresh arXiv papers. Each run
picks a random subset of sources, so coverage varies from day to day.

**2** daily digests so far · snapshots: hn 2, github 1, arxiv 2

## Recent digests

- [2026-11-11](digests/2026/2026-11-11.md)
- [2026-11-10](digests/2026/2026-11-10.md)

## Trending on Hacker News this week

`claude` ×4 · `apple` ×3 · `agents` ×3 · `live` ×2 · `support` ×2 · `died` ×2 · `all` ×2 · `agent` ×2 · `hardest` ×2 · `street` ×2 · `launch` ×2 · `gemini` ×2 · `local` ×2 · `inference` ×2 · `models` ×2

## How it works

`radar.py` (standard library only) is run by a scheduled GitHub Actions workflow
a few times a day. Tune sources and randomness in `config.json`.
Run it yourself with `python3 radar.py --force --no-commit`.
