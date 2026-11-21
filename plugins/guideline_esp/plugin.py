"""Extends the aiming guideline through multiple cushion bounces."""
from __future__ import annotations

from src.memory_adapter.offsets import OFFSETS
from src.memory_adapter.process import GameProcess
from src.shared.contracts import ModPlugin
from src.shared.geometry import Vec2, reflect


class GuidelineEsp(ModPlugin):
    name = "guideline_esp"
    version = "0.9.1"

    def on_load(self) -> None:
        self.proc = GameProcess()
        self.proc.attach()
        self.bounces = 3

    def on_tick(self, _payload) -> None:
        if not self.proc.attached:
            return
        angle = self.proc.read_float(self.proc.resolve(OFFSETS["cue_angle"]))
        origin = Vec2(960, 520)
        dirv = Vec2(0, 0)
        import math
        dirv = Vec2(math.cos(angle), math.sin(angle))
        points = [origin]
        cur = origin
        for _ in range(self.bounces):
            cur = cur + dirv * 400
            points.append(cur)
            if cur.x < 0 or cur.x > 1920:
                dirv = reflect(dirv, Vec2(1, 0))
            if cur.y < 0 or cur.y > 1080:
                dirv = reflect(dirv, Vec2(0, 1))
        self.ctx.bus.publish("overlay:polyline", {"points": points, "color": "#00ff88"})


PLUGIN = GuidelineEsp