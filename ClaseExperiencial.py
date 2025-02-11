import sqlite3
import sys
from base64 import b64encode

import bcrypt
from PySide6.QtNetwork import QAbstractSocket
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, \
    QMessageBox, QTableWidget, QTableWidgetItem, QAbstractItemView, QCheckBox

from src.Login import Login


def crear_base_datos():
    conexion=sqlite3.connect("usuario.db")
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL UNIQUE,
            contrasena TEXT NOT NULL,
            es_admin INTEGER NOT NULL DEFAULT 0
        )
    ''')
    conexion.commit()
    conexion.close()
class LoginForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio de Sesion")
        self.setGeometry(100,100,250,250)

        # Layout principal en vertical
        main_layout=QVBoxLayout()
        title=QLabel("Inicio de sesion")
        main_layout.addWidget(title)

        # Entrada de texto para el usuario
        self.username_input= QLineEdit()
        self.username_input.setPlaceholderText("Nombre de usuario")
        main_layout.addWidget(self.username_input)

        # Entrada texto contraseña
        self.password_input=QLineEdit()
        self.password_input.setPlaceholderText("Contraseña")
        self.password_input.setEchoMode(QLineEdit.Password)#Esconde la contraseña
        main_layout.addWidget(self.password_input)

        # Boton Login
        login_button=QPushButton("Iniciar Sesion")
        login_button.clicked.connect(self.iniciar_sesion)
        main_layout.addWidget(login_button)

        # Boton para pasar a la ventana de registro
        register_button=QPushButton("Registrar")
        register_button.clicked.connect(self.registro)
        main_layout.addWidget(register_button)

        #Establecer el layput_principal
        central_widget= QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def registro(self):
        self.registro= Registerform()
        self.registro.show()
        self.close()

    def iniciar_sesion(self):
        usuario= self.username_input.text()
        contrasena=self.password_input.text()
        if not usuario or not contrasena:
            QMessageBox.warning(self,"Error","Todos los campos son obligatorios")

        conexion= sqlite3.connect("usuario.db")
        cursor=conexion.cursor()
        cursor.execute("SELECT contrasena, es_admin FROM usuarios WHERE usuario = ?",(usuario,))
        resultado=cursor.fetchone()#por que solo devolvera un resultado
        conexion.close()
        #Si el resultado es no nulo y la contraseña es igual a resultado pasamos de pantalla
        if resultado and bcrypt.checkpw(contrasena.encode(),resultado[0]):
            self.bienvenida=WelcomeForm(usuario,resultado[1])#resultado alberga 2 valores le apasamos si es admin --> 1
            self.bienvenida.show()
            self.close()
        else:
            QMessageBox.critical(self,"Error","Usuario o contraseña incorrecta")
            self.username_input.clear()
            self.password_input.clear()


class QCheckbox:
    pass


class Registerform(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro")
        self.setGeometry(100,100,250,250)

        # Layout principal en vertical
        main_layout = QVBoxLayout()
        title = QLabel("Registro")
        main_layout.addWidget(title)

        # Entrada de texto para el usuario
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Nombre de usuario")
        main_layout.addWidget(self.username_input)

        # Entrada texto contraseña
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Contraseña")
        self.password_input.setEchoMode(QLineEdit.Password)  # Esconde la contraseña
        main_layout.addWidget(self.password_input)

        #check box para marcar si es admin
        self.admin_checkbox= QCheckBox("¿Es administrador?")
        main_layout.addWidget(self.admin_checkbox)

        # Boton registro de usuario
        register_button = QPushButton("Registrar")
        register_button.clicked.connect(self.registrar_usuario)
        main_layout.addWidget(register_button)

        # Boton Login -> vuelve a la ventana login para iniciar sesion
        back_button = QPushButton("Iniciar Sesion")
        back_button.clicked.connect(self.volver_a_login)
        main_layout.addWidget(back_button)

        # Establecer el layout_principal
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def volver_a_login(self):
        self.login= LoginForm()#Creamos una instancia de la ventan login
        self.login.show()#abrimos la ventana login
        self.close()#cerramos la ventana actual

    def registrar_usuario(self):
        usuario=self.username_input.text()#Recogemos usuario
        contrasena=self.password_input.text()#Recogemos contraseña
        es_admin=1 if self.admin_checkbox.isChecked() else 0

        if not usuario or not contrasena:
            QMessageBox().warning(self,"Error","Todos los campos son obligatorios")
        else:
            #encriptamos la contraseña
            contrasena_encriptada= bcrypt.hashpw(contrasena.encode(), bcrypt.gensalt())
            try:
                conexxion= sqlite3.connect("usuario.db")
                cursor= conexxion.cursor()
                cursor.execute("INSERT INTO usuarios(usuario, contrasena, es_admin) VALUES (?,?,?)",
                               (usuario,contrasena_encriptada,es_admin))
                conexxion.commit()
                conexxion.close()
                QMessageBox.information(self,"Exito","Usuario ha sido registrado")
                self.volver_a_login() #Volvemos a la pantalla de inicio de sesion
            except sqlite3.IntegrityError:
                QMessageBox.critical(self,"Error","El usuario ya existe")


class WelcomeForm(QMainWindow):
    def __init__(self, usuario2,es_admin):
        super().__init__()
        self.setWindowTitle("Bienvenido")
        self.setGeometry(100,100,250,250)

        self.usuario2 = usuario2
        self.es_admin=es_admin
        # Layout principal
        main_layout=QVBoxLayout()

        #Etiqueta principal
        welcome_label=QLabel(f"¡Bienvenido, {self.usuario2}!")
        main_layout.addWidget(welcome_label)

        #Pintar la tabla
        self.tabla=QTableWidget()
        self.tabla.setColumnCount(2)#numeroColumnas
        self.tabla.setHorizontalHeaderLabels(["Usuario", "Contrasena-Encriptada"])#Estalecemos los nombres delas columnas
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)#Definimos el comportamiento de la tabla
        self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)
        main_layout.addWidget(self.tabla)
        self.cargar_usuarios()

        if es_admin==1:
            # Boton para eliminar una cuenta
            delete_button = QPushButton("Borrar cuenta seleccionada")
            delete_button.clicked.connect(self.borrar_cuenta)
            main_layout.addWidget(delete_button)

        cerrar_sesion=QPushButton("Cerrar Sesion")
        cerrar_sesion.clicked.connect(lambda : self.close())
        main_layout.addWidget(cerrar_sesion)
        #Establecemos el layout principal como el central Contenedor
        central_widget= QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def cargar_usuarios(self):
        conexion=sqlite3.connect("usuario.db")
        cursor= conexion.cursor()
        cursor.execute("SELECT usuario, contrasena FROM usuarios")
        usuarios = cursor.fetchall() ##usuarios almacena todos los datos
        conexion.close()
        self.tabla.setRowCount(len(usuarios))#numero de filas de la tabla sea = a la longitud de usuarios

        #para cada fila row me coge el usuario y contraseña de usuarios
        for row, (usuario, contrasena) in enumerate(usuarios):#enumerat devuelve tanto la posicion id y el dato
            # almacenado osea usuario y contraseña
            #va asignando a cada item el usuario y la contraseña
            self.tabla.setItem(row, 0, QTableWidgetItem(usuario))
            contrasena_legible = b64encode(contrasena).decode("utf-8")
            self.tabla.setItem(row, 1, QTableWidgetItem(contrasena_legible))
    def borrar_cuenta(self):
        selected_row= self.tabla.currentRow()
        if selected_row== -1: #-1 cuando no hay ninguna fila seleccionada
            QMessageBox.warning(self,"Error","Selecciona un cuenta para borrarla")
        else:
            #Extraemos el texto del usuario, cogeme la fila seleccionada y vete a la columna 0
            usuario= self.tabla.item(selected_row,0).text()
            respuesta=QMessageBox.question(self,"Confirmacion",f"Estas seguro de borrar la cuenta de '{usuario}'",
                                           QMessageBox.Yes | QMessageBox.No)
            if respuesta == QMessageBox.Yes: #Si la respuesta es si eliminamos de la bd
                conexion = sqlite3.connect("usuario.db")
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM usuarios WHERE usuario = ?", (usuario,))
                conexion.commit()
                conexion.close()
                QMessageBox.information(self, "Exito", "Cuenta eliminada con exito")
                self.cargar_usuarios()
                #si elimina su usario mismo con el que se ha logueado se le cierra la sesion
                if usuario==self.usuario2:
                    QMessageBox.information(self,"Exito","Sesion Finalizada")
                    self.login=LoginForm()
                    self.login.show()
                    self.close()


if __name__=="__main__":
    crear_base_datos()
    app=QApplication(sys.argv)
    ventana=Registerform()
    ventana.show()
    sys.exit(app.exec())