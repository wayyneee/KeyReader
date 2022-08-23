from ast import keyword
import sys,os
from turtle import goto
from PyQt5.QtGui import QFont
import time
import pickle
from datetime import datetime
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyperclip as pc

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
        self.keyword = ''
        self.setWindowTitle('RememberKey')
        self.setGeometry(500, 200, 500, 500)
        #---------add button------------------#
        self.ADDbutton = QPushButton('Add',self)
        self.ADDbutton.move(380,80)
        #---------Delete button---------------#
        self.Deletebutton = QPushButton('Delete',self)
        self.Deletebutton.move(380,110)
        #--------Search button --------------#
        self.Searchbutton = QPushButton('Search',self)
        self.Searchbutton.move(130,65)
        #------- RefreshAccountlist button --------------#
        self.RefreshAccountlistbutton = QPushButton('Refresh',self)
        self.RefreshAccountlistbutton.move(130,95)
        #------- Ｓignout button -------------#  
        self.Signoutbutton = QPushButton('Sign out',self)
        self.Signoutbutton.move(380,140)
        #--------Search edit-------------------#
        self.Searchedit = QLineEdit(self)
        self.Searchedit.move(30,75)
        #--------Select Account Label -----------#
        self.SelectAccountlabel = QLabel('Select Account :', self)
        self.SelectAccountlabel.move(30,110)
        #------- AccountName Label ---------#
        self.AccountNamelabel = QLabel('Account Name :',self)
        self.AccountNamelabel.move(30,170)
        #------- AccountText Label ---------#
        self.AccountTextlabel = QLabel('Account :',self)
        self.AccountTextlabel.move(30,200)
        #------- AccountCopy button --------#
        self.AccountCopybutton = QPushButton('Copy',self)
        self.AccountCopybutton.move(300,200)
        #------- KeyText label ---------------------#
        self.KeyTextlabel = QLabel('Key :',self)
        self.KeyTextlabel.move(30,230)
        #------- KeyCopy button---------------------#
        self.KeyCopybutton = QPushButton('Copy',self)
        self.KeyCopybutton.move(300,230)
        #------- NoteText label --------------------#
        self.NoteTextlabel = QLabel('Note :',self)
        self.NoteTextlabel.move(30,260)
        #--------Select Account comboBox button---------#
        self.Accountcomboxbutton = QPushButton('select',self)
        self.Accountcomboxbutton.move(220,142)
    def Refresh(self):
        global Wlogin
        global data
        global WHomePage
        #---------Account Label----------------#
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
        self.AccountList = self.UpdateAccountList()
        self.Accountcombobox.addItems(self.AccountList)
        self.Accountcombobox.resize(200,35)
        self.Accountcombobox.move(30, 140)
        self.Accountcombobox.show()
    def refreshtable(self):
        #------- ShowAccount Name Label------#
        self.ShowAccountNamelabel = QLabel('',self)
        self.ShowAccountNamelabel.move(130,175)
        self.ShowAccountNamelabel.resize(200,20)
        self.ShowAccountNamelabel.show()
        #------- ShowAccount Label ---------#
        self.ShowAccountlabel = QLabel('',self)
        self.ShowAccountlabel.move(100,205)
        self.ShowAccountlabel.resize(200,20)
        self.ShowAccountlabel.setStyleSheet("background-color: white") 
        self.ShowAccountlabel.show()        
        #------- ShowKey label ---------------------#
        self.ShowKeylabel = QLabel('',self)
        self.ShowKeylabel.move(100,235)
        self.ShowKeylabel.resize(200,20)
        self.ShowKeylabel.setStyleSheet("background-color: white") 
        self.ShowKeylabel.show()
        #------- ShowNoteText label --------------------#
        self.ShowNotelabel = QLabel('',self)
        self.ShowNotelabel.resize(430,200)
        self.ShowNotelabel.setStyleSheet("background-color: white") 
        self.ShowNotelabel.move(30,290)
        self.ShowNotelabel.setWordWrap(True)
        self.ShowNotelabel.show()      
        if self.AccountList!=[]:
            self.ShowAccountNamelabel.setText(WHomePage.Accountcombobox.currentText())
            self.ShowAccountlabel.setText(data[WHomePage.Accountcombobox.currentText()]['Account'])
            self.ShowKeylabel.setText(data[WHomePage.Accountcombobox.currentText()]['Key'])
            self.ShowNotelabel.setText(data[WHomePage.Accountcombobox.currentText()]['Note'])
    def clear(self):
        self.ShowAccountNamelabel.clear()
        self.ShowAccountlabel.clear()
        self.ShowKeylabel.clear()
        self.ShowNotelabel.clear()
    def clearmylabel(self):
        self.Accountcombobox.clear()
        self.mylabel.clear()
    def clearSelectbox(self):
        self.Accountcombobox.clear()
    def UpdateAccountList(self):
        global data
        global Wlogin
        AccountList = []
        if self.keyword =='':
            for item in data:
                if item != 'ProgramAccount':
                    AccountList.append(item)  
            return AccountList
        else :
            for item in data:
                if item !='ProgramAccount' and self.keyword in item :
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

class DeletePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        global WHomePage
        self.setWindowTitle('Delete Page')
        self.setGeometry(550, 250, 300, 200)
        self.OKbutton = QPushButton('OK',self)
        self.OKbutton.move(40,160) 
        self.returnbutton = QPushButton('return',self)
        self.returnbutton.move(140,160)       
    def refreshDeletePage(self):
        stri = 'If you want to delete account 「 '+ WHomePage.Accountcombobox.currentText()+' 」, please enter theaccount name again.'
        self.deleteAccountlabel = QLabel(stri,self)
        self.deleteAccountlabel.move(15,30)
        self.deleteAccountlabel.resize(260,50)
        self.deleteAccountlabel.setWordWrap(True)
        self.deleteedit = QLineEdit(self)
        self.deleteedit.move(15,90)
        self.deleteedit.resize(260,30)
    def clear(self):
        self.deleteAccountlabel.clear()
        self.deleteedit.clear()
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
    Wlogin
    with open(appPath+'/'+Wlogin.Accountedit.text()+'.json', 'rb') as fp:
        global data
        data = pickle.load(fp)
        data = decode(data)
        fp.close()
def AddAccount(AccountName,Account,Key,Note):
    global data
    if AccountName != '':
        data[AccountName]= {'Account':Account,'Key':Key,'Note':Note}
    else:
        QMessageBox.information(None,'create fail','Please enter the Account Name')
def SaveData():
    Wlogin
    with open(appPath+'/'+Wlogin.Accountedit.text()+'.json', 'wb') as fp:
        global data
        data = encode(data)
        pickle.dump(data,fp)
        fp.close()

#----------Action-------------#
def compare():
    if os.path.isfile(appPath+'/'+Wlogin.Accountedit.text()+'.json')== True:
        global data
        global WHomePage
        RefreshData()
        if data['ProgramAccount']['Key']==Wlogin.PrivateKeyedit.text() and Wlogin.programkeyedit.text()== programkey:
            WHomePage.Refresh()
            WHomePage.refreshtable()
            WHomePage.show()
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
    global WRegisterPage
    WRegisterPage.clear()
    WRegisterPage.show()
    Wlogin.hide()
def RegisterToLogin():
    global Wlogin
    Wlogin.clear()
    Wlogin.show()
    WRegisterPage.hide()
def HomeToAdd():
    global WAddPage
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
    WHomePage.clearmylabel()
    WHomePage.clearSelectbox()
    WHomePage.Refresh()
    WAddPage.hide()
    WHomePage.show()
def SelectAccount():
    global WHomePage
    WHomePage.clear()
    WHomePage.refreshtable()
def DeleteAccount():
    global WHomePage
    if WHomePage.AccountList!=[]:
        WHomePage.hide()
        WDeletePage.refreshDeletePage()
        WDeletePage.show()
    else:
        QMessageBox.information(None,'Delete fail','Nothing to delete.')
def DeleteToHome():
    WDeletePage.hide()
    WDeletePage.clear()
    WHomePage.show()
def CheckToDelete():
    global WHomePage
    global data
    if WDeletePage.deleteedit.text()==WHomePage.Accountcombobox.currentText():
        QMessageBox.information(None,'delete','Delete Successfully!')
        del data[WHomePage.Accountcombobox.currentText()]
        SaveData()
        RefreshData()
        WHomePage.clearmylabel()
        WHomePage.clearSelectbox()
        WHomePage.Refresh()
        WHomePage.clear()
        WHomePage.refreshtable()
        WDeletePage.clear()
        WDeletePage.hide()
        WHomePage.show()
    else:
        QMessageBox.information(None,'delete','Delete Fail,Please check the Account name.')
def Signout():
    global Wlogin,WHomePage
    WHomePage.hide()
    WHomePage.clearSelectbox()
    WHomePage.clearmylabel()
    WHomePage.clear()
    Wlogin.clear()
    Wlogin.show()
def CopyAccount():
    pc.copy(data[WHomePage.Accountcombobox.currentText()]['Account'])
def CopyKey():
    pc.copy(data[WHomePage.Accountcombobox.currentText()]['Key'])
def SearchAccount():
    global WHomePage
    WHomePage.keyword =  WHomePage.Searchedit.text()
    WHomePage.clearSelectbox()
    WHomePage.clearmylabel()
    WHomePage.Refresh()

def RefreshAccountList():
    global WHomePage
    WHomePage.keyword = ''
    WHomePage.clearSelectbox()
    WHomePage.clearmylabel()
    WHomePage.Refresh()
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
    WHomePage.Accountcomboxbutton.clicked.connect(SelectAccount)
    WHomePage.Deletebutton.clicked.connect(DeleteAccount)
    WHomePage.Signoutbutton.clicked.connect(Signout)
    WHomePage.AccountCopybutton.clicked.connect(CopyAccount)
    WHomePage.KeyCopybutton.clicked.connect(CopyKey)
    WHomePage.Searchbutton.clicked.connect(SearchAccount)
    WHomePage.RefreshAccountlistbutton.clicked.connect(RefreshAccountList)
    #- Add Page -#
    WAddPage.returnbutton.clicked.connect(AddToHome)
    WAddPage.SaveAccountButton.clicked.connect(AddPageSave)
    #-DeletePage-#
    WDeletePage.returnbutton.clicked.connect(DeleteToHome)
    WDeletePage.OKbutton.clicked.connect(CheckToDelete)
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
WDeletePage = DeletePage()

start()
sys.exit(app.exec_())