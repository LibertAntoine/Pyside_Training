import sys,os
import PySide2
from PySide2.QtWidgets import QApplication, QMainWindow, QAction
from PySide2.QtGui import QIcon

# Allow to find plugins needed for PySide2
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 Notepad Application")  # Configure le titre de la fenêtre
        self.setGeometry(300, 300, 500, 400)  # Configure la taille de la fenêtre

        self.setIcon()
        self.create_menu()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def create_menu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        viewMenu = mainMenu.addMenu('View')
        editMenu = mainMenu.addMenu('Edit')
        fontMenu = mainMenu.addMenu('Font')
        helpMenu = mainMenu.addMenu('Help')

        openAction = QAction(QIcon('icon.png'), "Open", self)
        openAction.setShortcut('Ctrl+O')

        saveAction = QAction(QIcon('icon.png'), "Save", self)
        saveAction.setShortcut('Ctrl+S')

        exitAction = QAction(QIcon('icon.png'), "Exit", self)
        exitAction.setShortcut('Ctrl+X') # Configure un raccourci pour activer la fonction (marche automatiquement)

        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(exitAction)

        exitAction.triggered.connect(self.exitApp)


    def exitApp(self):
        self.close()

myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)