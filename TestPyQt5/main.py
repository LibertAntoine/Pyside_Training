import sys
from PyQt5.QtWidgets import QApplication, QWidget

class Window(QWidget): # Hérite de la class QWidget
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Window") #Configure le titre de la fenêtre

        # Setup Window
        self.setGeometry(300, 300, 600, 300) #Configure la taille de la fenêtre
        self.setMinimumHeight(100)
        self.setMinimumWidth(250)

        self.setMaximumHeight(200)
        self.setMaximumWidth(800)

myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)