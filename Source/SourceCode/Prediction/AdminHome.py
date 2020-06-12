
from PyQt5 import QtCore, QtGui, QtWidgets
from ViewDataSet import ViewDataSet
from UploadDataSet import UploadDataSet
from DBConnection import DBConnection

class AdminHome(object):

    def viewdataSet(self):
        self.viewds = QtWidgets.QDialog()
        self.ui =ViewDataSet()
        self.ui.setupUi(self.viewds)
        self.ui.viewdata()
        self.viewds.show()
    def uploaddataset(self):
        self.upld = QtWidgets.QDialog()
        self.ui = UploadDataSet()
        self.ui.setupUi(self.upld)
        self.upld.show()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 496)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 691, 521))
        self.label.setStyleSheet("background-image: url(../Prediction/images/arch.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.datasetUploadBtn = QtWidgets.QPushButton(Dialog)
        self.datasetUploadBtn.setGeometry(QtCore.QRect(280, 190, 151, 41))
        self.datasetUploadBtn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 75 16pt \"Times New Roman\";\n")
        #self.pushButton.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
#"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.datasetUploadBtn.setObjectName("datasetUploadBtn")
        self.datasetUploadBtn.clicked.connect(self.uploaddataset)
        self.viewDatasetBtn = QtWidgets.QPushButton(Dialog)
        self.viewDatasetBtn.setGeometry(QtCore.QRect(280, 280, 151, 41))
        self.viewDatasetBtn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 75 16pt \"Times New Roman\";\n")
#"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.viewDatasetBtn.setObjectName("viewDatasetBtn")
        self.viewDatasetBtn.clicked.connect(self.viewdataSet)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Admin Home"))
        self.datasetUploadBtn.setText(_translate("Dialog", "DataSet Upload"))
        self.viewDatasetBtn.setText(_translate("Dialog", "View DataSet"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = AdminHome()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

