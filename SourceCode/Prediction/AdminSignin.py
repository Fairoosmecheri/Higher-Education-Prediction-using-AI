from PyQt5 import QtCore, QtGui, QtWidgets

from AdminHome import AdminHome


class AdminSignin(object):

    def adminSignin(self):
        uname = self.usernameLineEdit.text()
        passwd = self.passwwordLineEdit.text()
        if ((uname == "admin") and (passwd == "admin")):
            self.admin = QtWidgets.QDialog()
            self.ui = AdminHome()
            self.ui.setupUi(self.admin)
            self.admin.show()
        else:
            self.showMessageBox("Information", "Incorrect username or password")


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
        self.usernameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.usernameLineEdit.setGeometry(QtCore.QRect(110, 150, 251, 31))
        self.usernameLineEdit.setText("")
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.passwordLabel = QtWidgets.QLabel(Dialog)
        self.passwordLabel.setGeometry(QtCore.QRect(110, 190, 71, 16))
        self.passwordLabel.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.passwordLabel.setObjectName("passwordLabel")
        self.passwwordLineEdit = QtWidgets.QLineEdit(Dialog)
        self.passwwordLineEdit.setGeometry(QtCore.QRect(110, 210, 251, 31))
        self.passwwordLineEdit.setText("")
        self.passwwordLineEdit.setObjectName("passwwordLineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(164, 260, 151, 41))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 75 16pt \"Times New Roman\";\n")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.adminSignin)



        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Admin Login"))
        self.titleLabel.setText(_translate("Dialog", "Admin Login"))
        self.usernameLabel.setText(_translate("Dialog", "Username"))
        self.passwordLabel.setText(_translate("Dialog", "Password"))
        self.pushButton.setText(_translate("Dialog", "Sign in"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = AdminSignin()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())