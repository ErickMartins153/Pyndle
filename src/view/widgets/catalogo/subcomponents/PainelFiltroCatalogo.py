from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from src.view.components.BotaoAvaliacao import BotaoAvaliacao
from src.view.utils import widgetSearch
from src.controller.telaPrincipal import getGeneros
from src.view.utils.container import verticalFrame, gridFrame
from src.view.utils.imageTools import relHeight, relWidth


class PainelFiltroCatalogo(QtWidgets.QFrame):
    """
    Painel com os filtros do "Catálogo"

    **ATRIBUTOS:**
        - generoMarcado: informa o gênero que será filtrado
        - ordemAlf: informa a ordem do filtro
    """
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()

        # ATRIBUTOS ----------------------------------------
        self.generoMarcado = None
        self.ordemAlf = None

        # CONFIGURAÇÕES -----------------------------------------------
        self.setParent(parent)
        self.setMinimumWidth(relWidth(400, 1920))
        self.setMaximumWidth(relWidth(500, 1920))


        # CONTAINER PRINCIPAL ------------------------------------------

        painelFiltroLayout = QtWidgets.QVBoxLayout()
        painelFiltroLayout.setSpacing(0)
        self.setLayout(painelFiltroLayout)


        # BOTÃO DE VOLTAR ----------------------------------------------

        # Container para alinhar botão no container principal
        conteinerBotaoVoltar = QtWidgets.QHBoxLayout()
        conteinerBotaoVoltar.setAlignment(Qt.AlignmentFlag.AlignLeft)
        painelFiltroLayout.addLayout(conteinerBotaoVoltar)

        # Instanciamento do botão
        botaoVoltar = QtWidgets.QPushButton()
        botaoVoltar.setObjectName("botaoVoltar")
        botaoVoltar.setStyleSheet(f"""
        width: {relWidth(20, 1920)}px;
        height: {relHeight(20, 1080)}px;
        """)
        botaoVoltar.clicked.connect(self.voltarBotaoClicado)
        botaoVoltar.setMinimumSize(relWidth(40, 1920), relHeight(40, 1080))
        conteinerBotaoVoltar.addWidget(botaoVoltar)

        # LAYOUT COM O FRAME/CONTAINER DE FILTROS ----------------------------------------------

        layoutFrame = QtWidgets.QVBoxLayout()
        layoutFrame.setAlignment(Qt.AlignmentFlag.AlignCenter)
        painelFiltroLayout.addLayout(layoutFrame)


        # CONTAINER (Frame com os filtros) -----------------------------------------------------

        # Grid para posicionamento dos elementos no frame de filtros
        frameFiltros = gridFrame(self, "frameFiltros")
        frameFiltros.setStyleSheet(f"""
            border-radius: {relHeight(20, 1080)}px
        """)

        # Definindo configurações do layout do grid
        frameFiltros.setFixedSize(relWidth(350, 1920), relHeight(550, 1080))
        painelFiltroLayout.addWidget(frameFiltros)

        frameFiltros.layout().setContentsMargins(
            relWidth(20, 1920),
            relHeight(20, 1080),
            relWidth(20, 1920),
            relHeight(20, 1080),
        )

        # Adicionando Grid
        layoutFrame.addWidget(frameFiltros)


        # LABEL (FILTRAGEM) -----------------------------------------------------

        # Layout para alinhar label no Frame de filtros
        layoutLabelFiltros = QtWidgets.QHBoxLayout()
        layoutLabelFiltros.setAlignment(Qt.AlignmentFlag.AlignCenter)
        frameFiltros.layout().addLayout(layoutLabelFiltros, 0, 0, 100, 3)

        # Instanciamento do label
        labelFiltros = QtWidgets.QLabel("FILTRAGEM")
        labelFiltros.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        labelFiltros.setStyleSheet(
            f"""
        font-size: {relHeight(30, 1080)}px;
        """
        )

        # Adicionando label no layout para alinhamento
        layoutLabelFiltros.addWidget(labelFiltros)


        # ORDEM ALFABÉTICA ----------------------------------------------

        # LABEL ORDEM ALFABÉTICA ----------------------------------------

        # Instanciamento do label
        labelOrdemAlf = QtWidgets.QLabel("Ordem Alfabética |")
        labelOrdemAlf.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        labelOrdemAlf.setObjectName("filtroLabel")
        labelOrdemAlf.setStyleSheet(f"""
            font-size: {relHeight(20, 1080)}px;
        """)
        frameFiltros.layout().addWidget(labelOrdemAlf, 40, 0, 1, 1)


        # BOTÕES DE UP_ARROW E DOWN_ARROW ----------------------------------

        # Layout para posicionar botões upArrow e downArrow
        botaoAlfLayout = QtWidgets.QHBoxLayout()
        botaoAlfLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        frameFiltros.layout().addLayout(botaoAlfLayout, 40, 1, 1, 2)

        # Botão "UpArrow"
        self.botaoAlfUp = QtWidgets.QPushButton()
        self.botaoAlfUp.setStyleSheet(f"""
            width: {relWidth(10, 1920)}px;
            height: {relWidth(10, 1080)}px;
        """)
        self.botaoAlfUp.setFixedSize(relWidth(25, 1920), relHeight(25, 1080))
        self.botaoAlfUp.setCheckable(True)
        self.botaoAlfUp.setObjectName("botaoAlfUp")
        self.botaoAlfUp.clicked.connect(self.botaoOrdAlfClicado)
        botaoAlfLayout.addWidget(self.botaoAlfUp)

        # Botão "DownArrow"
        self.botaoAlfDown = QtWidgets.QPushButton()
        self.botaoAlfDown.setStyleSheet(f"""
            width: {relWidth(10, 1920)}px;
            height: {relWidth(10, 1080)}px;
        """)
        self.botaoAlfDown.setFixedSize(relWidth(25, 1920), relHeight(25, 1080))
        self.botaoAlfDown.setCheckable(True)
        self.botaoAlfDown.setObjectName("botaoAlfDown")
        self.botaoAlfDown.clicked.connect(self.botaoOrdAlfClicado)
        botaoAlfLayout.addWidget(self.botaoAlfDown)


        # Spacer para colocar os botões de UpArrow e DownArrow à esquerda
        spacer = QtWidgets.QSpacerItem(relWidth(40, 1920), 0)
        botaoAlfLayout.addSpacerItem(spacer)


        # GÊNEROS ---------------------------------------------------

        # CONTAINER DE GÊNEROS --------------------------------------
        conteinerGenero = verticalFrame(self, "conteinerGenero")
        conteinerGenero.layout().setSpacing(0)
        conteinerGenero.layout().setContentsMargins(0, 0, 0, 0)
        frameFiltros.layout().addWidget(conteinerGenero, 60, 0, 3, 3)


        # LABEL DE GÊNEROS -------------------------------------------

        # Instanciamento do label
        labelGeneros = QtWidgets.QLabel("Gêneros:")
        labelGeneros.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        labelGeneros.setObjectName("filtroLabel")
        labelGeneros.setStyleSheet(f"""
            font-size: {relHeight(20, 1080)}px;
            background-color: transparent;
        """)

        # Adicionando label
        conteinerGenero.layout().addWidget(labelGeneros)


        # CONTAINER DOS BOTÕES DE GÊNERO -------------------------------
        groupGeneros = gridFrame(self, "groupGeneros")
        groupGeneros.setStyleSheet("background-color: transparent")
        groupGeneros.layout().setAlignment(Qt.AlignmentFlag.AlignLeft)
        groupGeneros.layout().setContentsMargins(10, 3, 0, 0)
        groupGeneros.layout().setSpacing(10)
        conteinerGenero.layout().addWidget(groupGeneros)

        # RadioButtons ("Generos")
        self.groupRadio = QtWidgets.QButtonGroup()
        self.groupRadio.setExclusive(False)

        # Obtendo gêneros
        generos = getGeneros()

        # Criando botões de gênero
        quant_linhas, coluna, linha = 5, 0, 0
        for contador, genero in enumerate(generos):
            if contador != 0 and contador % quant_linhas == 0:
                coluna += 1
                linha = 0

            radioButton = QtWidgets.QCheckBox(genero)
            radioButton.setObjectName("radioButton")
            radioButton.setStyleSheet(f"""
                font-size: {relHeight(15, 1080)}px;
            """)

            radioButton.clicked.connect(self.radioButtonClicado)
            self.groupRadio.addButton(radioButton)
            groupGeneros.layout().addWidget(radioButton, linha, coluna)

            linha += 1


        # (BOTÃO FILTRAR) ----------------------------------------
        botaoFiltrar = QtWidgets.QPushButton()
        botaoFiltrar.setObjectName("botaoFiltrar")
        botaoVoltar.setStyleSheet(f"""
            #botaoFiltrar {{
                width: {relWidth(1, 1920)}px;
                height: {relHeight(1, 1080)}px;
                border-radius: 20px;
            }}  
        """)
        botaoFiltrar.clicked.connect(self.botaoFiltrarClicado)
        botaoFiltrar.setFixedSize(relWidth(100, 1920), relHeight(50, 1080))
        frameFiltros.layout().addWidget(botaoFiltrar, 90, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)


    # MÉTODOS -----------------------------------------------------


    def voltarBotaoClicado(self):
        """
        Volta a janela para "Dashboard"\n
        **OBS:** Reseta os filtros ativos no momento e atualiza os livros da
        DashBoard para caso o usuário tenha salvo algum livro
        """

        # Obtendo mainWindow para trocar de janela e atualizar livros
        mainWindow = widgetSearch.getAncestrais(self)["mainWindow"]
        widgetSearch.getDescendentes(mainWindow)["paginas"].setCurrentIndex(1)
        widgetSearch.getDescendentes(mainWindow)["fundoDashboard"].resizeAndDisplayLivros()

        # Resetando filtro
        self.ordemAlf = None
        self.generoMarcado = None

        for botao in self.groupRadio.buttons():
            botao.setChecked(False)
        self.botaoAlfDown.setChecked(False)
        self.botaoAlfUp.setChecked(False)

    def radioButtonClicado(self):
        """
        Controla o comportamento dos botões de seleção de gênero do filtro\n
        **OBS:** Permite que apenas um gênero seja escolhido por vez
        """

        # Caso o usuário clique em um gênero diferente, o gênero é mudado
        if self.sender().text() != self.generoMarcado:
            self.generoMarcado = self.sender().text()
            for botao in self.groupRadio.buttons():
                if botao != self.sender():
                    botao.setChecked(False)

        # Caso contrário, desmarca todos os gêneros
        else:
            self.generoMarcado = None
            self.sender().setChecked(False)


    def botaoOrdAlfClicado(self):
        """
        Controla o comportamento dos botões de ordem alfabética\n
        **OBS**: Permite que apenas um seja marcado por vez
        :return:
        """

        # Trata a informação recebida de acorodo com o ObjectName do botão, utilizando lógica booleana
        if self.sender().objectName() == "botaoAlfUp":
            ordem = True
        else:
            ordem = False

        # Caso a ordem escolhida seja diferente da atual, ela é definida
        if ordem != self.ordemAlf:
            self.ordemAlf = ordem
            if ordem is True:
                self.botaoAlfDown.setChecked(False)
            else:
                self.botaoAlfUp.setChecked(False)
        # Caso contrário, o filtro de ordem é resetado
        else:
            self.ordemAlf = None
            self.sender().setChecked(False)


    def botaoFiltrarClicado(self):
        """
        Ação para filtrar e atualizar os livros do PainelDeLivros
        """

        # Obtém o painél de livros
        widgetSearch.getIrmaos(self)["painelLivrosCatalogo"].getLivrosCatalogo(self.generoMarcado, self.ordemAlf)
        # Atualiza os livros dispostos
        widgetSearch.getIrmaos(self)["painelLivrosCatalogo"].resizeAndDisplayCatalogo(None)
