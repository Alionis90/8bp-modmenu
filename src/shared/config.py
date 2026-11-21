"""YAML config loader with typed defaults."""
from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field


class OverlayConfig(BaseModel):
    width: int = 1920
    height: int = 1080
    fps: int = 60
    click_through: bool = True


class ModConfig(BaseModel):
    log_level: str = "INFO"
    build_tag: str = "2026.01"
    overlay: OverlayConfig = Field(default_factory=OverlayConfig)
    plugins: dict[str, dict[str, Any]] = Field(default_factory=dict)

    def plugin(self, name: str) -> dict[str, Any]:
        return self.plugins.get(name, {})


def load_config(path: Path) -> ModConfig:
    if not path.exists():
        return ModConfig()
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return ModConfig(**data)