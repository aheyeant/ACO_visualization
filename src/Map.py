from typing import Optional

from src.DrawItem import DrawItem
from src.Line import Line
from src.Node import Node


class Map:
    def __init__(self, size: (int, int)):
        self.size = size
        self.min_path_len: float = -1
        self.nodes: list[Node] = []
        self.lines: list[Line] = []
        self.start: Node = None

    def sub_pheromone_all(self, alpha=1, beta=1, vaporize: float = 1, max_attractiveness: float = 0) -> float:
        max_attr = max_attractiveness
        for line in self.lines:
            # line.sub_pheromone(pheromone)
            line.check_data(alpha, beta, vaporize, max_attractiveness)
            line.walks = 0
            if line.attractiveness > max_attr:
                max_attr = line.attractiveness
        return max_attr

    def get_frame(self, field: [Line]=None) -> DrawItem:
        item: DrawItem = DrawItem()
        item.good = True
        if field is not None:
            for line in field:
                item.path.append((line.c_from, line.c_to))
        item.start = self.start.position
        for node in self.nodes:
            item.nodes.append(node.position)
        for line in self.lines:
            if line.no_draw:
                continue
            item.lines.append((line.c_from, line.c_to, line.color))
        return item

    def calculate_min_path(self):
        self._rec_path_len([0 for _ in range(len(self.nodes))], self.start, 0)

    def _rec_path_len(self, field: [], n_from: Optional[Node], length: float):
        if field is None:
            if self.min_path_len == -1:
                self.min_path_len = length
                return
            elif self.min_path_len > length:
                self.min_path_len = length
                return
        if self.min_path_len != -1:
            if self.min_path_len <= length:
                return
        field[n_from.ident] = 1
        tmp = []
        for line in n_from.lines:
            if field[line.get_next_id(n_from.position)] == 0:
                tmp.append(self.nodes[line.get_next_id(n_from.position)])
        if len(tmp) == 0:
            self._rec_path_len(None,
                               None,
                               length + n_from.find_by_id(self.start.ident).distance)
            return
        else:
            for node in tmp:
                self._rec_path_len([field[i] for i in range(len(field))],
                                   node,
                                   length + node.find_by_id(n_from.ident).distance)
