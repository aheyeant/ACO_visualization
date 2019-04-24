import time
from threading import Thread

from PyQt5.QtWidgets import QAction

from src.Communicator import Communicator
from src.Iteration import Iteration
from src.Map import Map


class ACO(Thread):
    def __init__(self):
        super().__init__()
        self.started = False
        self.has_map = False
        self.used = False
        self.map: Map = None
        self._action: QAction = None
        self._communicator: Communicator = None
        self._add_pheromone = 0
        self._sub_pheromone = 0
        self._alpha: float = 1
        self._beta: float = 1
        self._vaporize: float = 1
        self._delay = 0
        self._ants_count = 0
        self._max_iteration = 0
        self._random_factor: int = 0
        self.min_way: Iteration = None
        self._max_attractiveness: float = 0
        self.iterations = 0
        self.min_path = 0

    def set_map(self, ant_map: Map):
        self.map = ant_map
        self.has_map = True

    def initialize(self, action: QAction, communicator: Communicator, alpha, beta, vaporize,
                   delay, ants_count, iterations, random_factor):
        self._action = action
        self._communicator = communicator
        self._alpha = alpha
        self._beta = beta
        self._vaporize = vaporize
        self._delay = delay / 1000
        self._ants_count = ants_count
        self._max_iteration = iterations
        self._random_factor = int(random_factor * 100)

    def stop(self):
        self.started = False

    def run(self) -> None:
        self.started = True
        self.used = True
        while self.started:
            current = time.time()
            if self._max_iteration == self.iterations:
                return
            self._round()
            self._communicator.draw_place = self._communicator.work_place
            self._action.trigger()
            self._communicator.work_place = self.map.get_frame(self.min_way.lines)
            while (time.time() - current) < self._delay:
                pass

    def _round(self):
        self.iterations += 1
        tmp = []
        for i in range(self._ants_count):
            tmp.append(Iteration(self.map, self._random_factor))
        tmp.sort()
        if tmp[0].length < self.min_path or self.min_path == 0:
            print("New path len form:", self.min_path, "to", end=" ")
            self.min_path = tmp[0].length
            print(self.min_path, "iteration", self.iterations)
            self.min_way = tmp[0]
        self.min_path = tmp[0].length if tmp[0].length < self.min_path or self.min_path == 0 else self.min_path

        # self.min_path = tmp[0].length
        # important function
            # use one from:
                # _add_pheromone_all_lines
                # _add_pheromone_double_lines
                # _add_pheromone_per_length
        self._add_pheromone_per_length(tmp)
        # ------------------
        self._max_attractiveness = self.map.sub_pheromone_all(self._alpha,
                                                              self._beta,
                                                              self._vaporize,
                                                              self._max_attractiveness)

    @staticmethod
    def _add_pheromone_per_length(iterations: [Iteration]):
        for iteration in iterations:
            for line in iteration.lines:
                line.add_pheromone(1 / iteration.length)

    def _add_pheromone_all_lines(self, iterations: [Iteration]):
        for iteration in iterations:
            for line in iteration.lines:
                line.add_pheromone(self._add_pheromone)

    def _add_pheromone_double_lines(self, iterations: [Iteration]):
        for iteration in iterations:
            for line in iteration.lines:
                if line.walks > 1:
                    line.add_pheromone(self._add_pheromone * line.walks)
