from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QLabel,
    QPushButton,
    QMessageBox,
)
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import Qt
from src.view.components.ModuloLivro.LeitorPDF import LeitorPDF
from src.controller.telaPreviaLivro import dadosLivro, getPagAtual
from src.controller.telaInicial import dadosUsuario
from src.view.components.ModuloLivro.Grafico import Grafico


class Popup(QDialog):
    def __init__(self, nomeUsuario, idLivro):
        super().__init__()
        self.setStyleSheet(open("src/view/assets/styles/popup.css").read())
        self.idUsuario = dadosUsuario(nomeUsuario)["idUsuario"]
        self.idLivro = idLivro
        self.dadosLivro = dadosLivro(idLivro)

        self.titulo = self.dadosLivro["titulo"]
        self.genero = self.dadosLivro["genero"]
        self.autor = self.dadosLivro["autor"]
        self.anoPublicacao = self.dadosLivro["anoPublicacao"]
        self.capaLivro = self.dadosLivro["capaLivro"]
        self.arquivoPDF = self.dadosLivro["arquivoPdf"]

        self.lido = getPagAtual(self.idLivro, self.idUsuario)
        self.qtdPaginas = self.dadosLivro["pagTotal"]
        self.porcentagemLido = self.lido / self.qtdPaginas * 100

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

        qtdPaginasLabel = QLabel(f"Total de páginas: {self.qtdPaginas}")
        qtdPaginasLabel.setMaximumHeight(20)
        qtdPaginasLabel.setObjectName("info")
        infosLayout.addWidget(qtdPaginasLabel)

        avaliacaoLabel = QLabel(f"Avaliação: Placeholder")
        avaliacaoLabel.setMaximumHeight(20)
        avaliacaoLabel.setObjectName("info")
        infosLayout.addWidget(avaliacaoLabel)

        self.grafico = Grafico(self.porcentagemLido, 100 - self.porcentagemLido, self)
        infosLayout.addWidget(self.grafico)

        button = QPushButton("Fechar", self)
        button.clicked.connect(self.accept)
        infosLayout.addWidget(button)
        self.setLayout(layout)

    def abrirLeitorPDF(self):
        if self.arquivoPDF:
            # Criando e mostrando o leitor de PDF
            leitorPdf = LeitorPDF(
                self.idUsuario, self.idLivro, self.arquivoPDF, self.titulo, self
            )
            leitorPdf.sinalPaginaAtual.connect(self.updateGrafico)
            leitorPdf.exec()
        else:
            QMessageBox.critical(self, "Erro", "Esse livro não está disponível")

    def updateGrafico(self, paginaAtual):
        self.porcentagemLido = paginaAtual / self.qtdPaginas * 100
        self.grafico.atualizar(self.porcentagemLido, 100 - self.porcentagemLido)
