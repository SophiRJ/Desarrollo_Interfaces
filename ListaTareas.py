from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QLineEdit, QPushButton, QPointList, QListWidget, \
    QMessageBox


#Crea una aplicación que permita agregar tareas a una lista.
# El usuario puede escribir una tarea en un
#cuadro de texto y agregarla a un área de texto más grande
# que muestra todas las tareas acumuladas.

class ListaTareas(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lista Tareas")
        self.setGeometry(400,200,200,200)

        self.layout_principal=QVBoxLayout()
        self.setLayout(self.layout_principal)

        #Tarea
        self.tarea = QLineEdit()
        self.tarea.setPlaceholderText("Tarea")
        self.layout_principal.addWidget(self.tarea)

        #Boton
        self.boton=QPushButton()
        self.boton.setText("Añadir")
        self.layout_principal.addWidget(self.boton)

        #Lista
        self.lista=QListWidget()
        self.layout_principal.addWidget(self.lista)

        self.boton.clicked.connect(lambda : self.aniadir_lista())

    def aniadir_lista(self):
        tarea=self.tarea.text()
        if tarea:
            self.lista.addItem(tarea)
            self.tarea.clear()
        else:
            QMessageBox.warning(self,"Advertencia","Rellena el campo")

if __name__=="__main__":
    app=QApplication([])
    ventana=ListaTareas()
    ventana.show()
    app.exec()
