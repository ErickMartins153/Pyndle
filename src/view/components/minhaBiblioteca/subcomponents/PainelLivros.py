from PyQt6 import QtWidgets, QtGui
from src.controller.telaPrincipal import filtrarBiblioteca
from src.view.components.BotaoImagem import BotaoImagem
from src.view.utils import widgetSearch
from src.view.utils.imageTools import relHeight, relWidth
from src.view.components.ModuloLivro.Popup import Popup


class PainelLivros(QtWidgets.QScrollArea):
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
        self.getLivrosMinhaBiblioteca()

    def resizeEvent(self, a0: QtGui.QResizeEvent = QtGui.QResizeEvent) -> None:
        """
        Evento de redimensionamento de tela que define o tamanho dos botoesLivros e como serão dispostos,
        de acordo com a resolução da tela
        """
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
        linha, coluna = 0, 0
        for botaoImagem in self.listaBotaoLivro:
            botaoImagem.resizeButton(width, height)
            self.painelLivrosLayout.addWidget(botaoImagem, linha, coluna)

            coluna += 1

            if coluna == quantColunas:
                coluna = 0
                linha += 1

    def getLivrosMinhaBiblioteca(
        self, genero: str = None, avaliacao: int = None, ordemAlfabetica: bool = None
    ):
        """
        Obtém os livros da "Minha Biblioteca" com base no usuário atual da MainWindow\n
        Após isso, os livros são dispostos no display do painel de livros de "Minha Biblioteca"
        :param genero: define o gênero dos livros a serem dispostos
        :param avaliacao: define a avaliação dos livros a serem dispostos
        :param ordemAlfabetica: define a ordem na qual os livros serão dispostos
        """

        # Obtém o usuário atual a partir da MainWindow
        usuarioAtual = widgetSearch.getAncestrais(self)["mainWindow"].getUsuario()

        if usuarioAtual:  # Verifica se o usuário já foi definido
            livrosCatalogoBD = filtrarBiblioteca(
                usuarioAtual["idUsuario"], genero, avaliacao, ordemAlfabetica
            )

            for botao in self.listaBotaoLivro:
                botao.deleteLater()  # Deleta os botoesLivros que já existem
            self.listaBotaoLivro.clear()

            if livrosCatalogoBD:
                for livroDict in livrosCatalogoBD:
                    # Iteração dos dicionários de livro do BD para criar botões e adicionar na lista
                    botaoImagem = BotaoImagem(
                        livroDict["idLivro"], livroDict["capaLivro"]
                    )
                    botaoImagem.clicked.connect(self.botaoApertado)
                    self.listaBotaoLivro.append(botaoImagem)

            self.resizeEvent(None)
            # resizeEvent para dispor os livros de acordo com a resolução da janela

    def botaoApertado(self):
        mainWindow = widgetSearch.getAncestrais(self)["mainWindow"]
        usuarioAtual = mainWindow.getUsuario()["login"]
        popup = Popup(usuarioAtual, self.sender().getID())
        popup.exec()
