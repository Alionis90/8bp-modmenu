"""Core host loop: loads plugins, ticks them, routes IPC events."""
from __future__ import annotations

from typing import Any

from loguru import logger

from src.host.event_bus import EventBus
from src.host.registry import PluginRegistry
from src.shared.config import ModConfig
from src.shared.contracts import PluginContext
from src.overlay_core.window import OverlayWindow


class PluginHost:
    def __init__(self, registry: PluginRegistry, config: ModConfig) -> None:
        self.registry = registry
        self.config = config
        self.bus = EventBus()
        self.window = OverlayWindow(config.overlay)
        self._running = False

    def run(self) -> None:
        self.window.show()
        self._running = True
        for name, plugin_cls in self.registry.items():
            ctx = PluginContext(bus=self.bus, config=self.config.plugin(name))
            instance = plugin_cls(ctx)
            instance.on_load()
            self.bus.subscribe(f"tick:{name}", instance.on_tick)
            logger.debug("loaded plugin {}", name)
        self.window.loop(tick=lambda dt: self.bus.publish("frame", dt))

    def shutdown(self) -> None:
        self._running = False
        for name in self.registry:
            self.bus.publish(f"unload:{name}", None)
        self.window.close()