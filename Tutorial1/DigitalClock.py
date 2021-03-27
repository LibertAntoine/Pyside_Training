import sys,os
import PySide2
from PySide2.QtWidgets import QApplication, QWidget, QLCDNumber
from PySide2.QtCore import QTime, QTimer, SIGNAL
from PySide2.QtGui import QIcon

# Allow to find plugins needed for PySide2
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class DigitalClock(QLCDNumber):
    def __init__(self, parent = None):
        super(DigitalClock, self).__init__(parent)


        self.setSegmentStyle(QLCDNumber.Filled)

        timer = QTimer(self) # Crée un timer
        self.connect(timer, SIGNAL('timeout()'), self.showTime) # Ajouter un signal, quand le timer arrive à 0, on fait l'action
        timer.start(1000) # On lance le timer à 1000 ms, l'action s'effectuera toutes les secondes.
        self.showTime()


        self.setWindowTitle("Pyside2 Digital Clock")  # Configure le titre de la fenêtre
        self.resize(300, 200)

        self.setIcon()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)


    def showTime(self):
        time = QTime.currentTime() # Récupère le temps
        text = time.toString('hh:mm') # Formate l'affichage du temps
        if(time.second() % 2) == 0: # Enlève les deux points entre les minutes et heures une seconde sur deux.
            text = text[:2] + ' ' + text[3:]

        self.display(text) # Affiche le texte

myApp = QApplication(sys.argv)
window = DigitalClock()
window.show()

myApp.exec_()
sys.exit(0)


