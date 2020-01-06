import sys
import matplotlib.pyplot as mp
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolBar
from matplotlib.figure import Figure
import random as rand
import hopalong as h
from math import sqrt
from qtpy import QtCore as qc, QtWidgets as qw, QtGui as qg

class DataWindow(qw.QMainWindow):
    def __init__(self, hopalong, parent=None):
        super().__init__(parent)

        self.setAttribute(qc.Qt.WA_DeleteOnClose)
        self.setWindowTitle("Datos de Hopalong")

        self._main = qw.QWidget()
        self.setCentralWidget(self._main)
        main_layout = qw.QVBoxLayout(self._main)

        self.fixed_points_label = qw.QLabel("Puntos fijos: " + str(hopalong.fixed_points()))
        self.k_per_2 = qw.QLabel("2-Periódicos: " + str(hopalong.k_periods_2()))
        self.k_per_3 = qw.QLabel("3-Periódicos: " + str(hopalong.k_periods_3()))
        self.k_per_4 = qw.QLabel("4-Periódicos: " + str(hopalong.k_periods_4()))
        self.lyapunov = qw.QLabel("Exponente de Lyapunov: " + str(hopalong.exp_lyapunov()))

        main_layout.addWidget(self.fixed_points_label)
        main_layout.addWidget(self.k_per_2)
        main_layout.addWidget(self.k_per_3)
        main_layout.addWidget(self.k_per_4)
        main_layout.addWidget(self.lyapunov)


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
        random_button = qw.QPushButton("Puntos aleatorios")
        selected_points_button = qw.QPushButton("Puntos elegidos")
        data_button = qw.QPushButton("Ver datos")
        
        self.alpha_text = qw.QLineEdit("3.")
        self.beta_text = qw.QLineEdit("2.")
        self.delta_text = qw.QLineEdit("1.")
        self.n_points_text = qw.QLineEdit("25")
        self.iterations_text = qw.QLineEdit("5000")

        self.x_points_text = qw.QLineEdit("")
        self.y_points_text = qw.QLineEdit("")

        alpha_label = qw.QLabel("Alpha")
        beta_label = qw.QLabel("Beta")
        delta_label = qw.QLabel("Delta")
        n_points_label = qw.QLabel("Número de puntos aleatorios")
        iterations_label = qw.QLabel("Iteraciones")
        x_points_label = qw.QLabel("Puntos X: ")
        y_points_label = qw.QLabel("Puntos Y: ")

        random_button.clicked.connect(self.reset)
        selected_points_button.clicked.connect(self.selected_points)
        data_button.clicked.connect(self.view_data)

        elements_layout.addWidget(alpha_label)
        elements_layout.addWidget(self.alpha_text)
        elements_layout.addWidget(beta_label)
        elements_layout.addWidget(self.beta_text)
        elements_layout.addWidget(delta_label)
        elements_layout.addWidget(self.delta_text)
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
        elements_layout.addWidget(data_button)
        main_layout.addWidget(hopalong_canvas)

        self._dynamic_ax = hopalong_canvas.figure.subplots()

        alpha = float(self.alpha_text.text())
        beta = float(self.beta_text.text())
        delta = float(self.delta_text.text())
        n_points = int(self.n_points_text.text())
        iterations = int(self.iterations_text.text())

        self.update_function(alpha, beta, delta, n_points, iterations)

    def reset(self):
        alpha = float(self.alpha_text.text())
        beta = float(self.beta_text.text())
        delta = float(self.delta_text.text())
        n_points = int(self.n_points_text.text())
        iterations = int(self.iterations_text.text())

        self.update_function(alpha, beta, delta, n_points, iterations)

    def selected_points(self):
        alpha = float(self.alpha_text.text())
        beta = float(self.beta_text.text())
        delta = float(self.delta_text.text())
        n_points = 0
        iterations = int(self.iterations_text.text())
        
        if(len(self.x_points_text.text()) > 0 and len(self.y_points_text.text()) > 0):
            x = [float(i) for i in self.x_points_text.text().split(",")]
            y = [float(i) for i in self.y_points_text.text().split(",")]
        else:
            x = [0.]
            y = [0.]
        self.update_function(alpha, beta, delta, n_points, iterations, x, y)

    def update_function(self, alpha, beta, delta, n_points, iterations, x=None, y=None):
        self._dynamic_ax.clear()
        self.hopa = h.Hopalong(alpha, beta, delta, n_points, iterations, x, y)
        x = self.hopa.x
        y = self.hopa.y
        self._dynamic_ax.plot(x, y, ',')
        self._dynamic_ax.plot(x[0], y[0], '.', color='black')
        self._dynamic_ax.figure.canvas.draw()

    def view_data(self):
        widget = DataWindow(self.hopa, self)
        widget.resize(500,500)
        widget.show()


if __name__ == "__main__":
    app = qw.QApplication(sys.argv)

    widget = HopalongWindow()
    widget.resize(500,500)
    widget.show()

    sys.exit(app.exec_())
