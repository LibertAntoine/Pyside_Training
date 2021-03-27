import sys,os
import PySide2
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QCheckBox
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt

# Allow to find plugins needed for PySide2
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 CheckBox")  # Configure le titre de la fenêtre
        self.setGeometry(300, 300, 400, 100)  # Configure la taille de la fenêtre

        self.setIcon()

        self.createCheckBox()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def createCheckBox(self):
        vbox = QVBoxLayout()

        self.label = QLabel("", self) # Cree un label, qu'on l'on va remplir plus tard en fonction de l'état du bouton

        check = QCheckBox("I like football", self) # Crée un check button avec un label
        check.stateChanged.connect(self.checkBoxChange)
        check.toggle() # Pass le check en coché

        vbox.addWidget(check) # Ajoute la checkbox dans le layout
        vbox.addWidget(self.label)
        
        self.setLayout(vbox) # Place le layout dans la fenêtre

    def checkBoxChange(self, state):
        if state == Qt.Checked:
            self.label.setText("Yes I like football")
        else:
            self.label.setText("No I don't like football")

myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)