import sys,os
import PySide2
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QGroupBox, QGridLayout
from PySide2.QtGui import QIcon, QFont

# Allow to find plugins needed for PySide2
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 Grid Layout")  # Configure le titre de la fenêtre
        self.setGeometry(300, 300, 500, 400)  # Configure la taille de la fenêtre

        self.setIcon()

        self.createGridLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def createGridLayout(self):
        self.groupBox = QGroupBox("Please choose one laguage")
        self.groupBox.setFont(QFont("Sanserif", 13))
        gridLayout = QGridLayout()

        button = QPushButton("C++", self)
        button.setIcon(QIcon("icon.png"))
        gridLayout.addWidget(button, 0, 0)

        button2 = QPushButton("Css", self)
        button2.setIcon(QIcon("icon.png"))
        gridLayout.addWidget(button2, 0, 1)

        button3 = QPushButton("Javascript", self)
        button3.setIcon(QIcon("icon.png"))
        gridLayout.addWidget(button3, 1, 0)

        button4 = QPushButton("C#", self)
        button4.setIcon(QIcon("icon.png"))
        gridLayout.addWidget(button4, 1, 1)

        button5 = QPushButton("Python", self)
        button5.setIcon(QIcon("icon.png"))
        gridLayout.addWidget(button5, 2, 0)

        self.groupBox.setLayout(gridLayout)


myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)