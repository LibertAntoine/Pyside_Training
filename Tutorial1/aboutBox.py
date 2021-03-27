import sys,os
import PySide2
from PySide2.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton
from PySide2.QtGui import QIcon, QPixmap

# Allow to find plugins needed for PySide2
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 About Box Creation")  # Configure le titre de la fenêtre
        self.setGeometry(300, 300, 500, 400)  # Configure la taille de la fenêtre

        self.setIcon()
        self.pushButton()


    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def pushButton(self):
        self.aboutButton = QPushButton("Open About Box", self)
        self.aboutButton.move(50, 100)
        self.aboutButton.clicked.connect(self.aboutBox)

    def aboutBox(self):
        QMessageBox.about(self.aboutButton, "About PySide2", "Pyside2 is a cross Platform GUI Library for Python Programming.")




myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)