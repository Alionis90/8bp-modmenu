from pathlib import Path

from src.host.registry import PluginRegistry


def test_registry_discovers_plugins():
    reg = PluginRegistry()
    reg.discover(Path("plugins"))
    assert len(reg) >= 1
    assert "aim_assist" in list(reg)