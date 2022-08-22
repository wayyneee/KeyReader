import sys,os
from PyQt5.QtGui import QFont
import time
import pickle
from datetime import datetime
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

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
        #---------------- enter private key ---------------------------#
        self.PrivateKeylabel = QLabel('PrivateKey:', self)
        self.PrivateKeylabel.move(25, 110)
        self.PrivateKeyedit = QLineEdit(self)
        self.PrivateKeyedit.move(115, 110)
        #------------------- login button -----------------------------#
        self.loginbutton = QPushButton('Login',self)
        self.loginbutton.move(130, 160)
        #------------------- register button --------------------------#
        self.registerbutton = QPushButton('Register',self)
        self.registerbutton.move(20, 160)
    def clear(self):
        self.programkeyedit.clear()
        self.Accountedit.clear()
        self.PrivateKeyedit.clear()   

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
        #-------------------Set private key ----------------------#
        self.SetPrivateKeylabel = QLabel('Set PrivateKey:', self)
        self.SetPrivateKeylabel.move(25, 60)
        self.SetPrivateKeyedit = QLineEdit(self)
        self.SetPrivateKeyedit.move(130, 60)        
        #-------------------Create account ----------------------#
        self.registerbutton = QPushButton('Create',self)
        self.registerbutton.move(130, 110)
        #--------------------relogin -----------------------------#
        self.relogin = QPushButton('return',self)
        self.relogin.move(10,110)        
    def clear(self):
        self.SetAccountedit.clear()
        self.SetPrivateKeyedit.clear()

class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('RememberKey')
        self.setGeometry(500, 200, 500, 500)
        #---------add button------------------#
        self.ADDbutton = QPushButton('ADD',self)
        self.ADDbutton.move(280,80)
        #---------Delete button---------------#
        self.Deletebutton = QPushButton('Delete',self)
        self.Deletebutton.move(380,80)
        #--------Search button --------------#
        self.Searchbutton = QPushButton('Search',self)
        self.Searchbutton.move(280,110)  
        #------- Ｓignout button -------------#  
        self.Signoutbutton = QPushButton('Sign out',self)
        self.Signoutbutton.move(380,110)  
    def refresh(self):
        #---------Account Label----------------#
        global Wlogin
        global data
        self.mylabel = QLabel(Wlogin.Accountedit.text(), self)
        self.mylabel.move(27, 10)
        self.mylabel.setStyleSheet("background-color: lightgreen") 
        self.mylabel.setFont(QFont('Arial', 30))
        self.mylabel.setStyleSheet("border: 1px solid black;")
        self.mylabel.setAlignment(Qt.AlignCenter)
        self.mylabel.resize(450,50)
        self.mylabel.show()
        #--------Select Account Label -----------#
        self.SelectAccountlabel = QLabel('Select Account :', self)
        self.SelectAccountlabel.move(30,80)
        self.SelectAccountlabel.show()
        #--------Select Account comboBox---------#
        self.Accountcombobox = QComboBox(self)
        AccountList = self.UpdateAccountList()
        self.Accountcombobox.addItems(AccountList)
        self.Accountcombobox.setCurrentIndex(0)
        self.Accountcombobox.resize(200,35)
        self.Accountcombobox.move(30, 110)
        self.Accountcombobox.show()
        # self.Accountcombobox.currentIndexChanged.connect(self.onComboBoxChanged) 
    def UpdateAccountList(self):
        global data
        global Wlogin
        AccountList = []
        for item in data:
            if item != Wlogin.Accountedit.text():
                AccountList.append(item)  
        return AccountList

class AddPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('ADD Account')
        self.setGeometry(500, 200, 350, 500)
        #------- ADD account Label ----------#
        self.AddAccountlabel = QLabel('Add Account :', self)
        self.AddAccountlabel.move(27, 10)
        self.AddAccountedit = QLineEdit(self)
        self.AddAccountedit.resize(200,30)
        self.AddAccountedit.move(127,10)
        #------- Account Key Label ---------#
        self.AccountKeylabel = QLabel('Set Key:', self)
        self.AccountKeylabel.move(27, 60)
        self.AccountKeyedit = QLineEdit(self)
        self.AccountKeyedit.resize(200,30)
        self.AccountKeyedit.move(127,60)
        #-------Account Note Label ----------------#
        self.AccountNotelabel = QLabel('Note:', self)
        self.AccountNotelabel.move(27, 110)
        self.AccountNoteedit = QTextEdit(self)
        self.AccountNoteedit.resize(300,300)
        self.AccountNoteedit.move(27,150)
        #------Save Account button-------------------------#
        self.SaveAccountButton = QPushButton('Save',self)
        self.SaveAccountButton.move(230,460)
        #------ return button ----------------------#
        self.returnbutton = QPushButton('Return', self)
        self.returnbutton.move(27,460) 
    def clear(self):
        self.AddAccountedit.clear()
        self.AccountKeyedit.clear()
        self.AccountNoteedit.clear()

#---------page model-----------#
class messagewindows(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('my window')
        self.setGeometry(50, 50, 200, 150)


#-----------function-----------#
def encode(data):
    for item in data:
        predata =''
        for i in range(len(data[item])):
            predata = predata + chr((ord(data[item][i])+60))
        data[item] = predata
    return data

def decode(data):
    for item in data:
        predata =''
        for i in range(len(data[item])):
            predata = predata + chr((ord(data[item][i])-60))
        data[item] = predata
    return data

def RefreshData():
    with open(appPath+'/'+Wlogin.Accountedit.text()+'.json', 'rb') as fp:
        global data
        data = pickle.load(fp)
        data = decode(data)
        fp.close()


#----------Action-------------#
def compare():
    if os.path.isfile(appPath+'/'+Wlogin.Accountedit.text()+'.json')== True:
        RefreshData()
        if data[Wlogin.Accountedit.text()]==Wlogin.PrivateKeyedit.text() and Wlogin.programkeyedit.text()== programkey:
            WHomePage.show()
            WHomePage.refresh()
            Wlogin.hide()
        else:
            Wlogin.hide()
            WErrorPage.show()
            time.sleep(10)
    else:
        Wlogin.hide()
        WErrorPage.show()
        time.sleep(10)     
def ErrorToLogin():
    Wlogin.clear()
    Wlogin.show()
    WErrorPage.hide()   
def RegisterCreate():
    if WRegisterPage.SetPrivateKeyedit.text()!='' and WRegisterPage.SetAccountedit.text()!='':
        if os.path.isfile(appPath+'/'+WRegisterPage.SetAccountedit.text()+'.json')== True:
            QMessageBox.information(None, 'Create Fail', 'Create Fail!\nThe account has exist.')
        else:
            QMessageBox.information(None, 'Create successfully!', 'Create successfully!\nPrivate Key will not showing anymore,Please remember it.')
            with open(appPath+'/'+WRegisterPage.SetAccountedit.text()+'.json', 'wb') as fp:
                data ={}
                data[WRegisterPage.SetAccountedit.text()] = WRegisterPage.SetPrivateKeyedit.text()
                data = encode(data)
                pickle.dump(data, fp)
                fp.close()
            Wlogin.clear()
            Wlogin.show()
            WRegisterPage.hide()
    else:
        QMessageBox.information(None, 'Create Fail', 'Please enter the Account and Private Key.')  
def ToRegisterPage():
    WRegisterPage.clear()
    WRegisterPage.show()
    Wlogin.hide()
def RegisterToLogin():
    Wlogin.clear()
    Wlogin.show()
    WRegisterPage.hide()
def HomeToAdd():
    WAddPage.clear()
    WAddPage.show()
    WHomePage.hide()
def AddToHome():
    RefreshData()
    WAddPage.hide()
    WHomePage.show()
#----------listener-------------#
def start():
    #- login page -#
    Wlogin.show()
    Wlogin.loginbutton.clicked.connect(compare)
    Wlogin.registerbutton.clicked.connect(ToRegisterPage)
    #- Error Page -#
    WErrorPage.relogin.clicked.connect(ErrorToLogin)
    #- Register Page -#
    WRegisterPage.registerbutton.clicked.connect(RegisterCreate)
    WRegisterPage.relogin.clicked.connect(RegisterToLogin)
    #- Home Page -#
    WHomePage.ADDbutton.clicked.connect(HomeToAdd)
    #- Add Page -#
    WAddPage.returnbutton.clicked.connect(AddToHome)




#------ Setting -----------------#
data = {}
appPath = os.getcwd()
programkey = datetime.now().strftime("%Y%m%d")
app = QApplication(sys.argv)
Wlogin = login()
WHomePage = HomePage()
WErrorPage = ErrorPage()
WRegisterPage = RegisterPage()
WAddPage = AddPage()

start()
sys.exit(app.exec_())