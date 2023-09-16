from PyQt6 import QtWidgets, QtGui
from src.controller.telaPrincipal import filtrarCatalogo
from src.view.components.BotaoImagem import BotaoImagem
from src.view.utils import widgetSearch
from src.view.utils.imageTools import relHeight, relWidth
from src.view.components.catalogo.subcomponents.popupCatalogo import PopupCatalogo


class PainelLivros(QtWidgets.QScrollArea):
    # noinspection PyTypeChecker
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()
        # Atributos
        self.listaBotaoLivro = list()  # Lista para acessar os BotoesLivros em métodos

        # Configurações
        self.setParent(parent)
        self.setStyleSheet(
            open(
                "src/view/assets/styles/catalagoEMinhaBiblioteca/painelLivros.css"
            ).read()
        )
        self.setWidgetResizable(True)
        self.setContentsMargins(0, 0, 0, 0)
        self.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)

        # Central widget
        self.contentWidget = QtWidgets.QWidget(self)
        self.contentWidget.setObjectName("contentWidget")

        self.setWidget(self.contentWidget)

        # Definindo Layout
        self.painelLivrosLayout = QtWidgets.QGridLayout()
        self.painelLivrosLayout.setSpacing(relHeight(40, 1080))
        self.contentWidget.setLayout(self.painelLivrosLayout)

        # Definindo livros
        self.getLivrosCatalogo()
        self.resizeEvent(None)

    def resizeEvent(self, a0: QtGui.QResizeEvent = QtGui.QResizeEvent) -> None:
        super().resizeEvent(a0)
        mainWindow = widgetSearch.getAncestrais(self)[
            "mainWindow"
        ]  # mainWindow para identificar redimensionamentos

        # Redimensionamento dos livros
        if mainWindow.width() >= relWidth(
            1640, 1920
        ):  # Redimensiona de acordo com o tamanho da janela
            self.displayBotoesLivros(4, relWidth(240, 1920), relHeight(336, 1080))
        else:
            self.displayBotoesLivros(3, relWidth(200, 1920), relHeight(280, 1080))

    def displayBotoesLivros(self, quantColunas: int, width: int, height: int):
        """
        Adiciona os livros ao Painel de Livros
        :param quantColunas: Define a quantidade de colunas em que serão dispostos
        :param width: define a largura dos botões
        :param height: define a altura dos botões
        """
        # Limpar o layout atual

        linha, coluna = 0, 0
        for botaoImagem in self.listaBotaoLivro:
            botaoImagem.resizeButton(width, height)
            self.painelLivrosLayout.addWidget(botaoImagem, linha, coluna)

            coluna += 1

            if coluna == quantColunas:
                coluna = 0
                linha += 1

    def getLivrosCatalogo(self, genero: str = None, ordemAlfabetica: bool = None):
        livrosCatalogoBD = filtrarCatalogo(genero, ordemAlfabetica)

        for botao in self.listaBotaoLivro:
            botao.deleteLater()
        self.listaBotaoLivro.clear()

        if livrosCatalogoBD:
            for livroDict in livrosCatalogoBD:
                # Iteração dos dicionários de livro do BD para criar botões e adicionar na lista
                botaoImagem = BotaoImagem(livroDict["idLivro"], livroDict["capaLivro"])
                botaoImagem.clicked.connect(self.botaoApertado)
                self.listaBotaoLivro.append(botaoImagem)

    def botaoApertado(self):
        mainWindow = widgetSearch.getAncestrais(self)["mainWindow"]
        usuarioAtual = mainWindow.getUsuario()["login"]
        popup = PopupCatalogo(self.sender().getID(), usuarioAtual, self)
        popup.exec()
