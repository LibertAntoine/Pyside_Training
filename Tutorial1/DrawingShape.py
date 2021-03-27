import sys,os
import PySide2
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QIcon, QPainter, QBrush, QPen, QPolygon
from PySide2.QtCore import Qt, QPoint

# Allow to find plugins needed for PySide2
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 Icon")  # Configure le titre de la fenêtre
        self.setGeometry(300, 300, 500, 400)  # Configure la taille de la fenêtre

        self.setIcon()


    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 2, Qt.DashDotLine))
        painter.setBrush(QBrush(Qt.green, Qt.DiagCrossPattern))

        painter.drawEllipse(100, 100, 400, 200)
        painter.drawRect(200, 150, 400, 200)

        points = QPolygon([
            QPoint(10, 10),
            QPoint(10, 100),
            QPoint(100, 10),
            QPoint(100, 80)

        ])
        painter.drawPolygon(points)



myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)