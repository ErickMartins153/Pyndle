from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QLabel,
    QPushButton,
    QSpacerItem
)
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import Qt, pyqtSignal
from src.view.widgets.moduloLivro.Popup import Popup
from src.controller.telaPreviaLivro import dadosLivro
from src.controller.telaInicial import dadosUsuario
from src.controller.telaPrincipal import adicionarlivrosPessoais
from src.view.utils.imageTools import getResizedImage, relHeight, relWidth
from src.view.utils import widgetSearch
from src.view.utils.container import verticalFrame

class PopupCatalogo(QDialog):
    # Sinais
    sinalLivroAdicionado = pyqtSignal()

    def __init__(self, nomeUsuario: str, idLivro: int, parent):
        """
        PopUp utilizado para obter informações de livros do catálogo
        e adicioná-los a biblioteca pessoal
        :param nomeUsuario: Nome do usuário que está vizualizando o PopUp
        :param idLivro: ID do livro que está sendo exposto
        :param parent: widget o qual o PopUp está recl
        """
        super().__init__()

        # ATRIBUTOS ----------------------------------------------
        self.idLivro = idLivro
        self.nomeUsuario = nomeUsuario
        self.idUsuario = dadosUsuario(nomeUsuario)["idUsuario"]
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
        self.qtdPaginas = self.dadosLivro["pagTotal"]


        # CONFIGURAÇÕES -------------------------------------------

        self.setStyleSheet(open("src/view/assets/styles/popup.css").read())
        self.setWindowTitle(self.titulo)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setFixedSize(relWidth(550, 1366), relHeight(450, 768))
        self.setWindowFlag(Qt.WindowType.Window, False)
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowType.CustomizeWindowHint, True)
        self.setWindowFlag(Qt.WindowType.WindowTitleHint, False)


        # LAYOUT ------------------------------------------------------------
        layout = QHBoxLayout()
        layout.setObjectName("fundo")
        self.setLayout(layout)


        # CONTAINER (Grupo com botão de adicionar e capa) -----------------------------

        groupImagemBotao = verticalFrame(self)
        groupImagemBotao.setObjectName("groupImagemBotao")
        layout.addWidget(groupImagemBotao)

        groupImagemBotao.layout().setObjectName("ImagemBotaoLayout")
        groupImagemBotao.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        groupImagemBotao.setLayout(groupImagemBotao.layout())


        # CAPA DO LIVRO --------------------------------------------------------------

        imagemCapaLivro = QImage.fromData(self.capaLivro)
        capa = QLabel(self)
        capa.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap.fromImage(imagemCapaLivro)
        capa.setPixmap(pixmap)
        groupImagemBotao.layout().addWidget(capa, alignment=Qt.AlignmentFlag.AlignCenter)


        # SPACER --------------------------------------------------------------------

        spacer = QSpacerItem(0, relHeight(50, 1080))
        groupImagemBotao.layout().addSpacerItem(spacer)


        # BOTÃO DE ADICIONAR NA BIBLIOTECA ------------------------------------------

        containerBotaoAdicionar = QVBoxLayout()
        containerBotaoAdicionar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        groupImagemBotao.layout().addLayout(containerBotaoAdicionar)

        AdicionarBibliotecaBotao = QPushButton(groupImagemBotao)
        AdicionarBibliotecaBotao.setObjectName("lerLivroBotao")
        AdicionarBibliotecaBotao.setText("Adicionar livro")
        AdicionarBibliotecaBotao.clicked.connect(self.adicionarBiblioteca)
        containerBotaoAdicionar.addWidget(AdicionarBibliotecaBotao)


        # CONTAINER (Onde fica botão de fechar e metadados) --------------------------

        groupInfos = verticalFrame(self)
        groupInfos.setObjectName("groupTexto")
        layout.addWidget(groupInfos)

        groupInfos.layout().setObjectName("infosLayout")
        groupInfos.setLayout(groupInfos.layout())


        # CONTAINER (Grupo com os labels de metadados) ------------------------------
        groupMetadado = verticalFrame(groupInfos)
        groupMetadado.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
        groupMetadado.layout().setSpacing(50)
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
        tituloLabel.setMaximumHeight(20)
        groupMetadado.layout().addWidget(tituloLabel)

        # Mostrar gênero
        generoLabel = QLabel(f"Gênero: {self.genero}")
        generoLabel.setObjectName("info")
        generoLabel.setMaximumHeight(20)
        groupMetadado.layout().addWidget(generoLabel)

        # Mostrar autor
        autorLabel = QLabel(f"Autor: {self.autor}")
        autorLabel.setMaximumHeight(20)
        autorLabel.setObjectName("info")
        groupMetadado.layout().addWidget(autorLabel)

        # Mostrar ano
        anoLabel = QLabel(f"Ano: {self.anoPublicacao}")
        anoLabel.setMaximumHeight(20)
        anoLabel.setObjectName("info")
        groupMetadado.layout().addWidget(anoLabel)

        # Mostrar quantidade de páginas
        qtdPaginasLabel = QLabel(f"Total de páginas: {self.qtdPaginas}")
        qtdPaginasLabel.setMaximumHeight(20)
        qtdPaginasLabel.setObjectName("info")
        groupMetadado.layout().addWidget(qtdPaginasLabel)


        # BOTÃO DE FECHAR ---------------------------------------------------------
        layoutBotaoFechar = verticalFrame(groupInfos)
        layoutBotaoFechar.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        groupInfos.layout().addWidget(layoutBotaoFechar)

        botaoFechar = QPushButton("Fechar", self)
        botaoFechar.clicked.connect(self.accept)
        layoutBotaoFechar.layout().addWidget(botaoFechar)

        # DEFININDO PROPORÇÃO DO CONTAINER DE METADADOS ---------------------------
        groupInfos.layout().setStretch(0, 60)
        groupInfos.layout().setStretch(1, 20)


    # (MÉTODOS) ------------------------------------------------------------------


    def adicionarBiblioteca(self):
        """
        Adiciona o livro correspondente do PopUp na biblioteca pessoal do usuário atual
        """

        # Criando relação entre usuário e livro
        adicionarlivrosPessoais(self.idUsuario, self.idLivro)
        self.hide()

        # Abre PopUp de "Minha Biblioteca"
        popUpBiblioteca = Popup(self.nomeUsuario, self.idLivro, self)
        # Quando o livro for apagado, manda sinal para atualizar a dashboard
        try:
            popUpBiblioteca.sinalLivroApagado.connect(self.parent.atualizarLivros)
        except AttributeError:
            pass

        #Emite sinal que o livro foi adicionado para atualizar a dashboard
        self.sinalLivroAdicionado.emit()
        popUpBiblioteca.exec()
        self.close()
