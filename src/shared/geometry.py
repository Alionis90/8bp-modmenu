"""2D geometry helpers used by aim assist and guideline prediction."""
from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Vec2:
    x: float
    y: float

    def __add__(self, other: "Vec2") -> "Vec2":
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vec2") -> "Vec2":
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, k: float) -> "Vec2":
        return Vec2(self.x * k, self.y * k)

    def length(self) -> float:
        return math.hypot(self.x, self.y)

    def normalized(self) -> "Vec2":
        l = self.length() or 1.0
        return Vec2(self.x / l, self.y / l)


def reflect(incident: Vec2, normal: Vec2) -> Vec2:
    d = incident.normalized()
    return d - normal * (2 * d.x * normal.x + 2 * d.y * normal.y)


def ghost_ball(cue: Vec2, target: Vec2, pocket: Vec2, ball_r: float = 11.0) -> Vec2:
    """Position the cue ball must occupy at contact to send target into pocket."""
    to_pocket = (pocket - target).normalized()
    return target - to_pocket * (ball_r * 2.0)