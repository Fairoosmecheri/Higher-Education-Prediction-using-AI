
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from DBConnection import DBConnection

class UserRegister(object):
    def userRegister(self):
        uname = self.usernameInput.text()
        passwd = self.passwordInput.text()
        if (uname == "" or passwd == ""):
            self.showMessageBox("Information", "Please fill all fields.")
        else :
            database = DBConnection.getConnection()
            cursor = database.cursor()
            database.commit()

            query = "select * from user where uname = %s or password = %s"
            p = ""
            values = (uname,p)
            cursor.execute(query,values)
            row = cursor.fetchall()
            if row :
                self.showMessageBox("Information", "Username already exists")
                self.usernameInput.setText("")
                self.passwordInput.setText("")
            else :
                query = "insert into user (uname,  password) values (%s,%s)"
                values = (uname, passwd)
                cursor.execute(query, values)
                database.commit()
                print("Register Successfully")
                self.usernameInput.setText("")
                self.passwordInput.setText("")
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
        Dialog.resize(1440, 820)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1440, 820))
        # self.label.setStyleSheet("background-image: url(../Prediction/images/adminBackground.jpg); background-size : auto;")
        self.label.setStyleSheet("border-image: url(../Prediction/images/userloginBackground.jpg) 0 0 0 0 stretch stretch;")
        self.label.setText("")
        self.label.setObjectName("label")

        self.titleLabel = QtWidgets.QLabel(Dialog)
        self.titleLabel.setGeometry(QtCore.QRect(500, 220, 790, 81))
        self.titleLabel.setStyleSheet("color: rgb(255, 255, 255); font: 70pt \"Franklin Gothic Heavy\";")
        self.titleLabel.setObjectName("titleLabel")

        self.usernameLabel = QtWidgets.QLabel(Dialog)
        self.usernameLabel.setGeometry(QtCore.QRect(672, 320, 100, 26))
        self.usernameLabel.setStyleSheet("font: 18pt \"Franklin Gothic Heavy\";color: #ffffff;")
        self.usernameLabel.setObjectName("usernameLabel")

        self.usernameInput = QtWidgets.QLineEdit(Dialog)
        self.usernameInput.setGeometry(QtCore.QRect(595, 350, 251, 31))
        self.usernameInput.setText("")
        self.usernameInput.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameInput.setObjectName("usernameInput")
        self.usernameInput.setStyleSheet("font: 20pt;")

        self.passwordLabel = QtWidgets.QLabel(Dialog)
        self.passwordLabel.setGeometry(QtCore.QRect(672, 400, 100, 26))
        self.passwordLabel.setStyleSheet("font: 18pt \"Franklin Gothic Heavy\";color: #ffffff;")
        self.passwordLabel.setObjectName("passwordLabel")

        self.passwordInput = QtWidgets.QLineEdit(Dialog)
        self.passwordInput.setGeometry(QtCore.QRect(595, 430, 251, 31))
        self.passwordInput.setText("")
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setObjectName("passwordInput")
        self.passwordInput.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordInput.setStyleSheet("font: 20pt;")

        self.registerBtn = QtWidgets.QPushButton(Dialog)
        self.registerBtn.setGeometry(QtCore.QRect(595, 490, 251, 41))
        self.registerBtn.setStyleSheet("background-color: rgb(255, 255, 255);font: 16pt \"Franklin Gothic Heavy\";\n")
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