import sys

from PySide6.QtWidgets import QMainWindow, QApplication
from src import DescuentoInterfaz

class Descuento(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=DescuentoInterfaz.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnCalcular.clicked.connect(self.calcular)

    def calcular(self):
        try:
            precio=int(self.ui.txtPrecio.toPlainText())
            porcentaje=int(self.ui.txtDescuento.toPlainText())
            descuento=(precio*porcentaje)/100
            precio_final=precio - descuento
            self.ui.txtPrecioFinal.setPlainText(str(precio_final))
        except ValueError:
            print("Rellene todos los campos")

if __name__=="__main__":
    app=QApplication(sys.argv)
    window= Descuento()
    window.show()
    sys.exit(app.exec())
