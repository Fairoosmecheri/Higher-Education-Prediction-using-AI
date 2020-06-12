
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from DBConnection import DBConnection

class UserRegister(object):
    def userRegister(self):
        uname = self.usernameInput.text()
        passwd = self.passwordInput.text()
        database = DBConnection.getConnection()
        cursor = database.cursor()
        database.commit()
        query = "insert into user (uname,  password) values (%s,%s)"
        values = (uname, passwd)
        cursor.execute(query, values)
        database.commit()
        print("Register Successfully")
        self.showMessageBox("Information", "User Registered Successfully")

    def showMessageBox(self, title, message):
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setWindowTitle(title)
            msgBox.setText(message)
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.exec_()

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
        Dialog.setWindowTitle(_translate("Dialog", "User Register"))
        self.titleLabel.setText(_translate("Dialog", "User Register"))
        self.usernameLabel.setText(_translate("Dialog", "Username"))
        self.passwordLabel.setText(_translate("Dialog", "Password"))
        self.registerBtn.setText(_translate("Dialog", "Register"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = UserRegister()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())