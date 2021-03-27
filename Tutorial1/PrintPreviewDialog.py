import sys,os
import PySide2
from PySide2.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit
from PySide2.QtGui import QIcon, QFont
from PySide2.QtPrintSupport import QPrintPreviewDialog, QPrinter

# Allow to find plugins needed for PySide2
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 Print Preview Dialog")  # Configure le titre de la fenêtre
        self.setGeometry(300, 300, 500, 400)  # Configure la taille de la fenêtre

        self.textEdit = QTextEdit(self)
        self.textEdit.setFont((QFont("Sanserif", 13)))
        self.setCentralWidget(self.textEdit) # L'élément rempli la fenêtre

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

        previewAction = QAction(QIcon('icon.png'), "Print Preview", self)
        previewAction.triggered.connect(self.printPreviewDialog)
        viewMenu.addAction(previewAction)



    def exitApp(self):
        self.close()

    def printPreviewDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)

        previewDialog.paintRequested.connect(self.printPreview) # Rempli le dialog
        previewDialog.exec_() # Lance le dialog

    def printPreview(self, printer):
        self.textEdit.print_(printer)


myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)