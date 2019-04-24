from PyQt5.QtGui import QColor

from src.Coordinate import Coordinate


class DrawItem:
    def __init__(self):
        self.good = False
        self.start: Coordinate = Coordinate()
        self.nodes: list[Coordinate] = []
        self.path: list[(Coordinate, Coordinate)] = []
        self.lines: list[(Coordinate, Coordinate, QColor)] = []
