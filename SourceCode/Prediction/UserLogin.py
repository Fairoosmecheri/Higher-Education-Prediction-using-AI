
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import xlrd
from Predict import Ui_Predict
from DBConnection import DBConnection
from UserRegister import UserRegister


class UserLogin(object):
    def userLogin(self):
        uname = self.usernameInput.text()
        passwd = self.passwordInput.text()
        database = DBConnection.getConnection()
        cursor = database.cursor()
        database.commit()
        query = "select * from user where uname = %s and password = %s"
        values = (uname,passwd)
        cursor.execute(query,values)
        row = cursor.fetchall()
        if row:
            print("Login success")
            self.user = QtWidgets.QDialog()
            self.ui = Ui_Predict()
            self.ui.setupUi(self.user)
            self.user.show()
        else:
            self.showMessageBox("Information", "Incorrect username or password")

    def showMessageBox(self, title, message):
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setWindowTitle(title)
            msgBox.setText(message)
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.exec_()

    def userRegister(self):
        print("Reg")
        self.userreg = QtWidgets.QDialog()
        self.ui = UserRegister()
        self.ui.setupUi(self.userreg)
        self.userreg.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(544, 388)
        Dialog.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.titleLabel = QtWidgets.QLabel(Dialog)
        self.titleLabel.setGeometry(QtCore.QRect(200, 70, 141, 20))
        self.titleLabel.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.titleLabel.setObjectName("titleLabel")
        self.usernameLabel = QtWidgets.QLabel(Dialog)
        self.usernameLabel.setGeometry(QtCore.QRect(110, 130, 71, 16))
        self.usernameLabel.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.usernameLabel.setObjectName("usernameLabel")
        self.usernameInput = QtWidgets.QLineEdit(Dialog)
        self.usernameInput.setGeometry(QtCore.QRect(110, 150, 251, 31))
        self.usernameInput.setText("")
        self.usernameInput.setObjectName("usernameInput")
        self.passwordLabel = QtWidgets.QLabel(Dialog)
        self.passwordLabel.setGeometry(QtCore.QRect(110, 190, 71, 16))
        self.passwordLabel.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.passwordLabel.setObjectName("passwordLabel")
        self.passwordInput = QtWidgets.QLineEdit(Dialog)
        self.passwordInput.setGeometry(QtCore.QRect(110, 210, 251, 31))
        self.passwordInput.setText("")
        self.passwordInput.setObjectName("passwordInput")
        self.loginBtn = QtWidgets.QPushButton(Dialog)
        self.loginBtn.setGeometry(QtCore.QRect(164, 260, 151, 41))
        self.loginBtn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 75 16pt \"Times New Roman\";\n")
        self.loginBtn.setObjectName("loginBtn")
        self.loginBtn.clicked.connect(self.userLogin)
        self.registerBtn = QtWidgets.QPushButton(Dialog)
        self.registerBtn.setGeometry(QtCore.QRect(164, 300, 151, 41))
        self.registerBtn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "font: 75 16pt \"Times New Roman\";\n")
        self.registerBtn.setObjectName("registerBtn")
        self.registerBtn.clicked.connect(self.userRegister)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "User Login"))
        self.titleLabel.setText(_translate("Dialog", "User Login"))
        self.usernameLabel.setText(_translate("Dialog", "Username"))
        self.passwordLabel.setText(_translate("Dialog", "Password"))
        self.loginBtn.setText(_translate("Dialog", "Login"))
        self.registerBtn.setText(_translate("Dialog", "Register"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = UserLogin()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

