import sys,os
import PySide2
from PySide2.QtWidgets import QApplication, QMainWindow, QProgressBar, QStatusBar, QLabel
from PySide2.QtGui import QIcon, QPixmap

# Allow to find plugins needed for PySide2
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 Progress Bar")  # Configure le titre de la fenêtre
        self.setGeometry(300, 300, 500, 400)  # Configure la taille de la fenêtre

        self.setIcon()

        # Create Progress Bar
        self.statusLabel = QLabel("Showing Progress")
        self.progressBar = QProgressBar()
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)

        self.createStatusBar()


    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def createStatusBar(self):
        self.statusBar = QStatusBar()
        self.progressBar.setValue(10)
        self.statusBar.addWidget(self.statusLabel, 1)
        self.statusBar.addWidget(self.progressBar, 2)
        self.setStatusBar(self.statusBar)



myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)