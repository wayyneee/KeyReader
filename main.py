import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLineEdit,QPushButton,
                             QLabel,QMainWindow)
import sip
from PyQt5.QtGui import QFont



class login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('RememberKey')
        self.setGeometry(600, 300, 250, 150)
        ###############enter program key###########################
        self.programkeylabel = QLabel('ProgramKey:', self)
        self.programkeylabel.move(10, 10)
        self.programkeyedit = QLineEdit(self)
        self.programkeyedit.move(100, 10)
        ################enter prevate key##########################
        self.programkeylabel = QLabel('PrevateKey:', self)
        self.programkeylabel.move(10, 60)
        self.programkeyedit = QLineEdit(self)
        self.programkeyedit.move(100, 60)



# class ADDWindows(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#     def initUI(self):
#         self.setWindowTitle('RememberKey')
#         self.setGeometry(50, 50, 500, 500)
#         self.Home = QPushButton('Home', self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    Wlogin = login()
    Wlogin.show()
    sys.exit(app.exec_())