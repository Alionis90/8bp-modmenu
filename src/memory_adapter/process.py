"""Attaches to the 8 Ball Pool client process and exposes read/write helpers."""
from __future__ import annotations

from typing import Optional

import pymem
from loguru import logger

PROCESS_NAME = "8BallPool.exe"


class GameProcess:
    def __init__(self) -> None:
        self._pm: Optional[pymem.Pymem] = None
        self._base: int = 0

    def attach(self) -> bool:
        try:
            self._pm = pymem.Pymem(PROCESS_NAME)
            self._base = pymem.process.module_from_name(
                self._pm.process_handle, PROCESS_NAME
            ).lpBaseOfDll
            logger.info("attached to {} @ 0x{:x}", PROCESS_NAME, self._base)
            return True
        except Exception as exc:
            logger.error("attach failed: {}", exc)
            self._pm = None
            return False

    @property
    def attached(self) -> bool:
        return self._pm is not None

    def read_float(self, address: int) -> float:
        assert self._pm is not None
        return self._pm.read_float(address)

    def write_float(self, address: int, value: float) -> None:
        assert self._pm is not None
        self._pm.write_float(address, value)

    def resolve(self, offset: int) -> int:
        return self._base + offset