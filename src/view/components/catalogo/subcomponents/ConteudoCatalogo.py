from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
from src.view.components.catalogo.subcomponents.PainelFiltro import PainelFiltro
from src.view.components.catalogo.subcomponents.PainelLivros import PainelLivros


class ConteudoCatalogo(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()

        # Configurações
        self.setParent(parent)

        # Definição de layout
        conteudoCatalogoLayout = QtWidgets.QHBoxLayout()
        conteudoCatalogoLayout.setSpacing(0)
        self.setLayout(conteudoCatalogoLayout)

        # Painel de filtragem
        painelFiltro = PainelFiltro(self)
        painelFiltro.setObjectName("painelFiltro")
        conteudoCatalogoLayout.addWidget(painelFiltro)

        # Painel de livros
        painelLivros = PainelLivros(self)
        painelLivros.setObjectName("painelLivros")
        conteudoCatalogoLayout.addWidget(painelLivros)

        conteudoCatalogoLayout.setStretch(0, 41)
        conteudoCatalogoLayout.setStretch(1, 100)
