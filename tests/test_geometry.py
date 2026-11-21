from src.shared.geometry import Vec2, ghost_ball, reflect


def test_ghost_ball_aligns_with_pocket():
    cue = Vec2(100, 100)
    target = Vec2(500, 300)
    pocket = Vec2(960, 120)
    ghost = ghost_ball(cue, target, pocket)
    assert ghost.x < target.x


def test_reflect_off_horizontal_wall():
    out = reflect(Vec2(1, 1), Vec2(0, 1))
    assert abs(out.y + 1.0) < 1e-6