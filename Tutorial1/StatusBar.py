import sys,os
import PySide2
from PySide2.QtWidgets import QApplication, QMainWindow, QStatusBar
from PySide2.QtGui import QIcon, QPixmap

# Allow to find plugins needed for PySide2
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 Status Bar")  # Configure le titre de la fenêtre
        self.setGeometry(300, 300, 500, 400)  # Configure la taille de la fenêtre

        self.setIcon()
        self.createStatusBar()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def createStatusBar(self):
        self.myStatus = QStatusBar()
        self.myStatus.showMessage("Status Bar Is Ready", 3000)
        self.setStatusBar(self.myStatus)


myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)