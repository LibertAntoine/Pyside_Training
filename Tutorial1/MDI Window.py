import sys,os
import PySide2
from PySide2.QtWidgets import QApplication, QTextEdit, QAction,QMainWindow, QMdiSubWindow, QMdiArea
from PySide2.QtGui import QIcon

# Allow to find plugins needed for PySide2
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class Window(QMainWindow):

    count = 0

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Pyside2 MDI Window")
        self.setGeometry(100,100, 900, 500)
        self.setWindowIcon(QIcon('icon.png'))

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        menu_bar = self.menuBar()

        file = menu_bar.addMenu("File")
        file.addAction("New")
        file.addAction("Cascade")
        file.addAction("Tiled")

        file.triggered[QAction].connect(self.windowTriggered)

    def windowTriggered(self, p):
        if p.text() == "New":
            Window.count = Window.count + 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("Sub Window " + str(Window.count))
            self.mdi.addSubWindow(sub)
            sub.show()

        if p.text() == "Cascade":
            self.mdi.cascadeSubWindows()

        if p.text() == "Tiled":
            self.mdi.tileSubWindows()


myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)