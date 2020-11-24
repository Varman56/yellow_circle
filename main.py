import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from UI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication


class Circles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Git и желтые окружности')
        self.do_paint = False
        self.draw_btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        cnt = randint(3, 100)
        for i in range(cnt):
            qp.setBrush(
                QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            x, y = randint(0, self.width()), randint(0, self.height())
            d = randint(5, 100)
            qp.drawEllipse(x, y, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())
