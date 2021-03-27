import sys,os
import PySide2
from PySide2.QtWidgets import QApplication,QMainWindow, QPushButton, QGraphicsItem, QGraphicsView, QGraphicsScene
from PySide2.QtGui import QBrush, QPen, QFont
from PySide2.QtCore import Qt

# Allow to find plugins needed for PySide2
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class Window(QMainWindow):


    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pyside2 Graphics Scene")
        self.setGeometry(300, 200, 640, 520)
        self.create_ui()

    def create_ui(self):
        button = QPushButton("Rotate - ", self)
        button.setGeometry(200, 450, 100, 50)
        button.clicked.connect(self.rotateMinus)


        button2 = QPushButton("Rotate + ", self)
        button2.setGeometry(320, 450, 100, 50)
        button2.clicked.connect(self.rotatePlus)

        scene = QGraphicsScene(self)

        greenBrush = QBrush(Qt.green)
        blueBrush = QBrush(Qt.blue)

        blackPen = QPen(Qt.black)
        blackPen.setWidth(5)

        ellipse = scene.addEllipse(10,10, 200, 200, blackPen, greenBrush)
        rect = scene.addRect(-100, -100, 200, 200, blackPen, blueBrush)

        scene.addText("antoine-libert.com", QFont("Sanserif", 15))

        ellipse.setFlag(QGraphicsItem.ItemIsMovable)
        rect.setFlag(QGraphicsItem.ItemIsMovable)


        self.view = QGraphicsView(scene, self)
        self.view.setGeometry(0 ,0 ,640 ,440)


    def rotateMinus(self):
        self.view.rotate(-14)

    def rotatePlus(self):
        self.view.rotate(14)


myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)