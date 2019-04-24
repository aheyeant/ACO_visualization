from PyQt5.QtGui import QColor

DRAW_PLACE_SIZE = (1000, 1000)

MAP_SIZE = (200, 200)
PIXEL_SIZE = DRAW_PLACE_SIZE[0] // MAP_SIZE[0]


SECURITY_ZONE = 5

MAX_NODES = MAP_SIZE[0] * MAP_SIZE[1] // (SECURITY_ZONE * 2 + 1) ** 2 * 9 // 10

# colors ------------
NODE_COLOR: QColor = QColor(0, 255, 0)
START_COLOR: QColor = QColor(255, 0, 0)
PATH_COLOR: QColor = QColor(255, 100, 100)


LINE_COLOR = [QColor(200, 200, 200), QColor(200, 200, 200), QColor(160, 160, 160), QColor(140, 140, 140),
              QColor(120, 120, 120), QColor(100, 100, 100), QColor(80, 80, 80), QColor(60, 60, 60),
              QColor(40, 40, 40), QColor(20, 20, 20)]

LINE_COLORS_RANGE_MAX = len(LINE_COLOR) - 1
PHEROMONE_ON_GROUP = 100
# -------------------
