from src.Coordinate import Coordinate
from src.Line import Line
from src.Map import Map
from src.Constants import *
from src.Node import Node


class MapCreator:
    def __init__(self):
        self._map: Map = None
        self._tmp = None

    def get_map(self, nodes: int, map_size: (int, int)) -> Map:
        self._map = Map(map_size)

        self._init_map(nodes if nodes <= MAX_NODES else MAX_NODES)
        return self._map

    def _init_map(self, nodes: int):
        self._set_nodes(nodes)
        self._set_lines()
        self._set_start()

    def _set_lines(self):
        for i in range(0, len(self._map.nodes) - 1):
            for j in range(i + 1, len(self._map.nodes)):
                line = Line(self._map.nodes[i].position,
                            self._map.nodes[j].position,
                            self._map.nodes[i].ident,
                            self._map.nodes[j].ident)
                self._map.lines.append(line)
                self._map.nodes[i].add_line(line)
                self._map.nodes[j].add_line(line)

    def _set_nodes(self, nodes: int):
        self._tmp = [[0 for _ in range(self._map.size[0])] for _ in range(self._map.size[1])]
        while len(self._map.nodes) != nodes:
            new_coordinate = Coordinate.random_coordinate((SECURITY_ZONE, MAP_SIZE[0] - SECURITY_ZONE - 1),
                                                          (SECURITY_ZONE, MAP_SIZE[1] - SECURITY_ZONE - 1))
            if self._check_node_place(new_coordinate):
                self._map.nodes.append(Node(len(self._map.nodes), new_coordinate))
                self._tmp[new_coordinate.y][new_coordinate.x] = 1

    def _check_node_place(self, c: Coordinate) -> bool:
        for i in range(c.y - SECURITY_ZONE, c.y + SECURITY_ZONE):
            for j in range(c.x - SECURITY_ZONE, c.x + SECURITY_ZONE):
                if self._tmp[i][j] == 1:
                    return False
        return True

    def _set_start(self):
        self._map.start = self._map.nodes[0]
