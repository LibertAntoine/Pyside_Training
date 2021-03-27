import sys,os
import PySide2
from PySide2.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QSlider
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt
from PySide2 import QtGui

# Allow to find plugins needed for PySide2
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 Slider")  # Configure le titre de la fenêtre
        self.setGeometry(300, 300, 300, 250)  # Configure la taille de la fenêtre

        self.setIcon()
        self.setStyleSheet('background-color:grey')

        self.createSlider()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def createSlider(self):
        hbox = QHBoxLayout()

        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)

        self.slider.valueChanged.connect(self.changeValue)

        self.label = QLabel("0")
        self.setFont(QtGui.QFont("Sanserif", 15))

        hbox.addWidget(self.slider)
        hbox.addWidget(self.label)
        self.setLayout(hbox)

    def changeValue(self):
        size = self.slider.value()
        self.label.setText(str(size))

myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)