from PyQt5.QtGui import QColor

from src.Coordinate import Coordinate


class Line:
    def __init__(self, c_from: Coordinate, c_to: Coordinate, i_from, i_to):
        self.c_from: Coordinate = c_from
        self.c_to: Coordinate = c_to
        self.i_from: int = i_from
        self.i_to: int = i_to
        self.distance: float = Coordinate.distance(c_from, c_to)
        self.pheromone: float = 0
        self.attractiveness: float = self.pheromone / self.distance
        self.walks: int = 0
        self.no_draw: bool = True
        self.color: QColor = self._get_color()

    def add_pheromone(self, pheromone):
        self.pheromone += pheromone

    def get_next_id(self, c: Coordinate) -> int:
        return self.i_from if c == self.c_to else self.i_to

    def check_data(self, alpha=1, beta=1, vaporize=1, max_attractiveness: float = 1):
        self.color = self._get_color(max_attractiveness)
        self.attractiveness = (1 - vaporize) * self.attractiveness \
                              + self.pheromone ** alpha \
                              / self.distance ** beta
        self.pheromone = 0

    def _get_color(self, max_attractiveness: float = 0) -> QColor:
        if max_attractiveness == 0:
            tmp = 250
        else:
            tmp = 255 - int(self.attractiveness / max_attractiveness * 250)
        tmp -= 60
        if tmp < 0:
            tmp = 0
        if tmp > 180:
            self.no_draw = True
        else:
            self.no_draw = False
        return QColor(tmp, tmp, tmp)
        # return LINE_COLOR[tmp if tmp <= LINE_COLORS_RANGE_MAX else LINE_COLORS_RANGE_MAX]

    def __eq__(self, other):
        return self.c_from == other.c_from and self.c_to == other.c_to

    def __lt__(self, other):
        return self.attractiveness < other.attractiveness
