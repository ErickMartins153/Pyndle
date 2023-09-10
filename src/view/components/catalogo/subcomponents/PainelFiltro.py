from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QSizePolicy
from PyQt6.QtCore import Qt
from src.view.utils import widgetSearch


class PainelFiltro(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()

        # Configurações
        self.setParent(parent)
        # self.setContentsMargins(10, 10, 10, 10)
        self.setMinimumWidth(400)
        self.setMaximumWidth(500)

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
        botaoVoltar.setMaximumWidth(20)
        botaoVoltar.setMaximumHeight(20)
        conteinerBotaoVoltar.addWidget(botaoVoltar)


        # QLineEdit (Barra de pesquisa)
        barraPesquisa = QtWidgets.QLineEdit(self)
        barraPesquisa.setObjectName("barraPesquisa")
        barraPesquisa.setPlaceholderText("Pesquisar catálogo")
        barraPesquisa.setMinimumHeight(35)
        painelFiltroLayout.addWidget(barraPesquisa)

        # QFrame
        frameFiltros = QtWidgets.QFrame(self)
        frameFiltros.setStyleSheet("background-color: white; border-radius: 20px")
        frameFiltros.setObjectName("frameFiltros")
        painelFiltroLayout.addWidget(frameFiltros)

    def voltarBotaoClicado(self):
        mainWindow = widgetSearch.getAncestrais(self)["mainWindow"]
        widgetSearch.getDescendentes(mainWindow)["paginas"].setCurrentIndex(1)