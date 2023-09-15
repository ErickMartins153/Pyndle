from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from src.view.components.BotaoAvaliacao import BotaoAvaliacao
from src.view.utils import widgetSearch
from src.view.utils.container import verticalFrame, gridFrame
from src.view.utils.imageTools import relHeight, relWidth


class PainelFiltro(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()

        # Atributos
        self.generoMarcado = None
        self.ordemAlf = None

        # Configurações
        self.setParent(parent)
        self.setMinimumWidth(relWidth(400, 1920))
        self.setMaximumWidth(relWidth(500, 1920))

        # Definindo Layout
        painelFiltroLayout = QtWidgets.QVBoxLayout()
        self.setLayout(painelFiltroLayout)

        # QPushButton (Botão de voltar)
        conteinerBotaoVoltar = QtWidgets.QHBoxLayout()
        conteinerBotaoVoltar.setAlignment(Qt.AlignmentFlag.AlignLeft)
        painelFiltroLayout.addLayout(conteinerBotaoVoltar)

        botaoVoltar = QtWidgets.QPushButton()
        botaoVoltar.setObjectName("botaoVoltar")
        botaoVoltar.setStyleSheet(f"""
        width: {relWidth(20, 1920)}px;
        height: {relHeight(20, 1080)}px;
        """)
        botaoVoltar.clicked.connect(self.voltarBotaoClicado)
        botaoVoltar.setMinimumSize(relWidth(40, 1920), relHeight(40, 1080))
        conteinerBotaoVoltar.addWidget(botaoVoltar)

        # QFrame -----------------------------------------------------
        layoutFrame = QtWidgets.QVBoxLayout()
        layoutFrame.setAlignment(Qt.AlignmentFlag.AlignCenter)
        painelFiltroLayout.addLayout(layoutFrame)

        frameFiltros = QtWidgets.QFrame(self)
        frameFiltros.setStyleSheet(f"""
        border-radius: {relHeight(20, 1080)}px
        """)
        frameFiltros.setObjectName("frameFiltros")
        frameFiltros.setFixedSize(relWidth(350, 1920), relHeight(550, 1080))
        layoutFrame.addWidget(frameFiltros)

        layoutFrameFiltros = QtWidgets.QGridLayout()
        layoutFrameFiltros.setContentsMargins(relWidth(20, 1920), relHeight(20, 1080), relWidth(20, 1920), relHeight(20, 1080))
        frameFiltros.setLayout(layoutFrameFiltros)

        # QLabel ("FILTROS") -----------------------------------------------
        layoutLabelFiltros = QtWidgets.QHBoxLayout()
        layoutLabelFiltros.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutFrameFiltros.addLayout(layoutLabelFiltros, 0, 0, 100, 3)

        labelFiltros = QtWidgets.QLabel("FILTRAGEM")
        labelFiltros.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        labelFiltros.setStyleSheet(f"""
        font-size: {relHeight(30, 1080)}px;
        """)
        layoutLabelFiltros.addWidget(labelFiltros)

        # (Ordem Alfabética) ----------------------------------------------

        # Label "Ordem Alfabética"
        labelOrdemAlf = QtWidgets.QLabel("Ordem Alfabética |")
        labelOrdemAlf.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        labelOrdemAlf.setObjectName("filtroLabel")
        labelOrdemAlf.setStyleSheet(f"""
        font-size: {relHeight(20, 1080)}px;
        """)
        layoutFrameFiltros.addWidget(labelOrdemAlf, 40, 0, 1, 1)


        # Layout para posicionar botões upArrow e downArrow
        botaoAlfLayout = QtWidgets.QHBoxLayout()
        botaoAlfLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layoutFrameFiltros.addLayout(botaoAlfLayout, 40, 1, 1, 2)
        # layoutFrameFiltros.setRowStretch(1, 9)

        # Botões UpArrow e DownArrow
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


        # Spacer
        spacer = QtWidgets.QSpacerItem(relWidth(40, 1920), 0)
        botaoAlfLayout.addSpacerItem(spacer)

        # (Gêneros) ---------------------------------------------------

        # Container
        conteinerGenero = verticalFrame(self, "conteinerGenero")
        conteinerGenero.layout().setSpacing(0)
        conteinerGenero.layout().setContentsMargins(0, 0, 0, 0)
        layoutFrameFiltros.addWidget(conteinerGenero, 60, 0, 3, 3)

        # Label ("Gêneros")
        labelGeneros = QtWidgets.QLabel("Gêneros:")
        labelGeneros.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        labelGeneros.setObjectName("filtroLabel")
        labelGeneros.setStyleSheet(
            f"""
        font-size: {relHeight(20, 1080)}px;

        background-color: transparent;
        """)
        conteinerGenero.layout().addWidget(labelGeneros)

        # LayoutGeneros
        groupGeneros = gridFrame(self, "groupGeneros")
        groupGeneros.setStyleSheet("background-color: transparent")
        groupGeneros.layout().setAlignment(Qt.AlignmentFlag.AlignLeft)
        groupGeneros.layout().setContentsMargins(10, 3, 0, 0)
        groupGeneros.layout().setSpacing(10)
        conteinerGenero.layout().addWidget(groupGeneros)

        # RadioButtons ("Generos")
        self.groupRadio = QtWidgets.QButtonGroup()
        self.groupRadio.setExclusive(False)

        generos = (
            "Terror", "Fantasia", "Aventura",
            "Romance", "Matemática", "Geografia",
            "Linguagens", "Literatura"
        )

        quant_linhas, coluna, linha = 5, 0, 0
        for contador, genero in enumerate(generos):
            if contador != 0 and contador % quant_linhas == 0:
                coluna += 1
                linha = 0

            radioButton = QtWidgets.QCheckBox(genero)
            radioButton.clicked.connect(self.radioButtonClicado)
            radioButton.setObjectName("radioButton")
            radioButton.setStyleSheet(f"""
                font-size: {relHeight(15, 1080)}px;
            """)
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
        layoutFrameFiltros.addWidget(botaoFiltrar, 90, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)


    def voltarBotaoClicado(self):
        mainWindow = widgetSearch.getAncestrais(self)["mainWindow"]
        widgetSearch.getDescendentes(mainWindow)["paginas"].setCurrentIndex(1)
        widgetSearch.getDescendentes(mainWindow)["fundoDashboard"].resizeEvent(None)

        # Resetando filtro
        self.ordemAlf = None
        self.generoMarcado = None

        for botao in self.groupRadio.buttons():
            botao.setChecked(False)
        self.botaoAlfDown.setChecked(False)
        self.botaoAlfUp.setChecked(False)


    def radioButtonClicado(self):
        if self.sender().text() != self.generoMarcado:
            self.generoMarcado = self.sender().text()
            for botao in self.groupRadio.buttons():
                if botao != self.sender():
                    botao.setChecked(False)
        else:
            self.generoMarcado = None
            self.sender().setChecked(False)

        '''if self.generoMarcado:
            for botao in self.groupRadio.buttons():
                if self.sender() == botao and botao.isChecked():
                    botao.setChecked(False)'''

    def botaoOrdAlfClicado(self):
        if self.sender().objectName() == "botaoAlfUp":
            ordem = True
        else:
            ordem = False


        if ordem != self.ordemAlf:
            self.ordemAlf = ordem
            if ordem is True:
                self.botaoAlfDown.setChecked(False)
            else:
                self.botaoAlfUp.setChecked(False)
        else:
            self.ordemAlf = None
            self.sender().setChecked(False)


    def botaoFiltrarClicado(self):
        widgetSearch.getIrmaos(self)["painelLivrosCatalogo"].getLivrosCatalogo(self.generoMarcado, self.ordemAlf)
        widgetSearch.getIrmaos(self)["painelLivrosCatalogo"].resizeEvent(None)
