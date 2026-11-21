"""Loads client-side cue and table skins from skins/ without touching the account."""
from __future__ import annotations

from pathlib import Path

from src.shared.contracts import ModPlugin


class SkinSwapper(ModPlugin):
    name = "skin_swapper"
    version = "0.4.0"

    def on_load(self) -> None:
        self.skin_dir = Path("skins")
        self.active_cue = self.ctx.config.get("cue", "classic_black")
        self.active_table = self.ctx.config.get("table", "monaco_green")

    def on_tick(self, _payload) -> None:
        pass

    def set_cue(self, name: str) -> None:
        self.active_cue = name
        self.ctx.bus.publish("skin:cue_changed", {"name": name})

    def set_table(self, name: str) -> None:
        self.active_table = name
        self.ctx.bus.publish("skin:table_changed", {"name": name})


PLUGIN = SkinSwapper