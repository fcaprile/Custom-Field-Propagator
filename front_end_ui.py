# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front_end.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(749, 453)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 350, 75, 21))
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 380, 241, 20))
        self.label_7.setObjectName("label_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 380, 75, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setEnabled(True)
        self.comboBox.setGeometry(QtCore.QRect(360, 190, 101, 22))
        self.comboBox.setEditable(False)
        self.comboBox.setDuplicatesEnabled(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(280, 190, 81, 21))
        self.label_15.setObjectName("label_15")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 721, 171))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(560, 20, 151, 141))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 50, 41, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 20, 41, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 81, 20))
        self.label_4.setObjectName("label_4")
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setGeometry(QtCore.QRect(10, 80, 61, 16))
        self.label_16.setObjectName("label_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_17.setGeometry(QtCore.QRect(100, 80, 41, 20))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_20.setGeometry(QtCore.QRect(100, 110, 41, 20))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setGeometry(QtCore.QRect(10, 110, 51, 16))
        self.label_19.setObjectName("label_19")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 16, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(300, 30, 41, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(90, 50, 41, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 80, 41, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(60, 50, 21, 16))
        self.label.setObjectName("label")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_12.setGeometry(QtCore.QRect(90, 110, 41, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(160, 30, 141, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_15.setGeometry(QtCore.QRect(300, 60, 41, 20))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(170, 50, 131, 41))
        self.label_10.setObjectName("label_10")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(160, 80, 131, 41))
        self.label_14.setObjectName("label_14")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_16.setGeometry(QtCore.QRect(300, 90, 41, 20))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_18.setGeometry(QtCore.QRect(300, 120, 41, 20))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(160, 120, 141, 20))
        self.label_17.setObjectName("label_17")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(360, 50, 181, 81))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(30, 20, 91, 21))
        self.label_12.setObjectName("label_12")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_11.setGeometry(QtCore.QRect(130, 50, 41, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_13.setGeometry(QtCore.QRect(130, 20, 41, 20))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 50, 121, 20))
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 100, 71, 16))
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(10, 110, 81, 21))
        self.label_13.setObjectName("label_13")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 250, 101, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(110, 310, 251, 21))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 310, 81, 21))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(390, 250, 101, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(20, 190, 261, 21))
        self.radioButton.setObjectName("radioButton")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_19.setEnabled(False)
        self.lineEdit_19.setGeometry(QtCore.QRect(140, 220, 41, 20))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 230, 121, 16))
        self.label_3.setObjectName("label_3")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(30, 210, 101, 31))
        self.label_18.setObjectName("label_18")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_21.setGeometry(QtCore.QRect(360, 220, 161, 20))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(20, 350, 231, 20))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(250, 220, 101, 21))
        self.label_22.setObjectName("label_22")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 410, 241, 20))
        self.label_8.setObjectName("label_8")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 410, 75, 21))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(20, 250, 151, 16))
        self.label_23.setObjectName("label_23")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_22.setEnabled(False)
        self.lineEdit_22.setGeometry(QtCore.QRect(140, 250, 41, 20))
        self.lineEdit_22.setObjectName("lineEdit_22")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Phase Plate Simulator"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Save XZ and XY plane\'s intensity:</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Save"))
        self.comboBox.setItemText(0, _translate("MainWindow", "VPP (0-2pi)"))
        self.comboBox.setItemText(1, _translate("MainWindow", "None (Gaussian beam)"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Custom"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Phase mask:</span></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "Parameters"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Resolution parameters (nm)"))
        self.lineEdit_4.setText(_translate("MainWindow", "8"))
        self.label_6.setText(_translate("MainWindow", "Axial resolution"))
        self.lineEdit_5.setText(_translate("MainWindow", "5"))
        self.label_4.setText(_translate("MainWindow", "Radial resolution "))
        self.label_16.setText(_translate("MainWindow", "Radial FOV"))
        self.lineEdit_17.setText(_translate("MainWindow", "1000"))
        self.lineEdit_20.setText(_translate("MainWindow", "2000"))
        self.label_19.setText(_translate("MainWindow", "Axial FOV"))
        self.label_2.setText(_translate("MainWindow", "n"))
        self.lineEdit_3.setText(_translate("MainWindow", "640"))
        self.lineEdit.setText(_translate("MainWindow", "1.4"))
        self.lineEdit_2.setText(_translate("MainWindow", "1.5"))
        self.label.setText(_translate("MainWindow", "NA"))
        self.lineEdit_12.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "Wavelength at vacuum (nm)"))
        self.lineEdit_15.setText(_translate("MainWindow", "1"))
        self.label_10.setText(_translate("MainWindow", "Laser intensity (kW/cm^2)"))
        self.label_14.setText(_translate("MainWindow", "Gaussian beam radius (mm)"))
        self.lineEdit_16.setText(_translate("MainWindow", "5"))
        self.lineEdit_18.setText(_translate("MainWindow", "3"))
        self.label_17.setText(_translate("MainWindow", "Lens\'s aperture radius (mm)"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Polarization"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'arial,sans-serif\'; font-size:px; color:#222222; background-color:#ffffff;\">Δ </span>phase (degrees)</p></body></html>"))
        self.lineEdit_11.setText(_translate("MainWindow", "45"))
        self.lineEdit_13.setText(_translate("MainWindow", "90"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p>tan<span style=\" font-family:\'arial,sans-serif\'; color:#3c4043; background-color:#ffffff;\">−1</span>(ey/ex) (degrees)</p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "Axial distance"))
        self.label_13.setText(_translate("MainWindow", "from focus (nm)"))
        self.pushButton_3.setText(_translate("MainWindow", "Simulate"))
        self.lineEdit_14.setText(_translate("MainWindow", "(leave like this for local folder)"))
        self.pushButton_5.setText(_translate("MainWindow", "Saving folder"))
        self.pushButton_6.setText(_translate("MainWindow", "Clear images"))
        self.radioButton.setText(_translate("MainWindow", "Simulate field at the objective"))
        self.lineEdit_19.setText(_translate("MainWindow", "1000"))
        self.label_3.setText(_translate("MainWindow", " plate to objective (mm)"))
        self.label_18.setText(_translate("MainWindow", "Distance from phase"))
        self.lineEdit_21.setText(_translate("MainWindow", "VPP mask simulation"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Save text with used parameters:</span></p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Simulation name:</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Save amplitudes on the XY plane:</span></p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "Save"))
        self.label_23.setText(_translate("MainWindow", "Phase mask radius (mm)"))
        self.lineEdit_22.setText(_translate("MainWindow", "5"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

