"""Overlay that draws circles over active balls and pocket zones."""
from __future__ import annotations

from src.memory_adapter.offsets import POCKETS
from src.memory_adapter.process import GameProcess
from src.memory_adapter.reader import read_balls
from src.shared.contracts import ModPlugin


class BallEsp(ModPlugin):
    name = "ball_esp"
    version = "1.0.3"

    def on_load(self) -> None:
        self.proc = GameProcess()
        self.proc.attach()
        self.draw_pockets = True

    def on_tick(self, _payload) -> None:
        if not self.proc.attached:
            return
        balls = read_balls(self.proc)
        circles = [
            {"x": b.pos.x, "y": b.pos.y, "r": 11, "color": "#ff4444" if b.idx else "#ffffff"}
            for b in balls if b.active
        ]
        self.ctx.bus.publish("overlay:circles", {"items": circles})
        if self.draw_pockets:
            self.ctx.bus.publish("overlay:pockets", {"pockets": POCKETS})


PLUGIN = BallEsp