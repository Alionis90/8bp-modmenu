"""Converts bus events into overlay draw calls."""
from __future__ import annotations

from src.overlay_core.window import OverlayWindow


def bind_renderer(window: OverlayWindow, bus) -> None:
    def on_polyline(payload) -> None:
        window.highlight([(p.x, p.y) for p in payload["points"]])

    bus.subscribe("overlay:polyline", on_polyline)