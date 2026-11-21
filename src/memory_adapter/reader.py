"""Higher-level reads: parses the ball array into BallState objects."""
from __future__ import annotations

from src.memory_adapter.offsets import BALL_STRIDE, MAX_BALLS, OFFSETS
from src.memory_adapter.process import GameProcess
from src.shared.geometry import Vec2


class BallState:
    __slots__ = ("idx", "pos", "active")

    def __init__(self, idx: int, pos: Vec2, active: bool) -> None:
        self.idx = idx
        self.pos = pos
        self.active = active


def read_balls(proc: GameProcess) -> list[BallState]:
    if not proc.attached:
        return []
    base = proc.resolve(OFFSETS["ball_array"])
    balls: list[BallState] = []
    for i in range(MAX_BALLS):
        addr = base + i * BALL_STRIDE
        x = proc.read_float(addr)
        y = proc.read_float(addr + 4)
        active = proc.read_float(addr + 8) > 0.5
        balls.append(BallState(i, Vec2(x, y), active))
    return balls