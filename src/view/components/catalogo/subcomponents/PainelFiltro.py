from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QSizePolicy
from PyQt6.QtCore import Qt
from src.view.utils import widgetSearch
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


        # QLineEdit (Barra de pesquisa)
        barraPesquisa = QtWidgets.QLineEdit(self)
        barraPesquisa.setObjectName("barraPesquisa")
        barraPesquisa.setPlaceholderText("Pesquisar catálogo")
        barraPesquisa.setMinimumHeight(relHeight(35, 1080))
        painelFiltroLayout.addWidget(barraPesquisa)

        # QFrame
        frameFiltros = QtWidgets.QFrame(self)
        frameFiltros.setStyleSheet("background-color: white; border-radius: 20px")
        frameFiltros.setObjectName("frameFiltros")
        painelFiltroLayout.addWidget(frameFiltros)

    def voltarBotaoClicado(self):
        mainWindow = widgetSearch.getAncestrais(self)["mainWindow"]
        widgetSearch.getDescendentes(mainWindow)["paginas"].setCurrentIndex(1)