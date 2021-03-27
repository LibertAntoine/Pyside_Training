import sys,os
import PySide2
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PySide2.QtGui import QIcon, QPixmap, QFont

# Allow to find plugins needed for PySide2
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 PushButton")  # Configure le titre de la fenêtre
        self.setGeometry(300, 300, 500, 400)  # Configure la taille de la fenêtre

        self.setIcon()
        self.setButton()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def setButton(self):
        btn1 = QPushButton("Quit", self) #Create new button
        btn1.move(50, 100)

        btn1.clicked.connect(self.quitApp) # Connect un slot avec le signal de clique sur le bouton

    def quitApp(self): # Défini un slot qu'on voudra activer pour quitter l'application
        userInfo = QMessageBox.question(self, "Confirmation", "Do you want to quit the application ?", QMessageBox.Yes | QMessageBox.No)

        if userInfo == QMessageBox.Yes:
            myApp.quit()

        elif userInfo == QMessageBox.No:
            pass



myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)