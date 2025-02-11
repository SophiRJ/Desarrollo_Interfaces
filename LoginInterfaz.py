# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginInterfaz.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(248, 320)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnLogin = QPushButton(self.centralwidget)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setGeometry(QRect(60, 170, 81, 24))
        self.txtUsuario = QPlainTextEdit(self.centralwidget)
        self.txtUsuario.setObjectName(u"txtUsuario")
        self.txtUsuario.setGeometry(QRect(80, 40, 111, 31))
        self.txtContrasenia = QPlainTextEdit(self.centralwidget)
        self.txtContrasenia.setObjectName(u"txtContrasenia")
        self.txtContrasenia.setGeometry(QRect(80, 100, 111, 31))
        self.lblUsuario = QLabel(self.centralwidget)
        self.lblUsuario.setObjectName(u"lblUsuario")
        self.lblUsuario.setGeometry(QRect(10, 50, 51, 16))
        self.lblContrasenia = QLabel(self.centralwidget)
        self.lblContrasenia.setObjectName(u"lblContrasenia")
        self.lblContrasenia.setGeometry(QRect(10, 110, 71, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 248, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnLogin.setText(QCoreApplication.translate("MainWindow", u"Iniciar Sesion", None))
        self.lblUsuario.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.lblContrasenia.setText(QCoreApplication.translate("MainWindow", u"Contrasenia", None))
    # retranslateUi

