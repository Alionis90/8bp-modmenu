"""Helper that scans the client module for known signatures and prints offsets."""
from __future__ import annotations

import pymem
from pymem.pattern import pattern_scan_module

SIGNATURES = {
    "cue_angle": b"\xF3\x0F\x11\x05????\xF3\x0F\x10",
    "ball_array": b"\x48\x8D\x0D????\xE8????\x48\x8B",
}


def main() -> None:
    pm = pymem.Pymem("8BallPool.exe")
    for name, sig in SIGNATURES.items():
        addr = pattern_scan_module(pm.process_handle, "8BallPool.exe", sig)
        print(f"{name}: {hex(addr) if addr else 'not found'}")


if __name__ == "__main__":
    main()