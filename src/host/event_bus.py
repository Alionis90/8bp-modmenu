"""Tiny synchronous pub/sub used between host and plugins."""
from __future__ import annotations

from collections import defaultdict
from typing import Any, Callable

Handler = Callable[[Any], None]


class EventBus:
    def __init__(self) -> None:
        self._subs: dict[str, list[Handler]] = defaultdict(list)

    def subscribe(self, topic: str, handler: Handler) -> None:
        self._subs[topic].append(handler)

    def publish(self, topic: str, payload: Any) -> None:
        for handler in list(self._subs.get(topic, ())):
            try:
                handler(payload)
            except Exception:
                pass