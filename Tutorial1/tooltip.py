import sys,os
import PySide2
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QToolTip
from PySide2.QtGui import QIcon, QPixmap, QFont

# Allow to find plugins needed for PySide2
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 Icon")  # Configure le titre de la fenêtre
        self.setGeometry(300, 300, 500, 400)  # Configure la taille de la fenêtre

        QToolTip.setFont(QFont("Decorative", 10, QFont.Bold))
        self.setToolTip("Our Main Window")

        self.setIcon()
        self.setIconModes()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)


    def setIconModes(self):
        icon1 = QIcon("icon.png")
        label1 = QLabel('Sample', self)
        pixmap1 = icon1.pixmap(100, 100, QIcon.Active, QIcon.On)
        label1.setPixmap(pixmap1)
        label1.setToolTip("Active Icon")

        icon2 = QIcon("icon.png")
        label2 = QLabel('Sample', self)
        pixmap2 = icon2.pixmap(100, 100, QIcon.Disabled, QIcon.Off)
        label2.setPixmap(pixmap2)
        label2.move(100, 0)
        label2.setToolTip("Disabled Icon")

        icon3 = QIcon("icon.png")
        label3 = QLabel('Sample', self)
        pixmap3 = icon3.pixmap(100, 100, QIcon.Selected, QIcon.On)
        label3.setPixmap(pixmap3)
        label3.move(200, 0)
        label3.setToolTip("Selected Icon")


myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)