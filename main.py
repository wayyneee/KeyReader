import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLineEdit,QPushButton,
                             QLabel,QMainWindow)
import sip
from PyQt5.QtGui import QFont
import time


#------------TAB--------------#
class login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('RememberKey')
        self.setGeometry(600, 300, 250, 150)
        #------------------ enter program key --------------------------#
        self.programkeylabel = QLabel('ProgramKey:', self)
        self.programkeylabel.move(25, 10)
        self.programkeyedit = QLineEdit(self)
        self.programkeyedit.move(115, 10)
        #---------------- enter prevate key ---------------------------#
        self.PrevateKeylabel = QLabel('PrevateKey:', self)
        self.PrevateKeylabel.move(25, 60)
        self.PrevateKeyedit = QLineEdit(self)
        self.PrevateKeyedit.move(115, 60)
        #------------------- login button -----------------------------#
        self.loginbutton = QPushButton('Login',self)
        self.loginbutton.move(130, 110)
        #------------------- register button --------------------------#
        self.registerbutton = QPushButton('Register',self)
        self.registerbutton.move(20, 110)    

class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('RememberKey')
        self.setGeometry(600, 300, 250, 150)


class ErrorPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('RememberKey')
        self.setGeometry(600, 300, 250, 150)
        self.Errorlabel = QLabel('Key Error ...:', self)
        self.Errorlabel.move(80, 50)
        self.relogin = QPushButton('retry',self)
        self.relogin.move(75,80)

#-----------function-----------#
def compare():
    if Wlogin.programkeyedit.text()== '0' and Wlogin.PrevateKeyedit.text() == '0':
        WHomePage.show()
        Wlogin.hide()
    else:
        Wlogin.hide()
        WErrorPage.show()
        WErrorPage.relogin.clicked.connect(Wlogin.show)
        WErrorPage.relogin.clicked.connect(WErrorPage.hide)
        time.sleep(10)

#----------action-------------#
def start():
    #- login page -#
    Wlogin.show()
    Wlogin.loginbutton.clicked.connect(compare)
    #- 
#------ Setting -----------------#

app = QApplication(sys.argv)
Wlogin = login()
WHomePage = HomePage()
WErrorPage = ErrorPage()
start()
sys.exit(app.exec_())