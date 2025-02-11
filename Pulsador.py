import sys

from PySide6.QtWidgets import QMainWindow, QApplication

from src import PulsadorInterfaz


class Pulsador(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=PulsadorInterfaz.Ui_MainWindow()
        self.ui.setupUi(self)

        self.setStyleSheet("background-color: #F4C2C2;")
        self.resize(550, 300)
        self.ui.btnPulsar.setStyleSheet("background-color: white;")
        self.ui.btnResetear.setStyleSheet("background-color: white;")

        self.contador=0
        self.ui.btnPulsar.clicked.connect(self.contarPulsaciones)
        self.ui.btnResetear.clicked.connect(lambda : self.resetear())

    def contarPulsaciones(self):
        self.contador+=1
        self.ui.lblContador.setText(str(self.contador))
    def resetear(self):
        self.ui.lblContador.setText(str(0))
        self.contador=0

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=Pulsador()
    window.show()
    sys.exit(app.exec())
