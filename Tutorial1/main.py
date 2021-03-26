import sys,os
import PySide2
from PySide2.QtWidgets import QApplication, QWidget


# Allow to find plugins needed for PySide2
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


class Window(QWidget): # Hérite de la class QWidget
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 Test") #Configure le titre de la fenêtre
        self.setGeometry(300, 300, 300, 300) #Configure la taille de la fenêtre


myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)