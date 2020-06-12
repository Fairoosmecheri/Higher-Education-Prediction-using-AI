
from PyQt5 import QtCore, QtGui, QtWidgets

from AdminSignin import AdminSignin
from Predict import Ui_Predict
from UserLogin import UserLogin

class Ui_Dialog(object):

    def adminsignin(self):
        self.admin = QtWidgets.QDialog()
        self.ui = AdminSignin()
        self.ui.setupUi(self.admin)
        self.admin.show()
    def userhome(self):
        self.user = QtWidgets.QDialog()
        self.ui = UserLogin()
        self.ui.setupUi(self.user)
        self.user.show()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(621, 513)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-4, 0, 731, 551))
        self.label.setStyleSheet("background-image: url(../Prediction/images/arch.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.adminBtn = QtWidgets.QPushButton(Dialog)
        self.adminBtn.setGeometry(QtCore.QRect(210, 240, 191, 51))
        self.adminBtn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 75 16pt \"Times New Roman\";\n")
        self.adminBtn.setObjectName("adminBtn")
        self.adminBtn.clicked.connect(self.adminsignin)
        self.userBtn = QtWidgets.QPushButton(Dialog)
        self.userBtn.setGeometry(QtCore.QRect(210, 350, 191, 51))
        self.userBtn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Times New Roman\";\n")
        self.userBtn.setObjectName("userBtn")
        self.userBtn.clicked.connect(self.userhome)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", " Higher Education Prediction Using Deep Learning "))
        self.adminBtn.setText(_translate("Dialog", "Admin"))
        self.userBtn.setText(_translate("Dialog", "User"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
