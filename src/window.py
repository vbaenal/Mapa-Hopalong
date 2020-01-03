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
        reset_button = qw.QPushButton("Reset")
        
        self.alpha_text = qw.QLineEdit("25")
        self.beta_text = qw.QLineEdit("50")
        self.n_points_text = qw.QLineEdit("50")
        self.iterations_text = qw.QLineEdit("5000")

        self.delta_radio_button_0 = qw.QRadioButton("0")
        self.delta_radio_button_0.setChecked(True)
        self.delta_radio_button_1 = qw.QRadioButton("1")  

        alpha_label = qw.QLabel("Alpha")
        beta_label = qw.QLabel("Beta")
        delta_label = qw.QLabel("Delta")
        n_points_label = qw.QLabel("Random points")
        iterations_label = qw.QLabel("Iterations")

        reset_button.clicked.connect(self.reset)


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
        elements_layout.addWidget(reset_button)
        main_layout.addWidget(hopalong_canvas)
        self.addToolBar(qc.Qt.BottomToolBarArea,
                        NavigationToolBar(hopalong_canvas, self))

        self._dynamic_ax = hopalong_canvas.figure.subplots()

        alpha = int(self.alpha_text.text())
        beta = int(self.beta_text.text())
        delta = self.delta_state()
        n_points = int(self.n_points_text.text())
        iterations = int(self.iterations_text.text())

        self.update_function(alpha, beta, delta, n_points, iterations)

    def reset(self):
        alpha = int(self.alpha_text.text())
        beta = int(self.beta_text.text())
        delta = self.delta_state()
        n_points = int(self.n_points_text.text())
        iterations = int(self.iterations_text.text())

        self.update_function(alpha, beta, delta, n_points, iterations)

    def delta_state(self):
        if (self.delta_radio_button_0.isChecked()):
            return 0
        else:
            return 1

    def update_function(self, alpha, beta, delta, n_points, iterations):
        self._dynamic_ax.clear()
        hopa = h.Hopalong(alpha, beta, delta, n_points, iterations)
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
