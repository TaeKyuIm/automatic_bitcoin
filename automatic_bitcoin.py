import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Mysignal(QObject):
    signal1 = pyqtSignal()

    def run(self):
        self.signal1.emit()

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        mysignal = Mysignal()
        mysignal.signal1.connect(self.signal1_emmitted)
        mysignal.run()

    @pyqtSlot()
    def signal1_emmitted(self):
        print("signal1 emmitted")

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()