from PySide6.QtCore import QTime, QTimer
from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLineEdit


#Crea una aplicación que implemente un cronómetro. Debe incluir botones para iniciar,
# pausar y reiniciar el cronómetro, y mostrar el tiempo transcurrido en formato mm:ss. (QTime


class Cronometro(QWidget):
    def __init__(self):
        super().__init__()
        
        #Configuracion interfaz
        self.setWindowTitle("Cronometro")
        self.setGeometry(200,200,150,300)
        
        #Layout principal
        self.layout_principal=QVBoxLayout()
        self.setLayout(self.layout_principal)

        # Pantalla para mostrar el tiempo
        self.pantalla=QLineEdit()
        self.pantalla.setReadOnly(True)
        self.layout_principal.addWidget(self.pantalla)

        # Botones
        self.btnIniciar=QPushButton("Iniciar")
        self.layout_principal.addWidget(self.btnIniciar)

        self.btnPausar=QPushButton("Pausar")
        self.layout_principal.addWidget(self.btnPausar)

        self.btnReiniciar=QPushButton("Reiniciar")
        self.layout_principal.addWidget(self.btnReiniciar)

        # Conexión de botones
        self.btnIniciar.clicked.connect(self.iniciar)
        self.btnPausar.clicked.connect(self.pausar)
        self.btnReiniciar.clicked.connect(self.reiniciar)

        # Temporizador
        self.temporizador=QTimer(self)
        self.temporizador.timeout.connect(self.actualizar)

        # Variable para almacenar el tiempo de inicio
        self.start_time = None

    def iniciar(self):
        self.start_time=QTime.currentTime()  # Almacena el tiempo de inicio
        self.temporizador.start(1000)  # Actualización cada segundo

    def pausar(self):
        self.temporizador.stop()

    def reiniciar(self):
        self.temporizador.stop()
        self.start_time=None
        self.pantalla.setText("00:00")

    def actualizar(self):
        if self.start_time:  # Verifica si se ha iniciado el cronómetro
            tiempo_actual = QTime.currentTime()
            segundos_transcurridos = self.start_time.secsTo(tiempo_actual)  # Calcula la diferencia en segundos

            minutos = segundos_transcurridos // 60
            segundos = segundos_transcurridos % 60

            # Muestra el tiempo en formato mm:ss
            self.pantalla.setText(f"{minutos:02}:{segundos:02}")
        
if __name__== "__main__":
    app=QApplication([])
    ventana=Cronometro()
    ventana.show()
    app.exec()