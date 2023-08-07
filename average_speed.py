from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
     QLineEdit, QPushButton, QComboBox

import sys


class AverageSpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # Create the widgets
        distance_label = QLabel("Distance:")
        self.distance_input = QLineEdit()
        self.unit_list = QComboBox()
        self.unit_list.addItems(["Metric (km)", "Imperial (miles)"])
        time_label = QLabel("Time (hours)")
        self.time_input = QLineEdit()
        calculate_button = QPushButton("Calculate average speed")
        calculate_button.clicked.connect(self.calc_speed)
        self.output_label = QLabel("")

        # Add widgets to the grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_input, 0, 1)
        grid.addWidget(self.unit_list, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_input, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 3)

        self.setLayout(grid)


    def calc_speed(self):
        # Get distance & time from the input boxes and calculate average speed
        distance = float(self.distance_input.text())
        hours = float(self.time_input.text())
        speed = distance / hours

        # Display results based on units chosen by user
        if self.unit_list.currentText() == "Metric (km)":
            self.output_label.setText(f"Average speed: {speed} km/h")
        if self.unit_list.currentText() == "Imperial (miles)":
            self.output_label.setText(f"Average speed: {speed} mph")



app = QApplication(sys.argv)
speed_calc = AverageSpeedCalculator()
speed_calc.show()
sys.exit(app.exec())
