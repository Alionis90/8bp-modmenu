"""Transparent always-on-top overlay window, click-through by default."""
from __future__ import annotations

from typing import Callable

from PySide6 import QtCore, QtGui, QtWidgets

from src.shared.config import OverlayConfig


class OverlayWindow(QtWidgets.QWidget):
    def __init__(self, cfg: OverlayConfig) -> None:
        super().__init__()
        self.cfg = cfg
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint
            | QtCore.Qt.FramelessWindowHint
            | QtCore.Qt.Tool
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        if cfg.click_through:
            self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        self.resize(cfg.width, cfg.height)
        self._lines: list[list[tuple[float, float]]] = []

    def highlight(self, points: list[tuple[float, float]]) -> None:
        self._lines = [points]
        self.update()

    def paintEvent(self, _evt: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        pen = QtGui.QPen(QtGui.QColor("#00ff88"))
        pen.setWidth(2)
        painter.setPen(pen)
        for line in self._lines:
            for a, b in zip(line, line[1:]):
                painter.drawLine(int(a[0]), int(a[1]), int(b[0]), int(b[1]))

    def loop(self, tick: Callable[[float], None]) -> None:
        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda: tick(1.0 / self.cfg.fps))
        timer.start(int(1000 / self.cfg.fps))
        QtWidgets.QApplication.instance().exec()