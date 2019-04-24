import random

from src.Line import Line
from src.Map import Map
from src.Node import Node


class Iteration:
    def __init__(self, ant_map: Map, random_factor: int):
        self._map = ant_map
        self._random_factor = random_factor
        self._touched = [0 for _ in range(len(self._map.nodes))]
        self._touched[self._map.start.ident] = 1
        self.lines = []
        self.length: float = 0
        self._go()

    def _go(self):
        current_node = self._map.start
        for _ in range(len(self._touched)):
            line = self._next_line(current_node)
            self.length += line.distance
            self.lines.append(line)
            line.walks += 1
            current_node = self._map.nodes[line.i_to if line.i_to != current_node.ident else line.i_from]
            self._touched[current_node.ident] = 1

    def _next_line_todo(self, n_from: Node) -> Line:
        tmp = []
        attractiveness: float = 0
        for line in n_from.lines:
            if self._touched[line.get_next_id(n_from.position)] == 0:
                attractiveness += line.attractiveness
                tmp.append(line)
        if len(tmp) == 0:
            return n_from.find_by_id(self._map.start.ident)
        tmp.sort()
        # todo

    def _next_line(self, n_from: Node) -> Line:
        tmp = []
        attractiveness: float = 0
        for line in n_from.lines:
            if self._touched[line.get_next_id(n_from.position)] == 0:
                attractiveness += line.attractiveness
                tmp.append(line)
        if len(tmp) == 0:
            return n_from.find_by_id(self._map.start.ident)
        if attractiveness == 0:
            return tmp[random.randint(0, len(tmp) - 1)]
        if random.randint(0, 100) < self._random_factor:
            return tmp[random.randint(0, len(tmp) - 1)]
        chance = random.randint(0, 100)
        for line in tmp:
            if line.attractiveness == 0:
                continue
            chance -= int(line.attractiveness / attractiveness * 100)
            if chance <= 0:
                return line
        return tmp[-1]

    def __lt__(self, other):
        return self.length < other.length
