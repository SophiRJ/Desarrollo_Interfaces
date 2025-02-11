

from PySide6.QtWidgets import QApplication, QMessageBox, QWidget, QVBoxLayout,  QPushButton, \
    QLineEdit


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(300,300,250,150)

        #Creamos layout principal
        self.layout_principal=QVBoxLayout()
        self.setLayout(self.layout_principal)

        #Usuario
        self.usuario=QLineEdit()
        self.usuario.setPlaceholderText("Usuario")
        self.layout_principal.addWidget(self.usuario)

        #Contraseña
        self.contrasenia=QLineEdit()
        self.contrasenia.setPlaceholderText("Contraseña")
        self.contrasenia.setEchoMode(QLineEdit.Password)
        self.layout_principal.addWidget(self.contrasenia)

        #Boton
        self.boton=QPushButton()
        self.boton.setText("Iniciar Sesion")
        self.layout_principal.addWidget(self.boton)

        #Conexion boton
        self.boton.clicked.connect(lambda : self.manejo_click())
    def limpiar(self):
        self.usuario.clear()
        self.contrasenia.clear()
    def manejo_click(self):
        user=self.usuario.text().strip()
        contrasenia=self.contrasenia.text().strip()
        if not user or not contrasenia:
            QMessageBox.warning(self,"Advertencia","Faltan datos")
        else:
            print(f"Bienvenid@ {user}")
            QMessageBox.information(self,"Exito",f"Bienvenid@ {user}")
            self.limpiar()
if __name__=="__main__":
    app=QApplication([])
    window=Login()
    window.show()
    app.exec()
