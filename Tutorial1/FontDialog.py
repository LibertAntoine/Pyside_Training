import sys,os
import PySide2
from PySide2.QtWidgets import QApplication, QMainWindow, QAction, QFontDialog, QTextEdit, QFileDialog
from PySide2.QtGui import QIcon, QFont
from PySide2.QtPrintSupport import QPrintPreviewDialog, QPrinter, QPrintDialog
from PySide2.QtCore import QFileInfo

# Allow to find plugins needed for PySide2
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 Font Dialog")  # Configure le titre de la fenêtre
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

        printAction = QAction(QIcon('icon.png'), "Print", self)
        printAction.setShortcut('Ctrl+P')
        printAction.triggered.connect(self.printDialog)

        pdfAction = QAction(QIcon('icon.png'), "Export PDF", self)
        pdfAction.triggered.connect(self.pdfExport)

        viewMenu.addAction(previewAction)
        viewMenu.addAction(printAction)
        viewMenu.addAction(pdfAction)

        fontAction = QAction(QIcon('icon.png'), "Font", self)
        fontAction.triggered.connect(self.fontDialog)

        fontMenu.addAction(fontAction)


    def exitApp(self):
        self.close()

    def printPreviewDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)

        previewDialog.paintRequested.connect(self.printPreview) # Rempli le dialog
        previewDialog.exec_() # Lance le dialog

    def printPreview(self, printer):
        self.textEdit.print_(printer)

    def printDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.textEdit.print_(printer)

    def pdfExport(self):
        fn, _ = QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF files(.pdf); All files")
        if fn != '':
            if QFileInfo(fn).suffix() == "": fn += '.pdf'
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.textEdit.document().print_(printer)

    def fontDialog(self):
        (ok, font) = QFontDialog.getFont()

        if ok:
            self.textEdit.setFont(font)



myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)