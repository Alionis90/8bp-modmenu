"""Shared plugin contract — every modmenu plugin implements ModPlugin."""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Protocol


class EventBusProto(Protocol):
    def subscribe(self, topic: str, handler) -> None: ...
    def publish(self, topic: str, payload: Any) -> None: ...


@dataclass
class PluginContext:
    bus: EventBusProto
    config: Any


class ModPlugin(ABC):
    name: str = "unnamed"
    version: str = "0.0.0"

    def __init__(self, ctx: PluginContext) -> None:
        self.ctx = ctx

    @abstractmethod
    def on_load(self) -> None: ...

    @abstractmethod
    def on_tick(self, payload: Any) -> None: ...

    def on_unload(self) -> None:
        pass