# daily-radar

A small bot that keeps a daily log of what is happening in tech: the Hacker News
front page, fast-rising new GitHub repositories, and fresh arXiv papers. Each run
picks a random subset of sources, so coverage varies from day to day.

**1** daily digests so far · snapshots: hn 1, github 1, arxiv 1

## Recent digests

- [2026-11-10](digests/2026/2026-11-10.md)

## Trending on Hacker News this week

`canada` ×2 · `now` ×2 · `code` ×2 · `tailscale` ×2

## How it works

`radar.py` (standard library only) is run by a scheduled GitHub Actions workflow
a few times a day. Tune sources and randomness in `config.json`.
Run it yourself with `python3 radar.py --force --no-commit`.
