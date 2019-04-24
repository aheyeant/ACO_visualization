import random
from math import sqrt


class Coordinate:
    def __init__(self, x: int=0, y: int=0):
        self.x = x
        self.y = y

    @staticmethod
    def distance(c1, c2) -> float:
        return sqrt(pow(c1.x - c2.x, 2) + pow(c1.y - c2.y, 2))

    @staticmethod
    def square_distance(c1, c2) -> float:
        return pow(c1.x - c2.x, 2) + pow(c1.y - c2.y, 2)

    @staticmethod
    def projection(c1, c2) -> (int, int, int):
        return c2.x - c1.x, c2.y - c1.y, abs(c1.x - c2.x) + abs(c1.y - c2.y)

    @staticmethod
    def get_vector(c1, c2) -> (float, float):
        tmp = abs(c1.x - c2.x) + abs(c1.y - c2.y)
        return (c2.x - c1.x) / tmp, (c2.y - c1.y) / tmp

    @staticmethod
    def get_around_coordinate(c) -> []:
        return [Coordinate(c.x - 1, c.y - 1),
                Coordinate(c.x, c.y - 1),
                Coordinate(c.x + 1, c.y - 1),
                Coordinate(c.x - 1, c.y),
                Coordinate(c.x + 1, c.y),
                Coordinate(c.x - 1, c.y + 1),
                Coordinate(c.x, c.y + 1),
                Coordinate(c.x + 1, c.y + 1)]

    @staticmethod
    def out_of_range(c, size: (int, int)) -> bool:
        return c.x < 0 or c.x >= size[0] or c.y < 0 or c.y >= size[1]

    @staticmethod
    def random_coordinate(x_interval: (int, int), y_interval: (int, int)):
        return Coordinate(random.randint(x_interval[0], x_interval[1]),
                          random.randint(y_interval[0], y_interval[1]))

    def __lt__(self, other):
        return self.y < other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __copy__(self):
        return Coordinate(self.x, self.y)

    def __str__(self):
        return "{x=" + str(self.x) + ",y=" + str(self.y) + "}"

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
