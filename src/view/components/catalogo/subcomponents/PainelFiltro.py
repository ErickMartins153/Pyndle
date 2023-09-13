from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QSizePolicy
from PyQt6.QtCore import Qt
from src.view.components.catalogo.subcomponents.BotaoAvaliacao import BotaoAvaliacao
from src.view.utils import widgetSearch
from src.view.utils.conteiners import verticalFrame, horizontalFrame, gridFrame
from src.view.utils.imageTools import relHeight, relWidth


class PainelFiltro(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()

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
        botaoVoltar.clicked.connect(self.voltarBotaoClicado)
        botaoVoltar.setMaximumSize(relWidth(20, 1920), relHeight(20, 1080))
        conteinerBotaoVoltar.addWidget(botaoVoltar)

        # QFrame -----------------------------------------------------
        layoutFrame = QtWidgets.QVBoxLayout()
        layoutFrame.setAlignment(Qt.AlignmentFlag.AlignCenter)
        painelFiltroLayout.addLayout(layoutFrame)

        frameFiltros = QtWidgets.QFrame(self)
        frameFiltros.setStyleSheet("background-color: white; border-radius: 20px")
        frameFiltros.setObjectName("frameFiltros")
        frameFiltros.setFixedSize(relWidth(350, 1920), relHeight(600, 1080))
        layoutFrame.addWidget(frameFiltros)

        layoutFrameFiltros = QtWidgets.QGridLayout()
        frameFiltros.setLayout(layoutFrameFiltros)

        # QLabel ("FILTROS") -----------------------------------------------
        layoutLabelFiltros = QtWidgets.QHBoxLayout()
        layoutLabelFiltros.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutFrameFiltros.addLayout(layoutLabelFiltros, 0, 0, 1, 3)

        labelFiltros = QtWidgets.QLabel("FILTRAGEM")
        labelFiltros.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        labelFiltros.setStyleSheet(f"""
        font-size: {relHeight(30, 1080)}px;
        """)
        layoutLabelFiltros.addWidget(labelFiltros)


        # (Ordem Alfabética) ----------------------------------------------

        # Label "Ordem Alfabética"
        labelOrdemAlf = QtWidgets.QLabel("Ordem Alfabética |")
        labelOrdemAlf.setObjectName("filtroLabel")
        labelOrdemAlf.setStyleSheet(f"""
        font-size: {relHeight(20, 1080)}px;
        """)
        layoutFrameFiltros.addWidget(labelOrdemAlf, 1, 0, 1, 1)

        # Layout para posicionar botões upArrow e downArrow
        botaoAlfLayout = QtWidgets.QHBoxLayout()
        botaoAlfLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layoutFrameFiltros.addLayout(botaoAlfLayout, 1, 1, 1, 2)
        # layoutFrameFiltros.setRowStretch(1, 9)

        # Botões UpArrow e DownArrow
        botaoAlfUp = QtWidgets.QPushButton()
        botaoAlfUp.setStyleSheet(f"""
        image: url(src/view/assets/icons/setaCima.svg);
        width: {relWidth(10, 1920)}px;
        height: {relWidth(10, 1080)}px;
        background-color: transparent;
        """)
        botaoAlfUp.setFixedSize(relWidth(25, 1920), relHeight(25, 1080))
        botaoAlfUp.setObjectName("botaoAlfUp")
        botaoAlfLayout.addWidget(botaoAlfUp)

        botaoAlfDown = QtWidgets.QPushButton()
        botaoAlfDown.setStyleSheet(f"""
        image: url(src/view/assets/icons/setaBaixo.svg);
        width: {relWidth(10, 1920)}px;
        height: {relWidth(10, 1080)}px;
        background-color: transparent;
        """)
        botaoAlfDown.setFixedSize(relWidth(25, 1920), relHeight(25, 1080))
        botaoAlfDown.setObjectName("botaoAlfDown")
        botaoAlfLayout.addWidget(botaoAlfDown)

        # Spacer
        spacer = QtWidgets.QSpacerItem(relWidth(100, 1920), 0)

        botaoAlfLayout.addSpacerItem(spacer)

        # (Gêneros) ---------------------------------------------------

        # Label ("Gêneros")
        labelGeneros = QtWidgets.QLabel("Gêneros:")
        labelGeneros.setObjectName("filtroLabel")
        labelGeneros.setStyleSheet(f"""
        font-size: {relHeight(20, 1080)}px;
        """)
        layoutFrameFiltros.addWidget(labelGeneros, 2, 0, 1, 1)

        # LayoutGeneros
        layoutGeneros = QtWidgets.QGridLayout()
        layoutGeneros.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layoutGeneros.setSpacing(0)
        layoutFrameFiltros.addLayout(layoutGeneros, 3, 0, 5, 3)

        # RadioButtons ("Generos")
        self.groupRadio = QtWidgets.QButtonGroup()

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

            radioButton = QtWidgets.QRadioButton(genero)
            self.groupRadio.addButton(radioButton)
            layoutGeneros.addWidget(radioButton, linha, coluna)
            linha += 1


        # (AVALIAÇÃO) -------------------------------------------
        avaliacaoLabel = QtWidgets.QLabel("Avaliação:")
        avaliacaoLabel.setObjectName("filtroLabel")
        avaliacaoLabel.setStyleSheet(f"""
        font-size: {relHeight(20, 1080)}px;
        """)
        layoutFrameFiltros.addWidget(avaliacaoLabel, 8, 0, 1, 3)

        botaoAvaliacao = BotaoAvaliacao()
        layoutFrameFiltros.addLayout(botaoAvaliacao, 9, 0, 1, 1)




    def voltarBotaoClicado(self):
        mainWindow = widgetSearch.getAncestrais(self)["mainWindow"]
        widgetSearch.getDescendentes(mainWindow)["paginas"].setCurrentIndex(1)
