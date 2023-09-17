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
from src.view.widgets.moduloLivro.LeitorPDF import LeitorPDF
from src.controller.telaPreviaLivro import dadosLivro, getPagAtual
from src.controller.telaInicial import dadosUsuario
from src.view.widgets.moduloLivro.Grafico import Grafico
from src.view.components.BotaoAvaliacao import BotaoAvaliacao
from src.controller.telaPreviaLivro import salvarAvaliacao, pegarAvaliacao
from src.view.utils.imageTools import getResizedImage, relHeight, relWidth


class Popup(QDialog):
    def __init__(self, nomeUsuario: str, idLivro: int, parent):
        super().__init__()
        # atributos ----------------
        self.idUsuario = dadosUsuario(nomeUsuario)["idUsuario"]
        self.idLivro = idLivro
        self.parent = parent
        self.atualizarLivrosPainel()
        self.dadosLivro = dadosLivro(idLivro)
        self.titulo = self.dadosLivro["titulo"]
        self.genero = self.dadosLivro["genero"]
        self.autor = self.dadosLivro["autor"]
        self.anoPublicacao = self.dadosLivro["anoPublicacao"]
        self.capaLivro = getResizedImage(
            self.dadosLivro["capaLivro"], relWidth(340, 1920), relHeight(476, 1080)
        )
        self.arquivoPDF = self.dadosLivro["arquivoPdf"]
        self.lido = getPagAtual(self.idLivro, self.idUsuario)
        self.qtdPaginas = self.dadosLivro["pagTotal"]
        self.porcentagemLido = self.lido / self.qtdPaginas * 100

        self.setStyleSheet(open("src/view/assets/styles/popup.css").read())
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
        groupImagemBotao.setFixedSize(300, 660)
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

        apagarLivroBotao = QPushButton(groupImagemBotao)
        apagarLivroBotao.setObjectName("apagarLivroBotao")
        apagarLivroBotao.setText("Apagar Livro")
        apagarLivroBotao.clicked.connect(self.deletarLivro)
        ImagemBotaoLayout.addWidget(apagarLivroBotao)

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

        avaliacaoLabel = QLabel(f"Avaliação:")
        avaliacaoLabel.setMaximumHeight(20)
        avaliacaoLabel.setObjectName("info")
        infosLayout.addWidget(avaliacaoLabel)

        botaoAvaliacao = BotaoAvaliacao(self.getAvaliacao())
        botaoAvaliacao.mudancaAvaliacao.connect(self.armazenarAvaliacao)
        botaoAvaliacao.setObjectName("estrela")
        infosLayout.addLayout(botaoAvaliacao)

        self.grafico = Grafico(self.porcentagemLido, 100 - self.porcentagemLido, self)
        infosLayout.addWidget(self.grafico)

        botaoFechar = QPushButton("Fechar", self)
        botaoFechar.clicked.connect(self.accept)
        infosLayout.addWidget(botaoFechar)
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

    def armazenarAvaliacao(self, avaliacaoAtual):
        self.avaliacaoAtual = avaliacaoAtual
        salvarAvaliacao(self.idUsuario, self.idLivro, self.avaliacaoAtual)

    def getAvaliacao(self):
        avaliacao = pegarAvaliacao(self.idLivro, self.idUsuario)
        if avaliacao:
            return avaliacao
        return 0

    def deletarLivro(self):
        caixaConfirmacao = QMessageBox(self)
        caixaConfirmacao.setIcon(QMessageBox.Icon.Question)
        caixaConfirmacao.setText(
            f"Você tem certeza que deseja apagar o livro '{self.titulo}'?"
        )
        botaoSim = caixaConfirmacao.addButton(
            "Sim, continuar", QMessageBox.ButtonRole.YesRole
        )
        botaoSim.setStyleSheet(
            """
            QPushButton{
                background-color: rgb(252, 16, 16);
            }
            QPushButton:hover{  
            background-color: rgb(182, 1, 1);
            font-weight: bolder;}
            """
        )
        caixaConfirmacao.addButton("Não, cancelar", QMessageBox.ButtonRole.NoRole)
        caixaConfirmacao.exec()

        if caixaConfirmacao.clickedButton() == botaoSim:
            # apagarLivro(self.idLivro, self.idUsuario)
            self.atualizarLivrosPainel()

            self.accept()

        else:
            print("nao deletou")

    def atualizarLivrosPainel(self):
        pass
        # fundoDashboard = getIrmaos(self.parent)["fundoDashboard"]
        # fundoDashboard.resizeEvent(None)
