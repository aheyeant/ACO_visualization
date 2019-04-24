import sys

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtWidgets import QApplication, QPushButton, QSlider, QWidget, QLabel, QAction, QMessageBox

from src.ACO import ACO
from src.Communicator import Communicator
from src.Constants import MAP_SIZE, NODE_COLOR, PIXEL_SIZE, START_COLOR, PATH_COLOR
from src.MapCreator import MapCreator
from src.GUIConstants import *


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self._variable_declaration()
        self._initialize()

    def _get_new_frame(self) -> bool:
        self.update()
        return True

    def _variable_declaration(self):
        self._paint_place: QRect = None

        self._check_new_frame_action = NotImplemented

        self._button_start = None
        self._button_stop = None
        self._button_new_map = None
        self._button_calculate_path = None

        self._sld_ants_count: int = None
        self._sld_alpha: float = None
        self._sld_beta: float = None
        self._sld_vaporize: float = None
        self._sld_random_factor: float = None
        self._sld_speed_frames: int = None
        self._sld_nodes_count: int = None
        self._sld_iterations: int = None

        self._label_sld_ants_count_name = None
        self._label_sld_ants_count_min = None
        self._label_sld_ants_count_max = None
        self._label_sld_ants_count_value = None

        self._label_sld_alpha_name = None
        self._label_sld_alpha_min = None
        self._label_sld_alpha_max = None
        self._label_sld_alpha_value = None

        self._label_sld_beta_name = None
        self._label_sld_beta_min = None
        self._label_sld_beta_max = None
        self._label_sld_beta_value = None

        self._label_sld_vaporize_name = None
        self._label_sld_vaporize_min = None
        self._label_sld_vaporize_max = None
        self._label_sld_vaporize_value = None

        self._label_sld_random_factor_name = None
        self._label_sld_random_factor_min = None
        self._label_sld_random_factor_max = None
        self._label_sld_random_factor_value = None

        self._label_sld_speed_frames_name = None
        self._label_sld_speed_frames_min = None
        self._label_sld_speed_frames_max = None
        self._label_sld_speed_frames_value = None

        self._label_sld_nodes_count_name = None
        self._label_sld_nodes_count_min = None
        self._label_sld_nodes_count_max = None
        self._label_sld_nodes_count_value = None

        self._label_sld_iterations_name = None
        self._label_sld_iterations_min = None
        self._label_sld_iterations_max = None
        self._label_sld_iterations_value = None

        self._label_iteration_name = None
        self._label_iteration_value = None

        self._label_path_length_name = None
        self._label_path_length_value = None

        self._label_calculated_path_name = None
        self._label_calculated_path_value = None

        self._ants_count_value: int = ANTS_COUNT_DEFAULT
        self._alpha_value = ALPHA_DEFAULT
        self._beta_value = BETA_DEFAULT
        self._vaporize_value = VAPORIZE_DEFAULT
        self._random_factor_value = RANDOM_FACTOR_DEFAULT
        self._frame_speed_value = SPEED_FRAME_DEFAULT
        self._nodes_count_value = NODES_COUNT_DEFAULT
        self._iterations_value = ITERATIONS_DEFAULT

        self._aco: ACO = ACO()
        self._map_creator: MapCreator = MapCreator()
        self._communicator = Communicator()

    def _initialize(self):
        self.resize(DISPLAY_WIDTH, DISPLAY_HEIGHT)
        self._visual_init()
        self._variable_initialize()
        self.show()

    def _variable_initialize(self):
        self._button_initialize()
        self._label_initialize()
        self._sld_initialize()
        self._action_initialize()
        self._tools_place_initialize()

    def _label_initialize(self):
        self._label_sld_ants_count_name = self._label_init(SLD_ANTS_COUNT_LABEL_NAME)
        self._label_sld_ants_count_min = self._label_init(SLD_ANTS_COUNT_LABEL_MIN)
        self._label_sld_ants_count_max = self._label_init(SLD_ANTS_COUNT_LABEL_MAX)
        self._label_sld_ants_count_value = self._label_init(str(SLD_ANTS_COUNT_RANGE[0]))

        self._label_sld_alpha_name = self._label_init(SLD_ALPHA_LABEL_NAME)
        self._label_sld_alpha_min = self._label_init(SLD_ALPHA_LABEL_MIN)
        self._label_sld_alpha_max = self._label_init(SLD_ALPHA_LABEL_MAX)
        self._label_sld_alpha_value = self._label_init(str(SLD_ALPHA_RANGE[0]))

        self._label_sld_beta_name = self._label_init(SLD_BETA_LABEL_NAME)
        self._label_sld_beta_min = self._label_init(SLD_BETA_LABEL_MIN)
        self._label_sld_beta_max = self._label_init(SLD_BETA_LABEL_MAX)
        self._label_sld_beta_value = self._label_init(str(SLD_BETA_RANGE[0]))

        self._label_sld_vaporize_name = self._label_init(SLD_VAPORIZE_LABEL_NAME)
        self._label_sld_vaporize_min = self._label_init(SLD_VAPORIZE_LABEL_MIN)
        self._label_sld_vaporize_max = self._label_init(SLD_VAPORIZE_LABEL_MAX)
        self._label_sld_vaporize_value = self._label_init(str(SLD_VAPORIZE_RANGE[0]))

        self._label_sld_random_factor_name = self._label_init(SLD_RANDOM_FACTOR_LABEL_NAME)
        self._label_sld_random_factor_min = self._label_init(SLD_RANDOM_FACTOR_LABEL_MIN)
        self._label_sld_random_factor_max = self._label_init(SLD_RANDOM_FACTOR_LABEL_MAX)
        self._label_sld_random_factor_value = self._label_init(str(SLD_RANDOM_FACTOR_RANGE[0]))

        self._label_sld_speed_frames_name = self._label_init(SLD_SPEED_FRAME_LABEL_NAME)
        self._label_sld_speed_frames_min = self._label_init(SLD_SPEED_FRAME_LABEL_MIN)
        self._label_sld_speed_frames_max = self._label_init(SLD_SPEED_FRAME_LABEL_MAX)
        self._label_sld_speed_frames_value = self._label_init(str(SLD_SPEED_FRAME_RANGE[0]))

        self._label_sld_nodes_count_name = self._label_init(SLD_NODES_COUNT_LABEL_NAME)
        self._label_sld_nodes_count_min = self._label_init(SLD_NODES_COUNT_LABEL_MIN)
        self._label_sld_nodes_count_max = self._label_init(SLD_NODES_COUNT_LABEL_MAX)
        self._label_sld_nodes_count_value = self._label_init(str(SLD_NODES_COUNT_RANGE[0]))

        self._label_sld_iterations_name = self._label_init(SLD_ITERATIONS_LABEL_NAME)
        self._label_sld_iterations_min = self._label_init(SLD_ITERATIONS_LABEL_MIN)
        self._label_sld_iterations_max = self._label_init(SLD_ITERATIONS_LABEL_MAX)
        self._label_sld_iterations_value = self._label_init(str(SLD_ITERATIONS_RANGE[0]))

        self._label_path_length_name = self._label_init(MIN_PATH_LABEL_NAME)
        self._label_path_length_value = self._label_init(MIN_PATH_LABEL_DEFAULT)

        self._label_iteration_name = self._label_init(ITERATIONS_LABEL_NAME)
        self._label_iteration_value = self._label_init(ITERATIONS_LABEL_DEFAULT)

        self._label_calculated_path_name = self._label_init(CALCULATED_PATH_LABEL_NAME)
        self._label_calculated_path_value = self._label_init(CALCULATED_PATH_LABEL_DEFAULT)

    def _label_init(self, text: str) -> QLabel:
        label = QLabel(self)
        label.setText(text)
        return label

    def _action_initialize(self):
        self._check_new_frame_action = QAction("new_frame", self)
        self._check_new_frame_action.triggered.connect(self._get_new_frame)

    def _button_initialize(self):
        self._button_start = QPushButton(BUTTON_START_NAME, self)
        self._button_start.clicked.connect(self._click_button_start)

        self._button_stop = QPushButton(BUTTON_STOP_NAME, self)
        self._button_stop.clicked.connect(self._click_button_stop)

        self._button_new_map = QPushButton(BUTTON_NEW_MAP_NAME, self)
        self._button_new_map.clicked.connect(self._click_button_new_map)

        self._button_calculate_path = QPushButton(BUTTON_CALCULATE_PATH_NAME, self)
        self._button_calculate_path.clicked.connect(self._click_button_calculate_path)

    def _sld_initialize(self):
        self._sld_ants_count = self._sld_init(self._sld_ants_count_change_value, POSITION_ANTS_COUNT_DEFAULT)
        self._sld_alpha = self._sld_init(self._sld_alpha_change_value, POSITION_ALPHA_DEFAULT)
        self._sld_beta = self._sld_init(self._sld_beta_change_value, POSITION_BETA_DEFAULT)
        self._sld_vaporize = self._sld_init(self._sld_vaporize_change_value, POSITION_VAPORIZE_DEFAULT)
        self._sld_speed_frames = self._sld_init(self._sld_speed_frames_change_value, POSITION_SPEED_FRAME_DEFAULT)
        self._sld_nodes_count = self._sld_init(self._sld_nodes_count_change_value, POSITION_NODES_COUNT_DEFAULT)
        self._sld_iterations = self._sld_init(self._sld_iterations_change_value, POSITION_ITERATIONS_RANGE_DEFAULT)
        self._sld_random_factor = self._sld_init(self._sld_random_factor_change_value, POSITION_RANDOM_FACTOR_DEFAULT)

    def _sld_init(self, triggered_function, position) -> QSlider:
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.valueChanged[int].connect(triggered_function)
        sld.setValue(position)
        return sld

    def _tools_place_initialize(self):
        self._paint_place = QRect(0, 0, *PAINT_PART_SIZE)

        top: int = 30

        top = self._place_for_sld(top, self._sld_ants_count,
                                  self._label_sld_ants_count_name,
                                  self._label_sld_ants_count_min,
                                  self._label_sld_ants_count_max,
                                  self._label_sld_ants_count_value)

        top = self._place_for_sld(top, self._sld_alpha,
                                  self._label_sld_alpha_name,
                                  self._label_sld_alpha_min,
                                  self._label_sld_alpha_max,
                                  self._label_sld_alpha_value)

        top = self._place_for_sld(top, self._sld_beta,
                                  self._label_sld_beta_name,
                                  self._label_sld_beta_min,
                                  self._label_sld_beta_max,
                                  self._label_sld_beta_value)

        top = self._place_for_sld(top, self._sld_vaporize,
                                  self._label_sld_vaporize_name,
                                  self._label_sld_vaporize_min,
                                  self._label_sld_vaporize_max,
                                  self._label_sld_vaporize_value)

        top = self._place_for_sld(top, self._sld_random_factor,
                                  self._label_sld_random_factor_name,
                                  self._label_sld_random_factor_min,
                                  self._label_sld_random_factor_max,
                                  self._label_sld_random_factor_value)

        top = self._place_for_sld(top, self._sld_speed_frames,
                                  self._label_sld_speed_frames_name,
                                  self._label_sld_speed_frames_min,
                                  self._label_sld_speed_frames_max,
                                  self._label_sld_speed_frames_value)

        top = self._place_for_sld(top, self._sld_nodes_count,
                                  self._label_sld_nodes_count_name,
                                  self._label_sld_nodes_count_min,
                                  self._label_sld_nodes_count_max,
                                  self._label_sld_nodes_count_value)

        top = self._place_for_sld(top, self._sld_iterations,
                                  self._label_sld_iterations_name,
                                  self._label_sld_iterations_min,
                                  self._label_sld_iterations_max,
                                  self._label_sld_iterations_value)

        top = self._place_for_button(top, self._button_start)
        top = self._place_for_button(top, self._button_stop)
        top = self._place_for_button(top, self._button_new_map)
        top = self._place_for_button(top, self._button_calculate_path)

        top = self._place_for_info_label(top, self._label_iteration_name, self._label_iteration_value)
        top = self._place_for_info_label(top, self._label_path_length_name, self._label_path_length_value)
        top = self._place_for_info_label(top, self._label_calculated_path_name, self._label_calculated_path_value)

    def _place_for_sld(self, top: int, sld: QSlider, name_sld: QLabel, min_sld: QLabel,
                       max_sld: QLabel, value_sld: QLabel) -> int:
        sld_rect: QRect = self._calculate_position(top + 20, SLD_SIZE)
        sld.setGeometry(sld_rect)

        name_rect: QRect = QRect(sld_rect.x(), sld_rect.y() - 20, *SLD_SIZE)
        name_sld.setGeometry(name_rect)

        min_rect: QRect = QRect(sld_rect.x() - 20, sld_rect.y() + 20, *LABEL_MIN_MAX_SIZE)
        min_sld.setGeometry(min_rect)

        max_rect: QRect = QRect(sld_rect.x() + SLD_SIZE[0] - 10, sld_rect.y() + 20, *LABEL_MIN_MAX_SIZE)
        max_sld.setGeometry(max_rect)

        value_rect: QRect = QRect(sld_rect.x() + SLD_SIZE[0] // 2 - 10, sld_rect.y() + 20, *LABEL_MIN_MAX_SIZE)
        value_sld.setGeometry(value_rect)

        return top + 40 + SLD_SIZE[1]

    def _place_for_button(self, top: int, button: QPushButton) -> int:
        button.setGeometry(self._calculate_position(top, BUTTON_SIZE))
        return top + BUTTON_SIZE[1] + 20

    def _place_for_info_label(self, top: int, name: QLabel, value: QLabel) -> int:
        name_rect: QRect = self._calculate_position(top, LABEL_VALUE_SIZE)
        name.setGeometry(name_rect)

        value_rect: QRect = QRect(name_rect.x(), name_rect.y() + LABEL_VALUE_SIZE[1], *LABEL_VALUE_SIZE)
        value.setGeometry(value_rect)
        return top + 2 * LABEL_VALUE_SIZE[1] + 20

    @staticmethod
    def _calculate_position(top_size: int, rect: tuple) -> QRect:
        x = PAINT_PART_SIZE[0] + (TOOLS_PART_WIDTH - rect[0]) // 2
        return QRect(x, top_size, *rect)

    def _visual_init(self):
        self.setWindowTitle("ACO algorithm")

    def _click_button_start(self) -> bool:
        if self._aco is None or not self._aco.has_map or self._aco.used:
            return True
        if not self._aco.started:
            print("START")
            self._aco.initialize(self._check_new_frame_action,
                                 self._communicator,
                                 self._alpha_value,
                                 self._beta_value,
                                 self._vaporize_value,
                                 self._frame_speed_value,
                                 self._ants_count_value,
                                 self._iterations_value,
                                 self._random_factor_value)
            self._aco.start()
        return True

    def _click_button_stop(self) -> bool:
        self._aco.stop()
        # self._aco = None
        return True

    def _click_button_new_map(self) -> bool:
        self._aco.stop()
        self._communicator.reload()
        self._aco = ACO()
        self._aco.set_map(self._map_creator.get_map(self._nodes_count_value, MAP_SIZE))
        self._communicator.draw_place = self._aco.map.get_frame()
        self._communicator.work_place = self._communicator.draw_place
        self._label_calculated_path_value.setText(CALCULATED_PATH_LABEL_DEFAULT)
        self.update()
        return True

    def _click_button_calculate_path(self) -> bool:
        if self._aco is not None:
            if self._aco.has_map:
                if self._aco.map.min_path_len == -1:
                    if self._nodes_count_value > 10:
                        if QMessageBox().question(self,
                                                  "Message",
                                                  "Nodes count > 10, long time calculate",
                                                  QMessageBox.Yes | QMessageBox.No,
                                                  QMessageBox.No) == QMessageBox.No:
                            return True

                    self._aco.map.calculate_min_path()
                self._label_calculated_path_value.setText(str(self._aco.map.min_path_len))
                return True
        self._label_calculated_path_value.setText(CALCULATED_PATH_LABEL_DEFAULT)
        return True

    def _sld_ants_count_change_value(self, value: int):
        one_step = SLD_ANTS_COUNT_RANGE[1] / 100
        self._ants_count_value = int(SLD_ANTS_COUNT_RANGE[0] + value * one_step)
        self._label_sld_ants_count_value.setText(str(self._ants_count_value))

    def _sld_alpha_change_value(self, value: int):
        one_step = SLD_ALPHA_RANGE[1] * 10 / 100
        self._alpha_value = int(SLD_ALPHA_RANGE[0] * 10 + value * one_step) / 10
        self._label_sld_alpha_value.setText(str(self._alpha_value))

    def _sld_beta_change_value(self, value: int):
        one_step = SLD_BETA_RANGE[1] * 10 / 100
        self._beta_value = int(SLD_BETA_RANGE[0] * 10 + value * one_step) / 10
        self._label_sld_beta_value.setText(str(self._beta_value))

    def _sld_vaporize_change_value(self, value: int):
        one_step = SLD_VAPORIZE_RANGE[1] / 100
        self._vaporize_value = (SLD_VAPORIZE_RANGE[0] + value * one_step)
        if value > 50:
            self._vaporize_value += 0.01
        self._label_sld_vaporize_value.setText(str(self._vaporize_value))

    def _sld_random_factor_change_value(self, value: int):
        one_step = SLD_RANDOM_FACTOR_RANGE[1] / 100
        self._random_factor_value = (SLD_RANDOM_FACTOR_RANGE[0] + value * one_step)
        if value > 50:
            self._random_factor_value += 0.01
        self._label_sld_random_factor_value.setText(str(self._random_factor_value))

    def _sld_speed_frames_change_value(self, value: int):
        if value != 0:
            value += 1
        one_step = (SLD_SPEED_FRAME_RANGE[1] - SLD_SPEED_FRAME_RANGE[0]) / 100
        self._frame_speed_value = int(SLD_SPEED_FRAME_RANGE[0] + value * one_step)
        self._label_sld_speed_frames_value.setText(str(self._frame_speed_value))

    def _sld_nodes_count_change_value(self, value: int):
        one_step = SLD_NODES_COUNT_RANGE[1] / 100
        self._nodes_count_value = int(SLD_NODES_COUNT_RANGE[0] + value * one_step)
        self._label_sld_nodes_count_value.setText(str(self._nodes_count_value))

    def _sld_iterations_change_value(self, value: int):
        one_step = SLD_ITERATIONS_RANGE[1] / 100
        self._iterations_value = int(SLD_ITERATIONS_RANGE[0] + value * one_step)
        self._label_sld_iterations_value.setText(str(self._iterations_value))

#    def _draw(self, qp: QPainter):
#        if self._aco.has_image():
#            for i in range(self._aco.image.size[1]):
#                for j in range(self._aco.image.size[0]):
#                    qp.setPen(self._aco.image.pix_map[i][j].current)
#                    qp.drawPoint(j, i)

    def _draw(self, qp: QPainter):
        if self._aco is not None:
            self._label_path_length_value.setText(str(self._aco.min_path))
            self._label_iteration_value.setText(str(self._aco.iterations))
        else:
            self._label_path_length_value.setText(MIN_PATH_LABEL_DEFAULT)
            self._label_iteration_value.setText(ITERATIONS_LABEL_DEFAULT)

        if self._communicator.draw_place.good:
            brush = qp.brush()
            for line in self._communicator.draw_place.lines:
                qp.setPen(line[2])
                qp.drawLine(line[0].x * PIXEL_SIZE + PIXEL_SIZE // 2,
                            line[0].y * PIXEL_SIZE + PIXEL_SIZE // 2,
                            line[1].x * PIXEL_SIZE + PIXEL_SIZE // 2,
                            line[1].y * PIXEL_SIZE + PIXEL_SIZE // 2)

            qp.setPen(PATH_COLOR)
            for line in self._communicator.draw_place.path:
                qp.drawLine(line[0].x * PIXEL_SIZE + PIXEL_SIZE // 2,
                            line[0].y * PIXEL_SIZE + PIXEL_SIZE // 2,
                            line[1].x * PIXEL_SIZE + PIXEL_SIZE // 2,
                            line[1].y * PIXEL_SIZE + PIXEL_SIZE // 2)

            qp.setPen(NODE_COLOR)
            qp.setBrush(QBrush(NODE_COLOR))
            for node in self._communicator.draw_place.nodes:
                qp.drawRect(node.x * PIXEL_SIZE,
                            node.y * PIXEL_SIZE,
                            PIXEL_SIZE,
                            PIXEL_SIZE)
            qp.setPen(START_COLOR)
            qp.setBrush(QBrush(START_COLOR))
            qp.drawRect(self._communicator.draw_place.start.x * PIXEL_SIZE,
                        self._communicator.draw_place.start.y * PIXEL_SIZE,
                        PIXEL_SIZE,
                        PIXEL_SIZE)
            qp.setBrush(brush)

    def closeEvent(self, e):
        self._aco.stop()
        super().closeEvent(e)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self._draw(qp)
        qp.end()

    def moveEvent(self, e):
        super().moveEvent(e)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec_())
