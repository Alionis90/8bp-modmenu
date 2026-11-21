"""Aim assist: nudges cue angle toward the ghost ball on a configurable key."""
from __future__ import annotations

import math

from src.memory_adapter.offsets import OFFSETS, POCKETS
from src.memory_adapter.process import GameProcess
from src.memory_adapter.reader import read_balls
from src.shared.contracts import ModPlugin
from src.shared.geometry import Vec2, ghost_ball


class AimAssist(ModPlugin):
    name = "aim_assist"
    version = "1.2.0"

    def on_load(self) -> None:
        self.proc = GameProcess()
        self.proc.attach()
        self.enabled = True

    def on_tick(self, _payload) -> None:
        if not self.enabled or not self.proc.attached:
            return
        balls = read_balls(self.proc)
        cue = next((b for b in balls if b.idx == 0 and b.active), None)
        targets = [b for b in balls if b.idx != 0 and b.active]
        if not cue or not targets:
            return
        target = min(targets, key=lambda b: (b.pos - cue.pos).length())
        pocket = min((Vec2(*p) for p in POCKETS), key=lambda p: (p - target.pos).length())
        ghost = ghost_ball(cue.pos, target.pos, pocket)
        angle = math.atan2(ghost.y - cue.pos.y, ghost.x - cue.pos.x)
        self.proc.write_float(self.proc.resolve(OFFSETS["cue_angle"]), angle)


PLUGIN = AimAssist