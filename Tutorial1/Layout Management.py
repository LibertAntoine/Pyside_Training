import sys,os
import PySide2
from PySide2.QtWidgets import QApplication, QWidget, QDialog, QHBoxLayout, QVBoxLayout, QGroupBox, QPushButton
from PySide2.QtGui import QIcon, QFont

# Allow to find plugins needed for PySide2
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 Layout Management")  # Configure le titre de la fenêtre
        self.setGeometry(300, 300, 500, 400)  # Configure la taille de la fenêtre

        self.setIcon()
        
        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)
        
    def createLayout(self):
        self.groupBox = QGroupBox("Please choose one language")
        self.groupBox.setFont(QFont("Sanserif", 13))

        hbox = QHBoxLayout()

        button = QPushButton("CSS", self)
        button.setIcon(QIcon("icon.png"))
        button.setMinimumWidth(40)
        hbox.addWidget(button)

        button2 = QPushButton("C++", self)
        button2.setIcon(QIcon("icon.png"))
        button2.setMinimumWidth(40)
        hbox.addWidget(button2)

        button3 = QPushButton("Javascript", self)
        button3.setIcon(QIcon("icon.png"))
        button3.setMinimumWidth(40)
        hbox.addWidget(button3)

        self.groupBox.setLayout(hbox)

myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)