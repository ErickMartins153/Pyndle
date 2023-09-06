from src.controller.telaPreviaLivro import dadosLivro
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QDialog,
    QFrame,
    QLabel,
)


class Popup(QDialog):
    def __init__(self, main_window, idLivro):
        super().__init__()
        self.dadosLivro = dadosLivro(idLivro)
        self.titulo = self.dadosLivro[1]
        self.genero = self.dadosLivro[2]
        self.autor = self.dadosLivro[3]
        self.anoPublicacao = self.dadosLivro[4]
        self.capaLivro = self.dadosLivro[5]
        self.arquivoPDF = self.dadosLivro[6]
        self.pagTotal = self.dadosLivro[7]
        self.setWindowTitle(self.titulo)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setFixedSize(700, 400)
        self.main_window = main_window

        layout = QHBoxLayout()
        layout.setObjectName("fundo")
        self.setLayout(layout)

        groupImagemBotao = QFrame(self)
        groupImagemBotao.setObjectName("groupImagemBotao")
        layout.addWidget(groupImagemBotao)

        ImagemBotaoLayout = QVBoxLayout()
        ImagemBotaoLayout.setObjectName("ImagemBotaoLayout")
        groupImagemBotao.setLayout(ImagemBotaoLayout)

        imagemCapaLivro = QImage.fromData(self.capaLivro)
        capa = QLabel(self)
        pixmap = QPixmap.fromImage(imagemCapaLivro)
        capa.setPixmap(pixmap)
        ImagemBotaoLayout.addWidget(capa)

        lerLivroBotao = QPushButton(groupImagemBotao)
        lerLivroBotao.setObjectName("lerLivroBotao")

        lerLivroBotao.setText("Ler Livro")
        ImagemBotaoLayout.addWidget(lerLivroBotao)

        groupTexto = QFrame(self)
        groupTexto.setObjectName("groupTexto")
        layout.addWidget(groupTexto)
        tituloLabel = QLabel(f"titulo: {self.titulo}")
        layout.addWidget(tituloLabel)
        generoLabel = QLabel(f"genero: {self.genero}")
        layout.addWidget(generoLabel)
        autorLabel = QLabel(f"autor: {self.autor}")
        layout.addWidget(autorLabel)

        button = QPushButton("Fechar Popup", self)
        button.clicked.connect(self.accept)

        layout.addWidget(button)
        self.setLayout(layout)
