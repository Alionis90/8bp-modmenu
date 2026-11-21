# Contributing

- Fork, branch from `main`, keep PRs focused on one plugin or one offset update.
- New features go under `plugins/<feature>/plugin.py` and must implement `ModPlugin`.
- Run `pytest tests/` before opening a PR.
- Do not commit real player IDs, session tokens, or screenshots with PII.
- Offset updates for a new client build go in `src/memory_adapter/offsets.py` with the build tag bumped.