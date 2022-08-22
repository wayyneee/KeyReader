import sys,os
from PyQt5.QtGui import QFont
import time
import pickle
from datetime import datetime
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#------------TAB--------------#
class LoginPage(QMainWindow):
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
        #--------Select Account Label -----------#
        self.SelectAccountlabel = QLabel('Select Account :', self)
        self.SelectAccountlabel.move(30,80)
        #------- AccountText Label ---------#
        self.AccountTextlabel = QLabel('Account :',self)
        self.AccountTextlabel.move(30,160)
        #------- AccountCopy button --------#
        self.AccountCopybutton = QPushButton('Copy',self)
        self.AccountCopybutton.move(30,190)
        #------- KeyText label ---------------------#
        self.KeyTextlabel = QLabel('Key :',self)
        self.KeyTextlabel.move(30,210)
        #------- KeyCopy button---------------------#
        self.KeyCopybutton = QPushButton('Copy',self)
        self.KeyCopybutton.move(30,240)
        #------- NoteText label --------------------#
        self.NoteTextlabel = QLabel('Note :',self)
        self.NoteTextlabel.move(30,260)
        #--------Select Account comboBox---------#
        self.Accountcombobox = QComboBox(self)
        AccountList = self.UpdateAccountList()
        self.Accountcombobox.addItems(AccountList)
        self.Accountcombobox.resize(200,35)
        self.Accountcombobox.move(30, 110)
        self.Accountcombobox.show()
    def Refresh(self):
        #---------Account Label----------------#
        global Wlogin
        global data
        global WHomePage
        self.mylabel = QLabel(Wlogin.Accountedit.text(), self)
        self.mylabel.move(27, 10)
        self.mylabel.setStyleSheet("background-color: lightgreen") 
        self.mylabel.setFont(QFont('Arial', 30))
        self.mylabel.setStyleSheet("border: 1px solid black;")
        self.mylabel.setAlignment(Qt.AlignCenter)
        self.mylabel.resize(450,50)
        self.mylabel.show()
        #--------Select Account comboBox---------#
        self.Accountcombobox = QComboBox(self)
        AccountList = self.UpdateAccountList()
        self.Accountcombobox.addItems(AccountList)
        self.Accountcombobox.resize(200,35)
        self.Accountcombobox.move(30, 110)
        self.Accountcombobox.show()
        #------- ShowAccount Label ---------#
        self.ShowAccountlabel = QLabel(data[WHomePage.Accountcombobox.currentText()]['Account'],self)
        self.ShowAccountlabel.move(100,160)
        self.ShowAccountlabel.show()
        #------- ShowKey label ---------------------#
        self.ShowKeylabel = QLabel(data[WHomePage.Accountcombobox.currentText()]['Key'],self)
        self.ShowKeylabel.move(100,210)
        self.ShowKeylabel.show()
        #------- ShowNoteText label --------------------#
        self.ShowNotelabel = QLabel(data[WHomePage.Accountcombobox.currentText()]['Note'],self)
        self.ShowNotelabel.resize(430,200)
        self.ShowNotelabel.setStyleSheet("background-color: white") 
        self.ShowNotelabel.move(30,290)
        self.ShowNotelabel.setWordWrap(True)
        self.ShowNotelabel.show()
    def clear(self):
        self.ShowAccountlabel.clear()
        self.ShowKeylabel.clear()
        self.ShowNotelabel.clear()

    def UpdateAccountList(self):
        global data
        global Wlogin
        AccountList = []
        for item in data:
            if item != 'ProgramAccount':
                AccountList.append(item)  
        return AccountList

class AddPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('ADD Account')
        self.setGeometry(500, 200, 350, 500)
        #------- Account Name Label ----------#
        self.AccountNamelabel = QLabel('Account Name:', self)
        self.AccountNamelabel.move(27, 10)
        self.AccountNameedit = QLineEdit(self)
        self.AccountNameedit.resize(200,25)
        self.AccountNameedit.move(127,10)
        #------- ADD account Label ----------#
        self.AddAccountlabel = QLabel('Add Account :', self)
        self.AddAccountlabel.move(27, 45)
        self.AddAccountedit = QLineEdit(self)
        self.AddAccountedit.resize(200,25)
        self.AddAccountedit.move(127,45)
        #------- Account Key Label ---------#
        self.AccountKeylabel = QLabel('Set Key:', self)
        self.AccountKeylabel.move(27, 80)
        self.AccountKeyedit = QLineEdit(self)
        self.AccountKeyedit.resize(200,25)
        self.AccountKeyedit.move(127,80)
        #-------Account Note Label ----------------#
        self.AccountNotelabel = QLabel('Note:', self)
        self.AccountNotelabel.move(27, 110)
        self.AccountNoteedit = QPlainTextEdit(self)
        self.AccountNoteedit.resize(300,300)
        self.AccountNoteedit.move(27,150)
        #------Save Account button-------------------------#
        self.SaveAccountButton = QPushButton('Save',self)
        self.SaveAccountButton.move(230,460)
        #------ return button ----------------------#
        self.returnbutton = QPushButton('Return', self)
        self.returnbutton.move(27,460) 
    def clear(self):
        self.AccountNameedit.clear()
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
        for itm in data[item]:
            for i in range(len(data[item][itm])):
                predata = predata + chr((ord(data[item][itm][i])+60))
            data[item][itm]=predata
            predata = ''
    return data


def decode(data):
    for item in data:
        predata =''
        for itm in data[item]:
            for i in range(len(data[item][itm])):
                predata = predata + chr((ord(data[item][itm][i])-60))
            data[item][itm]=predata
            predata = ''
    return data


def RefreshData():
    with open(appPath+'/'+Wlogin.Accountedit.text()+'.json', 'rb') as fp:
        global data
        data = pickle.load(fp)
        data = decode(data)
        fp.close()
def AddAccount(AccountName,Account,Key,Note):
    global data
    data[AccountName]= {'Account':Account,'Key':Key,'Note':Note}

def SaveData():
    with open(appPath+'/'+Wlogin.Accountedit.text()+'.json', 'wb') as fp:
        global data
        data = encode(data)
        pickle.dump(data,fp)
        fp.close()

#----------Action-------------#
def compare():
    if os.path.isfile(appPath+'/'+Wlogin.Accountedit.text()+'.json')== True:
        RefreshData()
        if data['ProgramAccount']['Key']==Wlogin.PrivateKeyedit.text() and Wlogin.programkeyedit.text()== programkey:
            WHomePage.show()
            WHomePage.Refresh()
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
                data ={'ProgramAccount':{'Account':'','Key':'','Note':''}}
                data['ProgramAccount']['Account'] = WRegisterPage.SetAccountedit.text()
                data['ProgramAccount']['Key'] = WRegisterPage.SetPrivateKeyedit.text()
                data['ProgramAccount']['Note'] = WRegisterPage.SetAccountedit.text() + WRegisterPage.SetPrivateKeyedit.text()
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
    WAddPage.hide()
    WHomePage.show()
def AddPageSave():
    global data
    global WHomePage
    AddAccount(WAddPage.AccountNameedit.text(), WAddPage.AddAccountedit.text(), WAddPage.AccountKeyedit.text(), WAddPage.AccountNoteedit.toPlainText())
    SaveData()
    RefreshData()
    WHomePage.Refresh()
    WAddPage.hide()
    WHomePage.show()
def ddd():
    print(1)
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
    WAddPage.SaveAccountButton.clicked.connect(AddPageSave)




#------ Setting -----------------#
data = {}
appPath = os.getcwd()
programkey = datetime.now().strftime("%Y%m%d")
app = QApplication(sys.argv)
Wlogin = LoginPage()
WHomePage = HomePage()
WErrorPage = ErrorPage()
WRegisterPage = RegisterPage()
WAddPage = AddPage()

start()
sys.exit(app.exec_())