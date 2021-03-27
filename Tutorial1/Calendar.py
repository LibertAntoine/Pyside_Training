import sys,os
import PySide2
from PySide2.QtWidgets import QApplication, QWidget, QCalendarWidget, QVBoxLayout
from PySide2.QtGui import QIcon

# Allow to find plugins needed for PySide2
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 Calendar")  # Configure le titre de la fenêtre
        self.setGeometry(300, 300, 500, 400)  # Configure la taille de la fenêtre

        self.setIcon()
        self.createCalendar()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def createCalendar(self):
        vbox = QVBoxLayout()

        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)

        vbox.addWidget(self.calendar) # Met le calendirer dans le layout
        self.setLayout(vbox) #Associe le layout à la fenêtre


myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)