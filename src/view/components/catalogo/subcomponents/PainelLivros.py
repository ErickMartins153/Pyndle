from PyQt6 import QtWidgets, QtGui
from src.controller.telaPrincipal import livrosCatalogo
from src.view.components.BotaoImagem import BotaoImagem
from src.view.utils import widgetSearch
from src.view.utils.imageTools import relHeight, relWidth


class PainelLivros(QtWidgets.QScrollArea):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()
        self.setStyleSheet(
            open("src/view/assets/styles/catalogo/painelLivros.css").read()
        )

        # Configurações
        self.setParent(parent)
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
        self.listaBotaoLivro = list()  # Lista para acessar os BotoesLivros em métodos
        self.atualizarLivros()

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        super().resizeEvent(a0)
        mainWindow = widgetSearch.getAncestrais(self)[
            "mainWindow"
        ]  # mainWindow para identificar redimensionamentos
        print(f"{mainWindow.width()}X{mainWindow.height()}")

        # Redimensionamento dos livros
        if mainWindow.width() >= relWidth(
            1640, 1920
        ):  # Redimensiona de acordo com o tamanho da janela
            print("Escalado")

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

    def atualizarLivros(self):
        # Limpar os livros
        self.limparLivros()

        livrosCatalogoBD = livrosCatalogo()
        for livroTupla in livrosCatalogoBD:
            botaoImagem = BotaoImagem(livroTupla[0], livroTupla[5])
            self.listaBotaoLivro.append(botaoImagem)

        # Exibir os livros
        self.displayBotoesLivros(3, relWidth(200, 1920), relHeight(280, 1080))

    def limparLivros(self):
        # Remover todos os livros do layout e da lista
        for botaoImagem in self.listaBotaoLivro:
            self.painelLivrosLayout.removeWidget(botaoImagem)
            botaoImagem.setParent(None)
        self.listaBotaoLivro.clear()
