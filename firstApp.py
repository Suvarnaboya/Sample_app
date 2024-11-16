


from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
import sys
from firstUI import *

class Naveen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.submitB.clicked.connect(self.wish)
    def wish(self):
        name = self.ui.lineEdit.text()
        self.ui.label_3.setText("Hai {}".format(name))



if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Naveen()
    w.show()
    sys.exit(app.exec_())

