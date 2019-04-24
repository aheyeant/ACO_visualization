from src.Coordinate import Coordinate
from src.Line import Line


class Node:
    def __init__(self, ident: int, position: Coordinate):
        self.position: Coordinate = position
        self.ident: int = ident
        self.lines: list[Line] = []

    def add_line(self, line: Line):
        self.lines.append(line)

    def find_by_id(self, ident: int) -> Line:
        for line in self.lines:
            if line.i_to == ident or line.i_from == ident:
                return line
        raise ValueError("Con not find line by id \"" + str(ident) + "\"")
