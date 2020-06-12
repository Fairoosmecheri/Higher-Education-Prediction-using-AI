from PyQt5 import QtCore, QtGui, QtWidgets

from AdminHome import AdminHome


class AdminSignin(object):

    def adminSignin(self):
        uname = self.lineEdit.text()
        passwd = self.lineEdit_1.text()
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
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 70, 141, 20))
        self.label.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 130, 71, 16))
        self.label_2.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 150, 251, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(110, 190, 71, 16))
        self.label_3.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_1 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_1.setGeometry(QtCore.QRect(110, 210, 251, 31))
        self.lineEdit_1.setText("")
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(164, 260, 151, 41))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 75 16pt \"Times New Roman\";\n")
        # self.pushButton.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
        # "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.adminSignin)



        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Admin Login"))
        self.label.setText(_translate("Dialog", "Admin Login"))
        self.label_2.setText(_translate("Dialog", "Username"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.pushButton.setText(_translate("Dialog", "Sign in"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = AdminSignin()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())