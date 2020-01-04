import sys
import matplotlib.pyplot as mp
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolBar
from matplotlib.figure import Figure
import random as rand
import hopalong as h
from math import sqrt
from qtpy import QtCore as qc, QtWidgets as qw, QtGui as qg

class HopalongWindow(qw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setAttribute(qc.Qt.WA_DeleteOnClose)
        self.setWindowTitle("Mapa Hopalong")

        self._main = qw.QWidget()
        self.setCentralWidget(self._main)
        main_layout = qw.QHBoxLayout(self._main)

        elements_layout = qw.QFormLayout()
        main_layout.addLayout(elements_layout)

        hopalong_canvas = FigureCanvas(Figure(figsize=(7,7)))
        random_button = qw.QPushButton("Random points")
        selected_points_button = qw.QPushButton("Selected points")
        
        self.alpha_text = qw.QLineEdit("3.")
        self.beta_text = qw.QLineEdit("2.")
        self.n_points_text = qw.QLineEdit("25")
        self.iterations_text = qw.QLineEdit("5000")

        self.delta_radio_button_0 = qw.QRadioButton("0")
        self.delta_radio_button_0.setChecked(True)
        self.delta_radio_button_1 = qw.QRadioButton("1")

        self.x_points_text = qw.QLineEdit("")
        self.y_points_text = qw.QLineEdit("")

        alpha_label = qw.QLabel("Alpha")
        beta_label = qw.QLabel("Beta")
        delta_label = qw.QLabel("Delta")
        n_points_label = qw.QLabel("Random points")
        iterations_label = qw.QLabel("Iterations")
        x_points_label = qw.QLabel("X Points: ")
        y_points_label = qw.QLabel("Y Points: ")

        random_button.clicked.connect(self.reset)
        selected_points_button.clicked.connect(self.selected_points)

        elements_layout.addWidget(alpha_label)
        elements_layout.addWidget(self.alpha_text)
        elements_layout.addWidget(beta_label)
        elements_layout.addWidget(self.beta_text)
        elements_layout.addWidget(delta_label)
        elements_layout.addWidget(self.delta_radio_button_0)
        elements_layout.addWidget(self.delta_radio_button_1)
        elements_layout.addWidget(n_points_label)
        elements_layout.addWidget(self.n_points_text)
        elements_layout.addWidget(iterations_label)
        elements_layout.addWidget(self.iterations_text)
        elements_layout.addWidget(random_button)
        elements_layout.addWidget(x_points_label)
        elements_layout.addWidget(self.x_points_text)
        elements_layout.addWidget(y_points_label)
        elements_layout.addWidget(self.y_points_text)
        elements_layout.addWidget(selected_points_button)
        main_layout.addWidget(hopalong_canvas)
        self.addToolBar(qc.Qt.BottomToolBarArea,
                        NavigationToolBar(hopalong_canvas, self))

        self._dynamic_ax = hopalong_canvas.figure.subplots()

        alpha = float(self.alpha_text.text())
        beta = float(self.beta_text.text())
        delta = self.delta_state()
        n_points = int(self.n_points_text.text())
        iterations = int(self.iterations_text.text())

        self.update_function(alpha, beta, delta, n_points, iterations)

    def reset(self):
        alpha = float(self.alpha_text.text())
        beta = float(self.beta_text.text())
        delta = self.delta_state()
        n_points = int(self.n_points_text.text())
        iterations = int(self.iterations_text.text())

        self.update_function(alpha, beta, delta, n_points, iterations)

    def selected_points(self):
        alpha = float(self.alpha_text.text())
        beta = float(self.beta_text.text())
        delta = self.delta_state()
        n_points = 0
        iterations = int(self.iterations_text.text())
        
        if(len(self.x_points_text.text()) > 0 and len(self.y_points_text.text()) > 0):
            x = [float(i) for i in self.x_points_text.text().split(",")]
            y = [float(i) for i in self.y_points_text.text().split(",")]
        else:
            x = [0.]
            y = [0.]
        self.update_function(alpha, beta, delta, n_points, iterations, x, y)

    def delta_state(self):
        if (self.delta_radio_button_0.isChecked()):
            return 0
        else:
            return 1

    def update_function(self, alpha, beta, delta, n_points, iterations, x=None, y=None):
        self._dynamic_ax.clear()
        hopa = h.Hopalong(alpha, beta, delta, n_points, iterations, x, y)
        x = hopa.x
        y = hopa.y
        self._dynamic_ax.plot(x, y, ',')
        self._dynamic_ax.plot(x[0], y[0], '.', color='black')
        self._dynamic_ax.figure.canvas.draw()

if __name__ == "__main__":
    app = qw.QApplication(sys.argv)

    widget = HopalongWindow()
    widget.resize(500,500)
    widget.show()

    sys.exit(app.exec_())
