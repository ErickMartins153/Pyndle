from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QFrame, QLabel, QPushButton, QMessageBox
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import Qt
from src.view.components.ModuloLivro.LeitorPDF import LeitorPDF
from src.controller.telaPreviaLivro import dadosLivro

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
        self.pagTotal = self.dadosLivro[7]
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
        h1.setMaximumHeight(32)

        tituloLabel = QLabel(f"titulo: {self.titulo}")
        tituloLabel.setObjectName("info")
        tituloLabel.setMaximumHeight(16)
        infosLayout.addWidget(tituloLabel)

        generoLabel = QLabel(f"genero: {self.genero}")
        generoLabel.setObjectName("info")
        generoLabel.setMaximumHeight(16)
        infosLayout.addWidget(generoLabel)

        autorLabel = QLabel(f"autor: {self.autor}")
        autorLabel.setMaximumHeight(16)
        autorLabel.setObjectName("info")
        infosLayout.addWidget(autorLabel)

        button = QPushButton("Fechar", self)
        button.clicked.connect(self.accept)
        infosLayout.addWidget(button)
        self.setLayout(layout)

        self.leitor_pdf = None

    def abrirLeitorPDF(self):
      if self.arquivoPDF:
        # Criando e mostrando o leitor de PDF com o caminho do PDF
        leitor_pdf = LeitorPDF(self.arquivoPDF)
        leitor_pdf.exec()
      else:
        QMessageBox.critical(None, "Erro", "Nenhum arquivo PDF especificado")
