from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from src.view.components.BotaoAvaliacao import BotaoAvaliacao
from src.view.widgets.minhaBiblioteca.subcomponents.FormularioLivro import FormularioLivro
from src.view.utils import widgetSearch
from src.view.utils.container import verticalFrame, horizontalFrame, gridFrame
from src.controller.telaPrincipal import getGeneros
from src.view.utils.imageTools import relHeight, relWidth


class PainelFiltroBiblioteca(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget):
        """
        Painel contendo os filtros de "Minha Biblioteca"
        :param parent: Parente do widget
        """
        super().__init__()

        # ATRIBUTOS --------------------------------------------

        self.generoMarcado = None
        self.ordemAlf = None
        self.avaliacao = None

        # CONFIGURAÇÕES -----------------------------------------

        self.setParent(parent)
        self.setMinimumWidth(relWidth(400, 1920))
        self.setMaximumWidth(relWidth(500, 1920))

        # LAYOUT --------------------------------------------------------

        painelFiltroLayout = QtWidgets.QVBoxLayout()
        painelFiltroLayout.setSpacing(relHeight(50, 1080))
        self.setLayout(painelFiltroLayout)

        # BOTÃO DE VOLTAR -------------------------------------------------------

        # Layout para posicionar botão de voltar
        conteinerBotaoVoltar = horizontalFrame(self)
        conteinerBotaoVoltar.setMaximumHeight(relHeight(60, 1080))
        conteinerBotaoVoltar.layout().setAlignment(Qt.AlignmentFlag.AlignLeft)
        painelFiltroLayout.addWidget(conteinerBotaoVoltar)

        # Definindo botão de voltar
        botaoVoltar = QtWidgets.QPushButton()
        botaoVoltar.setObjectName("botaoVoltar")
        botaoVoltar.setStyleSheet(
            f"""
            width: {relWidth(20, 1920)}px;
            height: {relHeight(20, 1080)}px;
        """
        )
        botaoVoltar.clicked.connect(self.voltarBotaoClicado)
        botaoVoltar.setMinimumSize(relWidth(40, 1920), relHeight(40, 1080))
        conteinerBotaoVoltar.layout().addWidget(botaoVoltar)


        # FRAME COM OS FILTROS ----------------------------------------------------

        # Layout no qual as informações do frame serão posicionados | Também ajuda no alinhamento
        layoutFrame = QtWidgets.QVBoxLayout()
        layoutFrame.setAlignment(Qt.AlignmentFlag.AlignCenter)
        painelFiltroLayout.addLayout(layoutFrame)

        # Frame propriamente dito
        frameFiltros = gridFrame(self)
        frameFiltros.setStyleSheet(f"""
        border-radius: {relHeight(20, 1080)}px
        """)
        frameFiltros.setObjectName("frameFiltros")
        frameFiltros.setFixedSize(relWidth(385, 1920), relHeight(550, 1080))
        layoutFrame.addWidget(frameFiltros)

        frameFiltros.layout().setContentsMargins(
            relWidth(20, 1920),
            relHeight(20, 1080),
            relWidth(20, 1920),
            relHeight(20, 1080),
        )
        frameFiltros.setLayout(frameFiltros.layout())


        # LABEL ("FILTRAGEM") -------------------------------------------------------

        # Layout para posicionar o label
        layoutLabelFiltros = QtWidgets.QHBoxLayout()
        layoutLabelFiltros.setAlignment(Qt.AlignmentFlag.AlignCenter)
        frameFiltros.layout().addLayout(layoutLabelFiltros, 0, 0, 100, 3)

        # Definindo label de filtragem
        labelFiltros = QtWidgets.QLabel("FILTRAGEM")
        labelFiltros.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        labelFiltros.setStyleSheet(
            f"""
        font-size: {relHeight(30, 1080)}px;
        """
        )
        layoutLabelFiltros.addWidget(labelFiltros)


        # ORDEM ALFABÉTICA -------------------------------------------------------

        # LABEL ("ORDEM ALFABÉTICA") ------------------------------------
        labelOrdemAlf = QtWidgets.QLabel("Ordem Alfabética |")
        labelOrdemAlf.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        labelOrdemAlf.setMinimumWidth(relWidth(220, 1920))
        labelOrdemAlf.setObjectName("filtroLabel")
        labelOrdemAlf.setStyleSheet(
            f"""
        font-size: {relHeight(20, 1080)}px;
        """
        )
        frameFiltros.layout().addWidget(labelOrdemAlf, 40, 0, 1, 1)

        # LAYOUT (UP_ARROW E DOWN_ARROW) ------------------------------------

        # Definição do layout
        botaoAlfLayout = QtWidgets.QHBoxLayout()
        botaoAlfLayout.setSpacing(0)
        botaoAlfLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        frameFiltros.layout().addLayout(botaoAlfLayout, 40, 1, 1, 2)


        # BOTÃO DE UP_ARROW -------------------------------------------------

        self.botaoAlfUp = QtWidgets.QPushButton()
        self.botaoAlfUp.setStyleSheet(
            f"""
        width: {relWidth(10, 1920)}px;
        height: {relWidth(10, 1080)}px;
        """
        )
        self.botaoAlfUp.setFixedSize(relWidth(25, 1920), relHeight(25, 1080))
        self.botaoAlfUp.setCheckable(True)
        self.botaoAlfUp.setObjectName("botaoAlfUp")
        self.botaoAlfUp.clicked.connect(self.botaoOrdAlfClicado)
        botaoAlfLayout.addWidget(self.botaoAlfUp)


        # BOTÃO DE DOWN_ARROW ------------------------------------------------

        self.botaoAlfDown = QtWidgets.QPushButton()
        self.botaoAlfDown.setStyleSheet(
            f"""
        width: {relWidth(10, 1920)}px;
        height: {relWidth(10, 1080)}px;
        """
        )
        self.botaoAlfDown.setFixedSize(relWidth(25, 1920), relHeight(25, 1080))
        self.botaoAlfDown.setCheckable(True)
        self.botaoAlfDown.setObjectName("botaoAlfDown")
        self.botaoAlfDown.clicked.connect(self.botaoOrdAlfClicado)
        botaoAlfLayout.addWidget(self.botaoAlfDown)


        # SPACER ---------------------------------------------------------------
        spacer = QtWidgets.QSpacerItem(relWidth(10, 1920), 0)

        botaoAlfLayout.addSpacerItem(spacer)


        # (Gêneros) ---------------------------------------------------

        # CONTAINER (Onde fica o label e o container dos gêneros) -------------------
        conteinerGenero = verticalFrame(self, "conteinerGenero")
        conteinerGenero.layout().setSpacing(0)
        conteinerGenero.layout().setContentsMargins(0, 0, 0, 0)
        frameFiltros.layout().addWidget(conteinerGenero, 60, 0, 3, 3)

        # LABEL ("GÊNEROS") ----------------------------------------------------
        labelGeneros = QtWidgets.QLabel("Gêneros:")
        labelGeneros.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        labelGeneros.setObjectName("filtroLabel")
        labelGeneros.setStyleSheet(
            f"""
        font-size: {relHeight(20, 1080)}px;
        background-color: transparent;
        """
        )
        conteinerGenero.layout().addWidget(labelGeneros)

        # LAYOUT (GENEROS) -----------------------------------------------------
        groupGeneros = gridFrame(self, "groupGeneros")
        groupGeneros.setStyleSheet("background-color: transparent")
        groupGeneros.layout().setAlignment(Qt.AlignmentFlag.AlignLeft)
        groupGeneros.layout().setContentsMargins(10, 3, 0, 0)
        groupGeneros.layout().setSpacing(10)
        conteinerGenero.layout().addWidget(groupGeneros)

        # Definindo radioButtons de gênero
        self.groupRadio = QtWidgets.QButtonGroup()
        self.groupRadio.setExclusive(False)

        # Coleta os gêneros definidos em TelaPrincipal.py
        generos = getGeneros()

        quant_linhas, coluna, linha = 5, 0, 0
        for contador, genero in enumerate(generos):
            if contador != 0 and contador % quant_linhas == 0:
                coluna += 1
                linha = 0

            radioButton = QtWidgets.QCheckBox(genero)
            radioButton.clicked.connect(self.radioButtonClicado)
            radioButton.setObjectName("radioButton")
            radioButton.setStyleSheet(
                f"""
                font-size: {relHeight(15, 1080)}px;
            """
            )
            self.groupRadio.addButton(radioButton)
            groupGeneros.layout().addWidget(radioButton, linha, coluna)
            linha += 1

        # (AVALIAÇÃO) -------------------------------------------

        # QLabel ("Avaliação")
        avaliacaoLabel = QtWidgets.QLabel("Avaliação:")
        avaliacaoLabel.setObjectName("filtroLabel")
        avaliacaoLabel.setStyleSheet(
            f"""
        font-size: {relHeight(20, 1080)}px;
        """
        )
        frameFiltros.layout().addWidget(avaliacaoLabel, 80, 0, 1, 3)

        # Botões de avaliação

        self.botaoAvaliacao = BotaoAvaliacao(0)
        for botao in self.botaoAvaliacao.getBotoes():
            botao.clicked.connect(self.botaoAvaliacaoClicado)
        frameFiltros.layout().addLayout(self.botaoAvaliacao, 81, 0, 1, 1)


        # (BOTÃO FILTRAR) ----------------------------------------
        botaoFiltrar = QtWidgets.QPushButton()
        botaoFiltrar.setObjectName("botaoFiltrar")
        botaoVoltar.setStyleSheet(
            f"""
            #botaoFiltrar {{
                width: {relWidth(1, 1920)}px;
                height: {relHeight(1, 1080)}px;
                border-radius: 20px;
            }}
                """
        )
        botaoFiltrar.clicked.connect(self.botaoFiltrarClicado)
        botaoFiltrar.setFixedSize(relWidth(100, 1920), relHeight(50, 1080))
        frameFiltros.layout().addWidget(
            botaoFiltrar, 90, 0, 1, 3, Qt.AlignmentFlag.AlignCenter
        )


        # (BOTÃO ADICIONAR) -----------------------------------------
        containerBotaoAdicionar = verticalFrame(self)
        containerBotaoAdicionar.setMaximumHeight(100)
        containerBotaoAdicionar.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        painelFiltroLayout.addWidget(containerBotaoAdicionar)

        botaoAdicionar = QtWidgets.QPushButton("")
        botaoAdicionar.setObjectName("botaoAdicionar")
        botaoAdicionar.setStyleSheet(
            f"""
            width: {relWidth(20, 1920)}px;
            height: {relHeight(20, 1080)}px;
        """
        )
        botaoAdicionar.clicked.connect(self.adicionarBotaoCliclado)
        botaoAdicionar.setMinimumSize(relWidth(40, 1920), relHeight(40, 1080))
        containerBotaoAdicionar.layout().addWidget(botaoAdicionar)


    # MÉTODOS ----------------------------------------------------

    def voltarBotaoClicado(self):
        """
        Volta de "Minha Biblioteca" para a "Dashboard"
        :return:
        """
        mainWindow = widgetSearch.getAncestrais(self)["mainWindow"]
        widgetSearch.getDescendentes(mainWindow)["paginas"].setCurrentIndex(1)
        widgetSearch.getDescendentes(mainWindow)["fundoDashboard"].resizeAndDisplayLivros()

        # Resetando filtro
        self.ordemAlf = None
        self.generoMarcado = None
        self.avaliacao = None

        for botao in self.groupRadio.buttons():
            botao.setChecked(False)
        self.botaoAlfDown.setChecked(False)
        self.botaoAlfUp.setChecked(False)
        self.botaoAvaliacao.setAvaliacao(0)


    def adicionarBotaoCliclado(self):
        """
        Abre o PopUp do livro
        """
        popup = FormularioLivro(self)
        popup.exec()


    def radioButtonClicado(self):
        """
        Trata o comportamento dos radioButtons de gênero
        **OBS**: Apenas permite que um seja selecionado por vez
        """

        # Verifica se o botão que enviou o sinal já não está marcado
        if self.sender().text() != self.generoMarcado:
            self.generoMarcado = self.sender().text()
            for botao in self.groupRadio.buttons():
                if botao != self.sender():
                    botao.setChecked(False)

        # Caso o botão que enviou o sinal esteja marcado, remove a marcação
        else:
            self.generoMarcado = None
            self.sender().setChecked(False)


    def botaoOrdAlfClicado(self):
        """
        Controla o tratamento dos UpArrow e DownArrow
        **OBS**: Apenas permite que um seja selecionado por vez
        :return:
        """

        # Trata a informação do botão recebido com lógica booleana
        if self.sender().objectName() == "botaoAlfUp":
            ordem = True
        else:
            ordem = False

        # Verifica se o sinal recebido já não é do botão que já está ativo
        if ordem != self.ordemAlf:
            self.ordemAlf = ordem
            if ordem is True:
                self.botaoAlfDown.setChecked(False)
            else:
                self.botaoAlfUp.setChecked(False)

        # Caso o botão que enviou o sinal seja aquele que já está marcado, remove marcação
        else:
            self.ordemAlf = None
            self.sender().setChecked(False)

    def botaoAvaliacaoClicado(self):
        """
        Trata o retorno do grupo de botões de avaliação
        """

        # Caso seja diferente de 0, apenas define o valor
        if self.botaoAvaliacao.getAvaliacao() != 0:
            self.avaliacao = self.botaoAvaliacao.getAvaliacao()
        # Caso contrário, a avaliação considerada é nula
        else:
            self.avaliacao = None

    def botaoFiltrarClicado(self):
        """
        Filtra os livros de "Minha Biblioteca"
        """

        # Acessa o painel de livros e atualiza os livros com o filtro
        widgetSearch.getIrmaos(self)["painelLivrosBiblioteca"].getLivrosMinhaBiblioteca(
            self.generoMarcado, self.avaliacao, self.ordemAlf)
