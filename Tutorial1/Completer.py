import sys,os
import PySide2
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QCompleter, QLineEdit
from PySide2.QtGui import QIcon

# Allow to find plugins needed for PySide2
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 COmpleter")  # Configure le titre de la fenêtre
        self.setGeometry(300, 300, 300, 250)  # Configure la taille de la fenêtre

        self.setIcon()
        self.createCompleter()


    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def createCompleter(self):
        vbox = QVBoxLayout()
        names = ["Antoine", "Lucie", "Justine", "Dorian", "Lucas", "Fabrice"]

        completer = QCompleter(names) # Crée un completeur qui quand on écrit propose en fonction des champs données

        self.lineEdit = QLineEdit() # Créer un input dans lequel on peut écrire
        self.lineEdit.setCompleter(completer)

        vbox.addWidget(self.lineEdit)

        self.setLayout(vbox)

myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)