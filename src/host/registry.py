"""Discovers plugin modules from the plugins/ folder."""
from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType
from typing import Iterator

from loguru import logger

from src.shared.contracts import ModPlugin


class PluginRegistry:
    def __init__(self) -> None:
        self._entries: dict[str, type[ModPlugin]] = {}

    def discover(self, root: Path) -> None:
        if not root.is_dir():
            logger.warning("plugin root {} missing", root)
            return
        for path in sorted(root.glob("*/plugin.py")):
            mod = self._import(path)
            cls = getattr(mod, "PLUGIN", None)
            if cls is None:
                logger.warning("{} has no PLUGIN symbol", path)
                continue
            self._entries[path.parent.name] = cls

    @staticmethod
    def _import(path: Path) -> ModuleType:
        name = f"8bp_plugin_{path.parent.name}"
        spec = importlib.util.spec_from_file_location(name, path)
        if spec is None or spec.loader is None:
            raise RuntimeError(f"cannot load {path}")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod

    def __iter__(self) -> Iterator[str]:
        return iter(self._entries)

    def items(self):
        return self._entries.items()

    def __len__(self) -> int:
        return len(self._entries)