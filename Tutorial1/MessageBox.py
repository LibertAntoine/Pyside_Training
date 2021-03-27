import sys,os
import PySide2
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QVBoxLayout
from PySide2.QtGui import QIcon

# Allow to find plugins needed for PySide2
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 Message box")  # Configure le titre de la fenêtre
        self.setGeometry(300, 300, 500, 400)  # Configure la taille de la fenêtre

        self.setIcon()
        self.createButton()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def createButton(self):
        vbox = QVBoxLayout()

        btn1 = QPushButton("Open About Message Box")
        btn1.clicked.connect(self.showAbout)
        btn2 = QPushButton("Open Warning Message Box")
        btn2.clicked.connect(self.showWarning)
        btn3 = QPushButton("Open Information Message Box")
        btn3.clicked.connect(self.showInformation)

        self.label = QLabel()

        btn4 = QPushButton("Open Question Message Box")
        btn4.clicked.connect(self.showQuestion)

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def showAbout(self):
        QMessageBox.about(self, "AboutBox", "This is about application")

    def showWarning(self):
        QMessageBox.warning(self, "Warning", "This is warning application")

    def showInformation(self):
        QMessageBox.information(self, "Information", "This is information application")

    def showQuestion(self):
        reply = QMessageBox.question(self, "Question", "Do you like PySide2", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.label.setText("I like PySide2.")
        elif reply == QMessageBox.No:
            self.label.setText("I don't like PySide2.")

myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)