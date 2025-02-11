# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DescuentoInterfaz.ui'
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
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(613, 330)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.txtPrecio = QTextEdit(self.centralwidget)
        self.txtPrecio.setObjectName(u"txtPrecio")
        self.txtPrecio.setGeometry(QRect(210, 50, 101, 31))
        self.txtDescuento = QTextEdit(self.centralwidget)
        self.txtDescuento.setObjectName(u"txtDescuento")
        self.txtDescuento.setGeometry(QRect(210, 100, 101, 31))
        self.btnCalcular = QPushButton(self.centralwidget)
        self.btnCalcular.setObjectName(u"btnCalcular")
        self.btnCalcular.setGeometry(QRect(60, 160, 75, 24))
        self.lblDescuento = QLabel(self.centralwidget)
        self.lblDescuento.setObjectName(u"lblDescuento")
        self.lblDescuento.setGeometry(QRect(70, 110, 71, 16))
        self.lblPrecio = QLabel(self.centralwidget)
        self.lblPrecio.setObjectName(u"lblPrecio")
        self.lblPrecio.setGeometry(QRect(70, 50, 71, 16))
        self.txtPrecioFinal = QPlainTextEdit(self.centralwidget)
        self.txtPrecioFinal.setObjectName(u"txtPrecioFinal")
        self.txtPrecioFinal.setGeometry(QRect(210, 160, 101, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 613, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnCalcular.setText(QCoreApplication.translate("MainWindow", u"Precio final", None))
        self.lblDescuento.setText(QCoreApplication.translate("MainWindow", u"Descuento %", None))
        self.lblPrecio.setText(QCoreApplication.translate("MainWindow", u"Precio inicial", None))
    # retranslateUi

