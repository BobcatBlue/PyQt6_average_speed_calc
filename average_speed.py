from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
     QLineEdit,QPushButton, QComboBox
import sys

class AverageSpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        distance_label = QLabel("Distance:")
        self.distance_input = QLineEdit()
        unit_list = QComboBox()
        unit_list.addItems(["Metric (km)", "Imperial (miles)"])
        time_label = QLabel("Time (hours)")
        self.time_input = QLineEdit()
        calculate_button = QPushButton("Calculate")
        self.output_label = QLabel("")

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_input, 0, 1)
        grid.addWidget(unit_list, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_input, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0)

        self.setLayout(grid)


app = QApplication(sys.argv)
speed_calc = AverageSpeedCalculator()
speed_calc.show()
sys.exit(app.exec())