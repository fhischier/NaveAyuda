import os
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

# ---------------- CONFIG ----------------
COLOR_FONDO = "#0f172a"
COLOR_BOTON = "#2563eb"
COLOR_HOVER = "#1d4ed8"
COLOR_TEXTO = "white"

# ---------------- PATH ----------------
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# ---------------- PREGUNTAS ----------------
PREGUNTAS = [
    {"pregunta": "¿Quien es el dueño Clamers?", "opciones": ["German", "Ioio", "Nari"], "correcta": 0},
    {"pregunta": "¿Cuanto paga Clamers?", "opciones": ["Bien", "Poco", "Mucho"], "correcta": 1},
    {"pregunta": "¿Quien es el mas gordo?", "opciones": ["German", "Ioio", "Nari"], "correcta": 0},
]

# ---------------- ESTILO BOTON ----------------
def estilo_boton():
    return f"""
    QPushButton {{
        background-color: {COLOR_BOTON};
        color: {COLOR_TEXTO};
        border-radius: 20px;
        font-size: 28px;
        padding: 25px;
    }}
    QPushButton:hover {{
        background-color: {COLOR_HOVER};
    }}
    """

# ---------------- ROTACIÓN ----------------
class RotatedWidget(QGraphicsView):
    def __init__(self, widget):
        super().__init__()

        self.setFrameShape(QFrame.NoFrame)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        scene = QGraphicsScene()
        self.setScene(scene)

        self.proxy = QGraphicsProxyWidget()
        self.proxy.setWidget(widget)
        scene.addItem(self.proxy)

        # 🔥 ROTAR 90°
        self.proxy.setTransformOriginPoint(self.proxy.boundingRect().center())
        self.proxy.setRotation(90)

        self.setStyleSheet("background:black;")

# ---------------- BASE ----------------
class BaseWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet(f"background-color: {COLOR_FONDO};")

        layout = QVBoxLayout(self)

        # BOTÓN CERRAR
        top = QHBoxLayout()
        top.addStretch()

        cerrar = QPushButton("X")
        cerrar.setFixedSize(50, 50)
        cerrar.clicked.connect(QApplication.quit)
        cerrar.setStyleSheet("""
            QPushButton {
                background-color: red;
                color: white;
                border-radius: 25px;
                font-weight: bold;
            }
        """)

        top.addWidget(cerrar)
        layout.addLayout(top)

        self.main_layout = layout

# ---------------- INICIO ----------------
class Inicio(BaseWidget):
    def __init__(self):
        super().__init__()

        self.imagen = QLabel()
        self.imagen.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap(resource_path("assets/Logo_Clamers_Blanco.png")).scaled(720,1080,Qt.KeepAspectRatio)
        self.imagen.setPixmap(pixmap)

        self.titulo = QLabel("TRIVIA")
        self.titulo.setAlignment(Qt.AlignCenter)
        self.titulo.setFont(QFont("Arial", 70, QFont.Bold))
        self.titulo.setStyleSheet(f"color:{COLOR_TEXTO}")

        self.btn = QPushButton("INICIAR")
        self.btn.setStyleSheet(estilo_boton())
        self.btn.clicked.connect(self.start)

        self.main_layout.addWidget(self.imagen)
        self.main_layout.addWidget(self.titulo)
        self.main_layout.addWidget(self.btn)

        # ANIMACIÓN
        self.y = 0
        self.dir = 1
        self.timer = QTimer()
        self.timer.timeout.connect(self.animar)
        self.timer.start(16)

    def animar(self):
        self.y += self.dir
        if abs(self.y) > 20:
            self.dir *= -1
        self.imagen.move(self.imagen.x(), self.y)

    def start(self):
        self.juego = Juego(self)
        self.juego.show()
        self.hide()

# ---------------- JUEGO ----------------
class Juego(BaseWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.index = 0
        self.correctas = 0
        self.incorrectas = 0

        self.pregunta = QLabel()
        self.pregunta.setAlignment(Qt.AlignCenter)
        self.pregunta.setWordWrap(True)
        self.pregunta.setFont(QFont("Arial", 50, QFont.Bold))
        self.pregunta.setStyleSheet(f"color:{COLOR_TEXTO}")

        self.main_layout.addWidget(self.pregunta)

        self.botones = []
        for i in range(3):
            b = QPushButton()
            b.setStyleSheet(estilo_boton())

            # 🔥 EVITA QUE SE ACHIQUEN
            b.setMinimumHeight(120)
            b.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

            b.clicked.connect(lambda _, x=i: self.verificar(x))
            self.main_layout.addWidget(b)
            self.botones.append(b)

        self.cargar()

    def cargar(self):
        p = PREGUNTAS[self.index]
        self.pregunta.setText(p["pregunta"])

        for i, op in enumerate(p["opciones"]):
            self.botones[i].setText(op)
            self.botones[i].setEnabled(True)
            self.botones[i].setStyleSheet(estilo_boton())

    def verificar(self, seleccion):
        correcta = PREGUNTAS[self.index]["correcta"]

        if seleccion == correcta:
            self.botones[seleccion].setStyleSheet(
                "background-color: green; color:white; border-radius:20px; padding:25px;"
            )
            self.correctas += 1
        else:
            self.botones[seleccion].setStyleSheet(
                "background-color: red; color:white; border-radius:20px; padding:25px;"
            )
            self.incorrectas += 1

        for b in self.botones:
            b.setEnabled(False)

        QTimer.singleShot(1000, self.siguiente)

    def siguiente(self):
        self.index += 1
        if self.index < len(PREGUNTAS):
            self.cargar()
        else:
            self.fin = Resultado(self.correctas, self.incorrectas, self.parent)
            self.fin.show()
            self.close()

# ---------------- RESULTADO ----------------
class Resultado(BaseWidget):
    def __init__(self, c, i, inicio):
        super().__init__()
        self.inicio = inicio

        label = QLabel(f"Correctas: {c}\nIncorrectas: {i}")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont("Arial", 60, QFont.Bold))
        label.setStyleSheet(f"color:{COLOR_TEXTO}")

        btn = QPushButton("REINICIAR")
        btn.setStyleSheet(estilo_boton())
        btn.clicked.connect(self.reset)

        self.main_layout.addWidget(label)
        self.main_layout.addWidget(btn)

    def reset(self):
        self.inicio.index = 0
        self.inicio.correctas = 0
        self.inicio.incorrectas = 0

        self.inicio.show()
        self.close()

# ---------------- MAIN ----------------
if __name__ == "__main__":
    app = QApplication(sys.argv)

    inicio = Inicio()
    rotado = RotatedWidget(inicio)
    rotado.showFullScreen()

    sys.exit(app.exec())