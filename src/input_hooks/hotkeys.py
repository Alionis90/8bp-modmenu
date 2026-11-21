"""Global hotkey registration for toggling plugin toggles."""
from __future__ import annotations

import win32api
import win32con

VK_MAP = {
    "F1": win32con.VK_F1,
    "F2": win32con.VK_F2,
    "F3": win32con.VK_F3,
    "INSERT": win32con.VK_INSERT,
}


def is_pressed(name: str) -> bool:
    vk = VK_MAP.get(name.upper())
    if vk is None:
        return False
    return bool(win32api.GetAsyncKeyState(vk) & 0x8000)