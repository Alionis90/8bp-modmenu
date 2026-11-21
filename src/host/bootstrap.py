"""Entry point for the 8bp-modmenu host process."""
from __future__ import annotations

import sys
from pathlib import Path

from loguru import logger

from src.host.plugin_host import PluginHost
from src.host.registry import PluginRegistry
from src.shared.config import load_config


def main() -> int:
    cfg = load_config(Path("config/default.yaml"))
    logger.remove()
    logger.add(sys.stderr, level=cfg.log_level)
    logger.info("8bp-modmenu starting (build={})", cfg.build_tag)

    registry = PluginRegistry()
    registry.discover(Path("plugins"))

    host = PluginHost(registry=registry, config=cfg)
    try:
        host.run()
    except KeyboardInterrupt:
        logger.info("shutdown requested")
    finally:
        host.shutdown()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())