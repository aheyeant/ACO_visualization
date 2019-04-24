from src.DrawItem import DrawItem


class Communicator:
    def __init__(self):
        self.work_place: DrawItem = DrawItem()
        self.draw_place: DrawItem = DrawItem()

    def reload(self):
        self.work_place: DrawItem = DrawItem()
        self.draw_place: DrawItem = DrawItem()
