from PyQt5 import QtCore, QtGui, QtWidgets
from DBConnection import DBConnection
from sklearn.neural_network import MLPClassifier
import numpy as np
import pandas as pd


class Ui_Predict(object):

    def predict(self):
        try:
            trainset = []

            if ( self.chinese.text() == "" or self.math.text() == "" or self.phy.text() == "" or self.che.text() == "" or self.bio.text() == "" or self.eng.text() == "" or self.sprt.text() == "" or self.condt.text() == "" or self.art.text() == "" ):
                self.showMessageBox("Information", "Please enter marks of all subjects")
            else :

                chinesemark = int(self.chinese.text())
                mathmark = int(self.math.text())
                phymark = int(self.phy.text())
                chemark = int(self.che.text())
                biomark = int(self.bio.text())
                histmark = int(self.hist.text())
                condtmark = int(self.condt.text())
                sprtmark = int(self.sprt.text())
                engmark = int(self.eng.text())
                artmark = int(self.art.text())

                testingdata = [mathmark, chinesemark, engmark, phymark, chemark,biomark,histmark,condtmark,sprtmark,artmark]
                testingdata = [testingdata]
                testingdata = np.array(testingdata)
                print("testingdata = ",testingdata)
                testdata = testingdata.reshape(len(testingdata), -1)

                database = DBConnection.getConnection()
                cursor = database.cursor()
                cursor.execute(
                    "select math,chinese,eng,phy,che,bio,hist,condt,sprt,art,result from dataset")
                row = cursor.fetchall()
                y_train = []
                trainset.clear()
                y_train.clear()
                for r in row:
                    x_train = []
                    x_train.clear()
                    x_train.append(float(r[0]))
                    x_train.append(float(r[1]))
                    x_train.append(float(r[2]))
                    x_train.append(float(r[3]))
                    x_train.append(float(r[4]))
                    x_train.append(float(r[5]))
                    x_train.append(float(r[6]))
                    x_train.append(float(r[7]))
                    x_train.append(float(r[8]))
                    x_train.append(float(r[9]))
                    y_train.append(r[10])
                    trainset.append(x_train)
                print("y=", y_train)
                print("trd=", trainset)
                trainset = np.array(trainset)
                print("trd=", trainset)

                # Train the model
                print("y_train = ",y_train)
                y_train = np.array(y_train)
                print("y_train = ",y_train)

                cnn = MLPClassifier()
                cnn.fit(trainset, y_train)
                reslt = cnn.predict(testdata)
                print("pre=", reslt)
                self.result.setText(reslt[0])
                query = "insert into dataset values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                values = (str(mathmark), str(chinesemark), str(engmark), str(phymark), str(chemark), str(biomark), str(histmark), str(condtmark), str(sprtmark),str(artmark), str(reslt[0]))
                print(values)
                cursor.execute(query, values)
                database.commit()

        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def showMessageBox(self, title, message):
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setWindowTitle(title)
            msgBox.setText(message)
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(852, 501)
        Dialog.setStyleSheet("background-color: rgb(0, 85, 127);")
        self.titleLabel = QtWidgets.QLabel(Dialog)
        self.titleLabel.setGeometry(QtCore.QRect(180, 80, 331, 61))
        self.titleLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "font: 12pt \"Franklin Gothic Heavy\";")
        self.titleLabel.setObjectName("titleLabel")

        self.mathLabel = QtWidgets.QLabel(Dialog)
        self.mathLabel.setGeometry(QtCore.QRect(70, 165, 60, 40))
        self.mathLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "font: 10pt \"Franklin Gothic Heavy\";")
        self.mathLabel.setObjectName("mathLabel")
        self.math = QtWidgets.QLineEdit(Dialog)
        self.math.setGeometry(QtCore.QRect(70, 200, 60, 40))
        self.math.setText("")
        self.math.setObjectName("math")

        self.chineseLabel = QtWidgets.QLabel(Dialog)
        self.chineseLabel.setGeometry(QtCore.QRect(140, 165, 60, 40))
        self.chineseLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "font: 10pt \"Franklin Gothic Heavy\";")
        self.chineseLabel.setObjectName("chineseLabel")
        self.chinese = QtWidgets.QLineEdit(Dialog)
        self.chinese.setGeometry(QtCore.QRect(140, 200, 60, 40))
        self.chinese.setText("")
        self.chinese.setObjectName("chinese")

        self.engLabel = QtWidgets.QLabel(Dialog)
        self.engLabel.setGeometry(QtCore.QRect(210, 165, 60, 40))
        self.engLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "font: 10pt \"Franklin Gothic Heavy\";")
        self.engLabel.setObjectName("engLabel")
        self.eng = QtWidgets.QLineEdit(Dialog)
        self.eng.setGeometry(QtCore.QRect(210, 200, 60, 40))
        self.eng.setText("")
        self.eng.setObjectName("eng")

        self.phyLabel = QtWidgets.QLabel(Dialog)
        self.phyLabel.setGeometry(QtCore.QRect(280, 165, 60, 40))
        self.phyLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "font: 10pt \"Franklin Gothic Heavy\";")
        self.phyLabel.setObjectName("phyLabel")
        self.phy = QtWidgets.QLineEdit(Dialog)
        self.phy.setGeometry(QtCore.QRect(280, 200, 60, 40))
        self.phy.setText("")
        self.phy.setObjectName("phy")

        self.cheLabel = QtWidgets.QLabel(Dialog)
        self.cheLabel.setGeometry(QtCore.QRect(350, 165, 60, 40))
        self.cheLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 10pt \"Franklin Gothic Heavy\";")
        self.cheLabel.setObjectName("cheLabel")
        self.che = QtWidgets.QLineEdit(Dialog)
        self.che.setGeometry(QtCore.QRect(350, 200, 60, 40))
        self.che.setText("")
        self.che.setObjectName("che")

        self.bioLabel = QtWidgets.QLabel(Dialog)
        self.bioLabel.setGeometry(QtCore.QRect(420, 165, 60, 40))
        self.bioLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 10pt \"Franklin Gothic Heavy\";")
        self.bioLabel.setObjectName("bioLabel")
        self.bio = QtWidgets.QLineEdit(Dialog)
        self.bio.setGeometry(QtCore.QRect(420, 200, 60, 40))
        self.bio.setText("")
        self.bio.setObjectName("bio")

        self.histLabel = QtWidgets.QLabel(Dialog)
        self.histLabel.setGeometry(QtCore.QRect(490, 165, 60, 40))
        self.histLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 10pt \"Franklin Gothic Heavy\";")
        self.histLabel.setObjectName("histLabel")
        self.hist = QtWidgets.QLineEdit(Dialog)
        self.hist.setGeometry(QtCore.QRect(490, 200, 60, 40))
        self.hist.setText("")
        self.hist.setObjectName("hist")

        self.condtLabel = QtWidgets.QLabel(Dialog)
        self.condtLabel.setGeometry(QtCore.QRect(560, 165, 60, 40))
        self.condtLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 10pt \"Franklin Gothic Heavy\";")
        self.condtLabel.setObjectName("condtLabel")
        self.condt = QtWidgets.QLineEdit(Dialog)
        self.condt.setGeometry(QtCore.QRect(560, 200, 60, 40))
        self.condt.setText("")
        self.condt.setObjectName("condt")

        self.sprtLabel = QtWidgets.QLabel(Dialog)
        self.sprtLabel.setGeometry(QtCore.QRect(630, 165, 60, 40))
        self.sprtLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 10pt \"Franklin Gothic Heavy\";")
        self.sprtLabel.setObjectName("sprtLabel")
        self.sprt = QtWidgets.QLineEdit(Dialog)
        self.sprt.setGeometry(QtCore.QRect(630, 200, 60, 40))
        self.sprt.setText("")
        self.sprt.setObjectName("sprt")

        self.artLabel = QtWidgets.QLabel(Dialog)
        self.artLabel.setGeometry(QtCore.QRect(700, 165, 60, 40))
        self.artLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 10pt \"Franklin Gothic Heavy\";")
        self.artLabel.setObjectName("artLabel")
        self.art = QtWidgets.QLineEdit(Dialog)
        self.art.setGeometry(QtCore.QRect(700, 200, 60, 40))
        self.art.setText("")
        self.art.setObjectName("art")

        self.predictBtn = QtWidgets.QPushButton(Dialog)
        self.predictBtn.setGeometry(QtCore.QRect(180, 280, 181, 41))
        self.predictBtn.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "font: 75 12pt \"Verdana\";")
        self.predictBtn.setObjectName("predictBtn")
        self.predictBtn.clicked.connect(self.predict)



        self.resultLabel = QtWidgets.QLabel(Dialog)
        self.resultLabel.setGeometry(QtCore.QRect(90, 390, 141, 31))
        self.resultLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "font: 12pt \"Franklin Gothic Heavy\";")
        self.resultLabel.setObjectName("resultLabel")
        self.result = QtWidgets.QLabel(Dialog)
        self.result.setGeometry(QtCore.QRect(230, 380, 351, 51))
        self.result.setStyleSheet("color: rgb(255, 255, 255);\n"
                                  "font: 12pt \"Franklin Gothic Heavy\";")
        self.result.setText("")
        self.result.setObjectName("result")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Prediction"))
        self.titleLabel.setText(_translate("Dialog", "Prediction Universities Degree"))
        self.predictBtn.setText(_translate("Dialog", "Predict"))
        self.resultLabel.setText(_translate("Dialog", "Result       :"))

        self.mathLabel.setText(_translate("Dialog", "Mathematics"))
        self.chineseLabel.setText(_translate("Dialog", "Chinese"))
        self.engLabel.setText(_translate("Dialog", "English"))
        self.phyLabel.setText(_translate("Dialog", "Physics"))
        self.cheLabel.setText(_translate("Dialog", "Chemistry"))
        self.bioLabel.setText(_translate("Dialog", "Biology"))
        self.histLabel.setText(_translate("Dialog", "History"))
        self.condtLabel.setText(_translate("Dialog", "Conduct"))
        self.sprtLabel.setText(_translate("Dialog", "Sports"))
        self.artLabel.setText(_translate("Dialog", "Arts"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Predict()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
