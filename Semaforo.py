import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from src import SemaforoInterfaz

class Semaforo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=SemaforoInterfaz.Ui_MainWindow()
        self.ui.setupUi(self)

        # Estilo general de la ventana
        self.setStyleSheet("background-color: black;")
        self.resize(650, 200)

        # Configuración inicial de los elementos
        self.ui.pushButton.setStyleSheet("background-color: white;")
        self.estado=2
        self.ui.lblRojo.setStyleSheet("QLabel {background-color: red}")
        self.ui.lblAmarillo.setStyleSheet("QLabel {background-color: white}")
        self.ui.lblVerde.setStyleSheet("QLabel {background-color: white}")

        # Conexion del botón a la función de cambio de color
        self.ui.pushButton.clicked.connect(self.cambioColor)
    def cambioColor(self):
        # Reseteamos todos los colores a blanco
        self.ui.lblRojo.setStyleSheet("QLabel {background-color: white}")
        self.ui.lblAmarillo.setStyleSheet("QLabel {background-color: white}")
        self.ui.lblVerde.setStyleSheet("QLabel {background-color: white}")

        # Cambiamos el color del semáforo según el estado
        if self.estado == 1:
            self.ui.lblRojo.setStyleSheet("QLabel {background-color: red}")
            self.estado = 2
        elif self.estado == 2:
            self.ui.lblAmarillo.setStyleSheet("QLabel {background-color: yellow}")
            self.estado = 3
        elif self.estado == 3:
            self.ui.lblVerde.setStyleSheet("QLabel {background-color: green}")
            self.estado = 1

if __name__=="__main__":
    app=QApplication(sys.argv)
    window =Semaforo()
    window.show()
    sys.exit(app.exec())