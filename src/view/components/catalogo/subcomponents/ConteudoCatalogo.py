from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
from src.view.components.catalogo.subcomponents.PainelFiltro import PainelFiltro
from src.view.components.catalogo.subcomponents.PainelLivros import PainelLivros
from src.view.utils.imageTools import relHeight, relWidth


class ConteudoCatalogo(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()

        # Configurações
        self.setParent(parent)

        # Definição de layout
        conteudoCatalogoLayout = QtWidgets.QVBoxLayout()
        conteudoCatalogoLayout.setSpacing(0)
        self.setLayout(conteudoCatalogoLayout)

        # QLabel (Catalogo)
        conteinerLabelCatalogo = QtWidgets.QHBoxLayout()
        conteudoCatalogoLayout.addLayout(conteinerLabelCatalogo)

        labelCatalogo = QtWidgets.QLabel("CATÁLOGO")
        labelCatalogo.setObjectName("labelCatalogo")
        labelCatalogo.setStyleSheet(f"""
        font-size: {relHeight(30, 1080)}px;
        """)
        labelCatalogo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        labelCatalogo.setMinimumHeight(relHeight(60, 1080))
        conteinerLabelCatalogo.addWidget(labelCatalogo)

        # Definição do contêiner com os painéis
        groupPaineis = QtWidgets.QHBoxLayout()
        groupPaineis.setSpacing(0)
        conteudoCatalogoLayout.addLayout(groupPaineis)

        # Painel de filtragem
        painelFiltro = PainelFiltro(self)
        painelFiltro.setObjectName("painelFiltro")
        groupPaineis.addWidget(painelFiltro)

        # Painel de livros
        painelLivros = PainelLivros(self)
        painelLivros.setObjectName("painelLivros")
        groupPaineis.addWidget(painelLivros)

        groupPaineis.setStretch(0, 41)
        groupPaineis.setStretch(1, 100)
