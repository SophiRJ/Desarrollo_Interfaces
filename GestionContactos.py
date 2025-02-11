import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QPushButton, QApplication, QLineEdit, QWidget, \
    QListWidget, QMessageBox, QMenuBar, QMenu


class GestionContactos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion Contactos")
        self.setGeometry(100,100,400,400)
        self.setContentsMargins(10,10,10,10)

        self.layout_principal=QVBoxLayout()
        self.contactoInput = QLineEdit()
        self.contactoInput.setFixedSize(200,30)
        self.contactoInput.setPlaceholderText("Contacto")
        self.contactoInput.setEnabled(False)
        self.layout_principal.addWidget(self.contactoInput)

        self.listaContactos=contactos(self)

        self.btnAnadir=QPushButton("Registrar usuario")
        self.layout_principal.addWidget(self.btnAnadir)
        self.btnAnadir.clicked.connect(self.registroContacto)

        central_widget=QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(self.layout_principal)

        ##menu
        menubar=QMenuBar()
        self.setMenuBar(menubar)

        file_menu=QMenu("Opciones",self)
        menubar.addMenu(file_menu)

        add_contact=QAction("Agregar contacto",self)
        file_menu.addAction(add_contact)
        add_contact.triggered.connect(lambda :self.control_menubar("Agregar contacto"))

        view_contacts=QAction("Ver contactos",self)
        file_menu.addAction(view_contacts)
        view_contacts.triggered.connect(lambda :self.control_menubar("Ver contactos"))

        delete_contact=QAction("Eliminar contacto",self)
        file_menu.addAction(delete_contact)
        delete_contact.triggered.connect(lambda :self.control_menubar("Eliminar contacto"))
    def control_menubar(self, action_name):
        contacto = self.contactoInput.text()
        if action_name=="Agregar contacto":
            if contacto:
                self.listaContactos.lista.addItem(contacto)
                self.mensaje("Contacto Agregado")
                self.contactoInput.clear()
            else:
                self.mensaje_error("Rellene un contacto")
        elif action_name=="Ver contactos":
            if self.listaContactos.lista.count()==0:
                self.mensaje_error("La lista esta vacia")
            else:
                self.mensaje("Cargando contactos")
                self.listaContactos.show()
                self.hide()
        elif action_name == "Eliminar contacto":
            if contacto:  # Obtiene el texto del QLineEdit
                items = self.listaContactos.lista.findItems(contacto, Qt.MatchExactly)  # Busca coincidencias exactas
                if items:  # Si encuentra el contacto
                    for item in items:
                        row = self.listaContactos.lista.row(item)
                        self.listaContactos.lista.takeItem(row)  # Borra el contacto que coincide con el texto
                    self.mensaje(f"Contacto '{contacto}' eliminado")
                    self.contactoInput.clear()
                else:
                    self.mensaje_error("El contacto no esta en la lista")
        else:
            self.mensaje_error("Rellene un contacto")
    def registroContacto(self):
        self.contactoInput.setEnabled(True)
    def mensaje(self,mensaje):
        QMessageBox.information(self,"Exito",mensaje)
    def mensaje_error(self,mensaje):
        QMessageBox.critical(self, "Error", mensaje)

class contactos(QMainWindow):
    def __init__(self,ventana_principal):
        super().__init__()
        self.setWindowTitle("Lista de Contactos")
        self.setGeometry(100,100,400,400)
        self.setContentsMargins(10,10,10,10)

        self.ventana_principal=ventana_principal

        self.layout_principal=QVBoxLayout()
        self.lista=QListWidget()
        self.layout_principal.addWidget(self.lista)
        self.lista.setFixedSize(200,200)

        self.btnAtras=QPushButton("Volver")
        self.layout_principal.addWidget(self.btnAtras)
        self.btnAtras.clicked.connect(self.volver)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(self.layout_principal)

    def volver(self):
        self.hide()
        self.ventana_principal.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    ventana=GestionContactos()
    ventana.show()
    app.exec()


