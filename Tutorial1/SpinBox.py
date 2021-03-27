import sys,os
import PySide2
from PySide2.QtWidgets import QApplication, QWidget, QDoubleSpinBox, QSpinBox, QLabel, QVBoxLayout
from PySide2.QtGui import QIcon

# Allow to find plugins needed for PySide2
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 SpinBox")  # Configure le titre de la fenêtre
        self.setGeometry(300, 300, 500, 400)  # Configure la taille de la fenêtre

        self.setIcon()
        self.spinBox()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def spinBox(self):
        vbox = QVBoxLayout()

        self.label = QLabel()

        self.spinbox = QDoubleSpinBox()
        self.spinbox.setMinimum(10)
        self.spinbox.setMaximum(100)
        self.spinbox.valueChanged.connect(self.spinValue)

        vbox.addWidget(self.label)
        vbox.addWidget(self.spinbox)

        self.setLayout(vbox)

    def spinValue(self):
        self.label.setText("Current Value is : " + str(self.spinbox.value()))


myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)