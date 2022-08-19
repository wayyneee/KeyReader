import sys,os
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLineEdit,QPushButton,
                             QLabel,QMainWindow,QMessageBox)
from PyQt5.QtGui import QFont
import time
import pickle
from datetime import datetime


#------------TAB--------------#
class login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Login')
        self.setGeometry(600, 300, 250, 210)
        #------------------ enter program key --------------------------#
        self.programkeylabel = QLabel('ProgramKey:', self)
        self.programkeylabel.move(25, 10)
        self.programkeyedit = QLineEdit(self)
        self.programkeyedit.move(115, 10)
        #---------------- enter Account ---------------------------#
        self.Accountlabel = QLabel('Account:', self)
        self.Accountlabel.move(25, 60)
        self.Accountedit = QLineEdit(self)
        self.Accountedit.move(115, 60)
        #---------------- enter prevate key ---------------------------#
        self.PrevateKeylabel = QLabel('PrevateKey:', self)
        self.PrevateKeylabel.move(25, 110)
        self.PrevateKeyedit = QLineEdit(self)
        self.PrevateKeyedit.move(115, 110)
        #------------------- login button -----------------------------#
        self.loginbutton = QPushButton('Login',self)
        self.loginbutton.move(130, 160)
        #------------------- register button --------------------------#
        self.registerbutton = QPushButton('Register',self)
        self.registerbutton.move(20, 160)    

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

class RegisterPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Register')
        self.setGeometry(600, 300, 258, 150)
        #-------------------Set Account ----------------------#
        self.SetAccountlabel = QLabel('Set Account:', self)
        self.SetAccountlabel.move(25, 10)
        self.SetAccountedit = QLineEdit(self)
        self.SetAccountedit.move(130, 10)
        #-------------------Set prevate key ----------------------#
        self.SetPrevateKeylabel = QLabel('Set PrevateKey:', self)
        self.SetPrevateKeylabel.move(25, 60)
        self.SetPrevateKeyedit = QLineEdit(self)
        self.SetPrevateKeyedit.move(130, 60)        
        #-------------------Create account ----------------------#
        self.registerbutton = QPushButton('Create',self)
        self.registerbutton.move(130, 110)
        #--------------------relogin -----------------------------#
        self.relogin = QPushButton('return',self)
        self.relogin.move(10,110)        

class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('RememberKey')
        self.setGeometry(500, 200, 500, 500)

#---------page model-----------#
class messagewindows(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('my window')
        self.setGeometry(50, 50, 200, 150)


#-----------function-----------#
def compare():
    if os.path.isfile(appPath+'/'+Wlogin.Accountedit.text()+'.json')== True:
        with open(appPath+'/'+Wlogin.Accountedit.text()+'.json', 'rb') as fp:
            data = pickle.load(fp)
            fp.close()        
        if data[Wlogin.Accountedit.text()]==Wlogin.PrevateKeyedit.text() and Wlogin.programkeyedit.text()== programkey:
            WHomePage.show()
            Wlogin.hide()
            del data
        else:
            Wlogin.hide()
            WErrorPage.show()
            time.sleep(10)
    else:
        Wlogin.hide()
        WErrorPage.show()
        time.sleep(10)     
   
def RegisterCreate():
    if WRegisterPage.SetPrevateKeyedit.text()!='' and WRegisterPage.SetAccountedit.text()!='':
        if os.path.isfile(appPath+'/'+WRegisterPage.SetAccountedit.text()+'.json')== True:
            QMessageBox.information(None, 'Create Fail', 'Create Fail!, the account has exist.')
        else:
            QMessageBox.information(None, 'Create successfully!', 'Create successfully! Prevate Key will not showing anymore,Please remember it.')
            with open(appPath+'/'+WRegisterPage.SetAccountedit.text()+'.json', 'wb') as fp:
                data ={}
                data[WRegisterPage.SetAccountedit.text()] = WRegisterPage.SetPrevateKeyedit.text()
                pickle.dump(data, fp)
                fp.close()
            Wlogin.show()
            WRegisterPage.hide()
    else:
        QMessageBox.information(None, 'Create Fail', 'Please enter the Account and Prevate Key.')




#----------action-------------#
def start():
    #- login page -#
    Wlogin.show()
    Wlogin.loginbutton.clicked.connect(compare)
    Wlogin.registerbutton.clicked.connect(WRegisterPage.show)
    Wlogin.registerbutton.clicked.connect(Wlogin.hide)
    #- Error Page -#
    WErrorPage.relogin.clicked.connect(Wlogin.show)
    WErrorPage.relogin.clicked.connect(WErrorPage.hide)
    #- Register Page -#
    WRegisterPage.registerbutton.clicked.connect(RegisterCreate)
    WRegisterPage.relogin.clicked.connect(Wlogin.show)
    WRegisterPage.relogin.clicked.connect(WRegisterPage.hide)



#------ Setting -----------------#
appPath = os.getcwd()
programkey = datetime.now().strftime("%Y%m%d")
app = QApplication(sys.argv)
Wlogin = login()
WHomePage = HomePage()
WErrorPage = ErrorPage()
WRegisterPage = RegisterPage()
messagewindow = messagewindows()
start()
sys.exit(app.exec_())