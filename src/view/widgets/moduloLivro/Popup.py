from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QLabel,
    QPushButton,
    QMessageBox,
    QSpacerItem
)
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import Qt, pyqtSignal
from src.view.widgets.moduloLivro.LeitorPDF import LeitorPDF
from src.controller.telaPreviaLivro import dadosLivro, getPagAtual
from src.controller.telaInicial import dadosUsuario
from src.view.widgets.moduloLivro.Grafico import Grafico
from src.view.components.BotaoAvaliacao import BotaoAvaliacao
from src.controller.telaPreviaLivro import salvarAvaliacao, pegarAvaliacao
from src.view.utils.imageTools import getResizedImage, relHeight, relWidth
from src.view.utils.container import verticalFrame
from src.controller.telaPrincipal import apagarLivro

class Popup(QDialog):
    # Sinais
    sinalLivroApagado = pyqtSignal()

    def __init__(self, nomeUsuario: str, idLivro: int, parent):
        super().__init__()
        # ATRIBUTOS ----------------------------------------------
        self.idUsuario = dadosUsuario(nomeUsuario)["idUsuario"]
        self.idLivro = idLivro
        self.parent = parent
        self.dadosLivro = dadosLivro(idLivro)
        self.titulo = self.dadosLivro["titulo"]
        self.genero = self.dadosLivro["genero"]
        self.autor = self.dadosLivro["autor"]
        self.anoPublicacao = self.dadosLivro["anoPublicacao"]
        self.capaLivro = getResizedImage(
            self.dadosLivro["capaLivro"], relWidth(280, 1920), relHeight(392, 1080)
        )
        self.arquivoPDF = self.dadosLivro["arquivoPdf"]
        self.lido = getPagAtual(self.idLivro, self.idUsuario)
        self.qtdPaginas = self.dadosLivro["pagTotal"]
        self.porcentagemLido = self.lido / self.qtdPaginas * 100

        # CONFIGURAÇÕES -------------------------------------------

        self.setStyleSheet(open("src/view/assets/styles/popup.css").read())
        self.setWindowFlag(Qt.WindowType.CustomizeWindowHint, True)
        self.setWindowFlag(Qt.WindowType.WindowTitleHint, False)
        self.setFixedSize(relWidth(550, 1366), relHeight(450, 768))

        # LAYOUT ---------------------------------------------------------
        layout = QHBoxLayout()
        layout.setObjectName("fundo")
        self.setLayout(layout)


        # CONTAINER (Grupo com botão de ler, apagar e capa) -----------------------------
        groupImagemBotao = verticalFrame(self)
        groupImagemBotao.setMinimumWidth(relWidth(275, 1366))
        groupImagemBotao.setObjectName("groupImagemBotao")
        layout.addWidget(groupImagemBotao)

        groupImagemBotao.layout().setObjectName("ImagemBotaoLayout")
        groupImagemBotao.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        groupImagemBotao.setLayout(groupImagemBotao.layout())

        # SPACER ----------------------------------------------------------------------

        spacer = QSpacerItem(0, relHeight(50, 1080))
        groupImagemBotao.layout().addSpacerItem(spacer)


        # CAPA DO LIVRO --------------------------------------------------------------

        imagemCapaLivro = QImage.fromData(self.capaLivro)
        capa = QLabel(self)
        pixmap = QPixmap.fromImage(imagemCapaLivro)
        capa.setPixmap(pixmap)
        groupImagemBotao.layout().addWidget(capa, alignment=Qt.AlignmentFlag.AlignHCenter)

        # SPACER ----------------------------------------------------------------------

        spacer = QSpacerItem(0, relHeight(50, 1080))
        groupImagemBotao.layout().addSpacerItem(spacer)


        # CONTAINER BOTÕES ------------------------------------------------------------

        containerBotoes = QVBoxLayout()
        containerBotoes.setAlignment(Qt.AlignmentFlag.AlignCenter)
        groupImagemBotao.layout().addLayout(containerBotoes)


        # BOTÃO DE LER LIVRO ------------------------------------------

        lerLivroBotao = QPushButton(groupImagemBotao)
        lerLivroBotao.setObjectName("lerLivroBotao")
        lerLivroBotao.setText("Ler Livro")
        containerBotoes.addWidget(lerLivroBotao)

        # Conectando o botão "Ler Livro" à função para abrir o leitor de PDF
        lerLivroBotao.clicked.connect(self.abrirLeitorPDF)


        # BOTÃO DE APAGAR LIVRO ---------------------------------------

        apagarLivroBotao = QPushButton(groupImagemBotao)
        apagarLivroBotao.setObjectName("apagarLivroBotao")
        apagarLivroBotao.setText("Apagar Livro")
        apagarLivroBotao.clicked.connect(self.deletarLivro)
        containerBotoes.addWidget(apagarLivroBotao)

        # CONTAINER (Onde fica botão de fechar e metadados) --------------------------

        groupInfos = verticalFrame(self)
        groupInfos.setObjectName("groupTexto")
        layout.addWidget(groupInfos)

        groupInfos.layout().setObjectName("infosLayout")
        groupInfos.setLayout(groupInfos.layout())

        # CONTAINER (Grupo com os labels de metadados) ------------------------------

        groupMetadado = verticalFrame(groupInfos)
        groupMetadado.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
        groupMetadado.layout().setSpacing(10)
        groupInfos.layout().addWidget(groupMetadado)


        # LABEL (Informações do livro) ----------------------------------------------

        h1 = QLabel("Informações do livro")
        h1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        groupMetadado.layout().addWidget(h1)
        h1.setObjectName("h1")
        h1.setMaximumHeight(50)

        # METADADOS DO PDF ----------------------------------------------------------

        # Mostrar título
        tituloLabel = QLabel(f"Titulo: {self.titulo}")
        tituloLabel.setObjectName("info")
        tituloLabel.setMaximumHeight(relHeight(20, 1080))
        groupMetadado.layout().addWidget(tituloLabel)

        # Mostrar gênero
        generoLabel = QLabel(f"Gênero: {self.genero}")
        generoLabel.setObjectName("info")
        generoLabel.setMaximumHeight(relHeight(20, 1080))
        groupMetadado.layout().addWidget(generoLabel)

        # Mostrar autor
        autorLabel = QLabel(f"Autor: {self.autor}")
        autorLabel.setMaximumHeight(relHeight(20, 1080))
        autorLabel.setObjectName("info")
        groupMetadado.layout().addWidget(autorLabel)

        # Mostrar ano
        anoLabel = QLabel(f"Ano: {self.anoPublicacao}")
        anoLabel.setMaximumHeight(relHeight(20, 1080))
        anoLabel.setObjectName("info")
        groupMetadado.layout().addWidget(anoLabel)

        # Mostrar quantidade de páginas
        qtdPaginasLabel = QLabel(f"Total de páginas: {self.qtdPaginas}")
        qtdPaginasLabel.setMaximumHeight(relHeight(20, 1080))
        qtdPaginasLabel.setObjectName("info")
        groupMetadado.layout().addWidget(qtdPaginasLabel)

        # Mostrar avaliação
        avaliacaoLabel = QLabel(f"Avaliação:")
        avaliacaoLabel.setMaximumHeight(relHeight(20, 1080))
        avaliacaoLabel.setObjectName("info")
        groupMetadado.layout().addWidget(avaliacaoLabel)

        botaoAvaliacao = BotaoAvaliacao(self.getAvaliacao())
        botaoAvaliacao.mudancaAvaliacao.connect(self.armazenarAvaliacao)
        botaoAvaliacao.setObjectName("estrela")
        groupMetadado.layout().addLayout(botaoAvaliacao)


        # GRÁFICO ---------------------------------------------------------------------

        layoutGrafico = QVBoxLayout()
        layoutGrafico.setAlignment(Qt.AlignmentFlag.AlignCenter)
        groupInfos.layout().addLayout(layoutGrafico)

        self.grafico = Grafico(self.porcentagemLido, 100 - self.porcentagemLido, self)
        layoutGrafico.addWidget(self.grafico)


        # BOTÃO DE FECHAR -------------------------------------------------------------

        layoutBotaoFechar = QVBoxLayout()
        layoutBotaoFechar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        groupInfos.layout().addLayout(layoutBotaoFechar)

        botaoFechar = QPushButton("Fechar", self)
        botaoFechar.clicked.connect(self.accept)
        layoutBotaoFechar.addWidget(botaoFechar)


        # DEFININDO PROPORÇÃO DO CONTAINER DE METADADOS ---------------------------
        groupInfos.layout().setStretch(0, 60)
        groupInfos.layout().setStretch(1, 20)


    # MÉTODOS ---------------------------------------------------------

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
            # Apaga o livro e a relação de pyndle.db
            apagarLivro(self.idLivro, self.idUsuario)

            # Emite o sinal de que o livro foi apagado
            self.sinalLivroApagado.emit()

            self.accept()

        else:
            self.accept()
