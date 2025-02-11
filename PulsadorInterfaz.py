# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PulsadorInterfaz.ui'
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
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(617, 323)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnPulsar = QPushButton(self.centralwidget)
        self.btnPulsar.setObjectName(u"btnPulsar")
        self.btnPulsar.setGeometry(QRect(150, 80, 75, 24))
        self.lblContador = QLabel(self.centralwidget)
        self.lblContador.setObjectName(u"lblContador")
        self.lblContador.setGeometry(QRect(340, 90, 49, 16))
        self.btnResetear = QPushButton(self.centralwidget)
        self.btnResetear.setObjectName(u"btnResetear")
        self.btnResetear.setGeometry(QRect(230, 130, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 617, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnPulsar.setText(QCoreApplication.translate("MainWindow", u"Pulsar", None))
        self.lblContador.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btnResetear.setText(QCoreApplication.translate("MainWindow", u"Resetear", None))
    # retranslateUi

