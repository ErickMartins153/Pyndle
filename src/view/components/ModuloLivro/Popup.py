from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QLabel,
    QPushButton,
    QMessageBox,
    QSpacerItem,
    QSizePolicy,
)
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import Qt
from src.view.components.ModuloLivro.LeitorPDF import LeitorPDF
from src.controller.telaPreviaLivro import dadosLivro
from src.view.components.ModuloLivro.Grafico import Grafico


class Popup(QDialog):
    def __init__(self, idLivro):
        super().__init__()
        self.setStyleSheet(open("src/view/assets/styles/popup.css").read())
        self.dadosLivro = dadosLivro(idLivro)
        self.titulo = self.dadosLivro[1]
        self.genero = self.dadosLivro[2]
        self.autor = self.dadosLivro[3]
        self.anoPublicacao = self.dadosLivro[4]
        self.capaLivro = self.dadosLivro[5]
        self.arquivoPDF = self.dadosLivro[6]
        self.qtdPaginasLabel = self.dadosLivro[7]
        self.setWindowTitle(self.titulo)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setFixedSize(700, 700)
        self.setWindowFlag(Qt.WindowType.Window, False)
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)

        layout = QHBoxLayout()
        layout.setObjectName("fundo")
        self.setLayout(layout)

        groupImagemBotao = QFrame(self)
        groupImagemBotao.setObjectName("groupImagemBotao")
        groupImagemBotao.setFixedSize(300, 610)
        layout.addWidget(groupImagemBotao)

        ImagemBotaoLayout = QVBoxLayout()
        ImagemBotaoLayout.setObjectName("ImagemBotaoLayout")
        ImagemBotaoLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        groupImagemBotao.setLayout(ImagemBotaoLayout)

        imagemCapaLivro = QImage.fromData(self.capaLivro)
        capa = QLabel(self)
        pixmap = QPixmap.fromImage(imagemCapaLivro)
        capa.setPixmap(pixmap)

        # colocar um espaço em cima e embaixo da capa, garantindo que ela fique no centro do frame
        ImagemBotaoLayout.addStretch()
        ImagemBotaoLayout.addWidget(capa, alignment=Qt.AlignmentFlag.AlignCenter)
        ImagemBotaoLayout.addStretch()

        lerLivroBotao = QPushButton(groupImagemBotao)
        lerLivroBotao.setObjectName("lerLivroBotao")
        lerLivroBotao.setText("Ler Livro")
        ImagemBotaoLayout.addWidget(lerLivroBotao)

        # Conectando o botão "Ler Livro" à função para abrir o leitor de PDF
        lerLivroBotao.clicked.connect(self.abrirLeitorPDF)

        groupInfos = QFrame(self)
        groupInfos.setObjectName("groupTexto")
        layout.addWidget(groupInfos)

        infosLayout = QVBoxLayout()
        infosLayout.setObjectName("infosLayout")
        groupInfos.setLayout(infosLayout)

        h1 = QLabel("Informações do livro")
        infosLayout.addWidget(h1)
        h1.setObjectName("h1")
        h1.setMaximumHeight(50)

        tituloLabel = QLabel(f"Titulo: {self.titulo}")
        tituloLabel.setObjectName("info")
        tituloLabel.setMaximumHeight(20)
        infosLayout.addWidget(tituloLabel)

        generoLabel = QLabel(f"Gênero: {self.genero}")
        generoLabel.setObjectName("info")
        generoLabel.setMaximumHeight(20)
        infosLayout.addWidget(generoLabel)

        autorLabel = QLabel(f"Autor: {self.autor}")
        autorLabel.setMaximumHeight(20)
        autorLabel.setObjectName("info")
        infosLayout.addWidget(autorLabel)

        anoLabel = QLabel(f"Ano: {self.anoPublicacao}")
        anoLabel.setMaximumHeight(20)
        anoLabel.setObjectName("info")
        infosLayout.addWidget(anoLabel)

        qtdPaginasLabel = QLabel(f"Total de páginas: {self.qtdPaginasLabel}")
        qtdPaginasLabel.setMaximumHeight(20)
        qtdPaginasLabel.setObjectName("info")
        infosLayout.addWidget(qtdPaginasLabel)

        avaliacaoLabel = QLabel(f"Avaliação: Placeholder")
        avaliacaoLabel.setMaximumHeight(20)
        avaliacaoLabel.setObjectName("info")
        infosLayout.addWidget(avaliacaoLabel)

        grafico = Grafico(50, 50, self)
        infosLayout.addWidget(grafico)

        button = QPushButton("Fechar", self)
        button.clicked.connect(self.accept)
        infosLayout.addWidget(button)
        self.setLayout(layout)

    def abrirLeitorPDF(self):
        if self.arquivoPDF:
            # Criando e mostrando o leitor de PDF
            leitor_pdf = LeitorPDF(self.arquivoPDF, self.titulo)
            leitor_pdf.exec()
        else:
            QMessageBox.critical(None, "Erro", "Esse livro não está disponível")
