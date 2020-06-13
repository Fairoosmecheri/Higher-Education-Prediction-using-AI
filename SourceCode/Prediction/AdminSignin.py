from PyQt5 import QtCore, QtGui, QtWidgets

from AdminHome import AdminHome


class AdminSignin(object):

    def adminSignin(self):
        uname = self.usernameLineEdit.text()
        passwd = self.passwwordLineEdit.text()
        if ((uname == "admin") and (passwd == "admin")):
            self.usernameLineEdit.setText("")
            self.passwwordLineEdit.setText("")
            self.admin = QtWidgets.QDialog()
            self.ui = AdminHome()
            self.ui.setupUi(self.admin)
            self.admin.show()
        else:
            self.usernameLineEdit.setText("")
            self.passwwordLineEdit.setText("")
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
        Dialog.resize(1440, 820)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1440, 820))
        #self.label.setStyleSheet("background-image: url(../Prediction/images/adminBackground.jpg); background-size : auto;")
        self.label.setStyleSheet("border-image: url(../Prediction/images/adminBackground.jpg) 0 0 0 0 stretch stretch;")
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

        self.usernameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.usernameLineEdit.setGeometry(QtCore.QRect(595, 350, 251, 31))
        self.usernameLineEdit.setText("")
        self.usernameLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.usernameLineEdit.setStyleSheet("font: 20pt;")

        self.passwordLabel = QtWidgets.QLabel(Dialog)
        self.passwordLabel.setGeometry(QtCore.QRect(672, 400, 100, 26))
        self.passwordLabel.setStyleSheet("font: 18pt \"Franklin Gothic Heavy\";color: #ffffff;")
        self.passwordLabel.setObjectName("passwordLabel")

        self.passwwordLineEdit = QtWidgets.QLineEdit(Dialog)
        self.passwwordLineEdit.setGeometry(QtCore.QRect(595, 430, 251, 31))
        self.passwwordLineEdit.setText("")
        self.passwwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwwordLineEdit.setObjectName("passwwordLineEdit")
        self.passwwordLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.passwwordLineEdit.setStyleSheet("font: 20pt;")

        self.signinButton = QtWidgets.QPushButton(Dialog)
        self.signinButton.setGeometry(QtCore.QRect(595, 490, 251, 41))
        self.signinButton.setStyleSheet("background-color: rgb(255, 255, 255);font: 16pt \"Franklin Gothic Heavy\";\n")
        self.signinButton.setObjectName("signinButton")
        self.signinButton.clicked.connect(self.adminSignin)



        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Admin Login"))
        self.titleLabel.setText(_translate("Dialog", "ADMIN LOGIN"))
        self.usernameLabel.setText(_translate("Dialog", "USERNAME"))
        self.passwordLabel.setText(_translate("Dialog", "PASSWORD"))
        self.signinButton.setText(_translate("Dialog", "SIGN IN"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = AdminSignin()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())