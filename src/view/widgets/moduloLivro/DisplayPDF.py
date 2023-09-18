import fitz as PyMuPDF
from PyQt6.QtWidgets import (
    QWidget,
    QFrame,
    QDialog,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QScrollArea
)
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QImage, QPixmap
from src.controller.telaPreviaLivro import setPagAtual, getPagAtual
from src.view.utils.imageTools import relHeight, relWidth
from src.view.utils.container import verticalFrame, horizontalFrame


class DisplayPDF(QScrollArea):
    def __init__(self, parent: QWidget | QFrame | QDialog, objectName: str = ""):
        super().__init__()

        # ATRIBUTOS -----------------------------------
        self.paginaAtual = QLabel()
        self.paginaAtual.setAlignment(Qt.AlignmentFlag.AlignHCenter)


        # CONFIGURAÇÕES ------------------------------
        self.setParent(parent)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setObjectName(objectName)
        self.setStyleSheet("background-color: #4d4d4d;")
        self.setWidgetResizable(True)

        # WIDGET CENTRAL ----------------------------
        self.widgetCentral = verticalFrame(self, "widgetCentral")
        self.setWidget(self.widgetCentral)

        self.widgetCentral.layout().setContentsMargins(0, 0, 0, 0)
        self.widgetCentral.layout().setSpacing(0)

        # DEFININDO PÁGINA --------------------------------
        self.widgetCentral.layout().addWidget(self.paginaAtual)


    # MÉTODOS ------------------------------------------

    def definirPagina(self, pixmap):
        self.paginaAtual.setPixmap(pixmap)
