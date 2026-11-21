"""Static offsets for the current client build. Update on patch days."""

BUILD = "2026.01-r4"

OFFSETS = {
    "table_state": 0x00A13C20,
    "cue_angle": 0x00A13C88,
    "cue_power": 0x00A13C90,
    "spin_x": 0x00A13C94,
    "spin_y": 0x00A13C98,
    "ball_array": 0x00A14000,
    "pocket_table": 0x00A14500,
}

BALL_STRIDE = 0x40
MAX_BALLS = 16

POCKETS = [
    (128, 132), (960, 120), (1792, 132),
    (128, 908), (960, 920), (1792, 908),
]