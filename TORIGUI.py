# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TORIGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TORiUi(object):
    def setupUi(self, TORiUi):
        TORiUi.setObjectName("TORiUi")
        TORiUi.resize(1200, 900)
        self.centralwidget = QtWidgets.QWidget(TORiUi)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1201, 901))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image_processing20200620-21668-36w7bn.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, -70, 571, 261))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Jarvis_Loading_Screen.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1000, 10, 181, 91))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("border2.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(810, 0, 191, 101))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("border1.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(880, 280, 281, 191))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("loader_sci-fi.gif"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(880, 480, 281, 181))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("loader_sci-fi.gif"))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(880, 670, 281, 191))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("loader_sci-fi.gif"))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(-10, 600, 411, 281))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("voice effect 2.gif"))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(-70, 110, 431, 381))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("8871.gif"))
        self.label_9.setScaledContents(False)
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 710, 61, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pngtree-vector-microphone-icon-png-image_889487.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(60, 60))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(1030, 30, 121, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(22)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background: transparent;\n"
"border: 0;\ncolor:#03e8fc;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(850, 30, 121, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(22)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setStyleSheet("background: transparent;\n"
"border: 0;\ncolor:#03e8fc;")
        self.textBrowser_3.setObjectName("textBrowser_3")
        TORiUi.setCentralWidget(self.centralwidget)

        self.retranslateUi(TORiUi)
        QtCore.QMetaObject.connectSlotsByName(TORiUi)

    def retranslateUi(self, TORiUi):
        _translate = QtCore.QCoreApplication.translate
        TORiUi.setWindowTitle(_translate("TORiUi", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TORiUi = QtWidgets.QMainWindow()
    ui = Ui_TORiUi()
    ui.setupUi(TORiUi)
    TORiUi.show()
    sys.exit(app.exec_())
