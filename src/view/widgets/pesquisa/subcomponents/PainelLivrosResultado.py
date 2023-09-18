from PyQt6 import QtWidgets, QtGui
from src.controller.telaPrincipal import filtrarLivros, checarRelacaoUsuarioLivro
from src.view.components.BotaoImagem import BotaoImagem
from src.view.widgets.moduloLivro.Popup import Popup
from src.view.widgets.catalogo.subcomponents.popupCatalogo import PopupCatalogo
from src.controller.telaPreviaLivro import dadosLivro
from src.controller.telaPrincipal import pesquisarLivro
from src.view.utils import widgetSearch
from src.view.utils.imageTools import relHeight, relWidth
from src.view.utils.container import gridWidget


class PainelLivrosResultado(QtWidgets.QScrollArea):
    # noinspection PyTypeChecker
    def __init__(self, parent: QtWidgets.QWidget, textoPesquisa: str):
        """
        Painel onde são dispostos os livros com barra de Scroll para navegar
        :param parent: Parente do Widget
        """
        super().__init__()
        # ATRIBUTOS -----------------------------------------------------------------
        self.listaBotaoLivro = list()  # Lista para acessar os BotoesLivros em métodos
        self.textoPesquisa = textoPesquisa

        # CONFIGURAÇÕES --------------------------------------------------------------
        self.setParent(parent)
        self.setStyleSheet(open("src/view/assets/styles/catalagoEMinhaBiblioteca/painelLivros.css").read())
        self.setWidgetResizable(True)
        self.setContentsMargins(0, 0, 0, 0)
        self.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)


        # WIDGET CENTRAL (Onde os livros são dispostos --------------------------------

        self.contentWidget = gridWidget(self)
        self.contentWidget.setObjectName("contentWidget")
        self.setWidget(self.contentWidget)

        self.contentWidget.layout().setSpacing(relHeight(40, 1080))

        # Definindo livros
        self.getLivrosFiltro()
        self.resizeAndDisplayFiltro()


    # (MÉTODOS) -----------------------------------------------------------------------------

    def resizeEvent(self, a0: QtGui.QResizeEvent = QtGui.QResizeEvent) -> None:
        """
        Evento de redimensionamento de tela
        :param a0:
        :return:
        """
        super().resizeEvent(a0)
        self.resizeAndDisplayFiltro()


    def resizeAndDisplayFiltro(self):
        """
        Redimensiona os livros do "Filtro" e os dispõe
        """

        # mainWindow para identificar redimensionamentos
        mainWindow = widgetSearch.getAncestrais(self)["mainWindow"]

        # Redimensiona de acordo com o tamanho da janela
        if mainWindow.width() >= relWidth(1640, 1920):
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
            self.contentWidget.layout().addWidget(botaoImagem, linha, coluna)

            coluna += 1

            if coluna == quantColunas:
                coluna = 0
                linha += 1

    def getLivrosFiltro(self, genero: str = None, ordemAlfabetica: bool = None):
        """
        Obtém os livros do filtro do pyndle.db de acordo com a palavra inserida
        :param genero: Genero do filtro
        :param ordemAlfabetica: Ordem na qual o "filtro" será filtrado
        :return:
        """

        resultadoPesquisa = pesquisarLivro(self.textoPesquisa, genero, ordemAlfabetica)

        # Obtendo livros da "Pesquisa" filtrado
        livrosFiltroBD = list()
        for registro in resultadoPesquisa:
            livrosFiltroBD.append({"idLivro": registro["idLivro"], "capaLivro": registro["capaLivro"]})
        

        # Destruindo os botões existentes
        for botao in self.listaBotaoLivro:
            botao.hide()
            botao.deleteLater()
        self.listaBotaoLivro.clear()

        # Criando os botões
        if livrosFiltroBD:
            for livroDict in livrosFiltroBD:
                    # Iteração dos dicionários de livro do BD para criar botões e adicionar na lista
                    botaoImagem = BotaoImagem(livroDict["idLivro"], livroDict["capaLivro"])
                    botaoImagem.clicked.connect(self.botaoApertado)
                    self.listaBotaoLivro.append(botaoImagem)


    def botaoApertado(self):
        """
        Abre o PopUp dos livros presentes no "Catálogo"\n
        **OBS**: O PopUp varia dependendo se o usuário já possui ou não aquele livro
        """

        # mainWindow para obter dados do usuário atual
        mainWindow = widgetSearch.getAncestrais(self)["mainWindow"]
        usuarioAtual = mainWindow.getUsuario()

        # Checa se o usuário possui aquele livro
        if checarRelacaoUsuarioLivro(usuarioAtual["idUsuario"], self.sender().getID()):
             #Abre PopUp da biblioteca caso já possua
            popupBiblioteca = Popup(usuarioAtual["login"], self.sender().getID(), self)
            popupBiblioteca.exec()
        else:
            # Abre PopUp do catálogo caso o usuário não possua o livro
            popupCatalogo = PopupCatalogo(usuarioAtual["login"], self.sender().getID(), self)
            popupCatalogo.exec()
