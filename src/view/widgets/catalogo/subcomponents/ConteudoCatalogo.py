from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from src.view.widgets.catalogo.subcomponents.PainelFiltroCatalogo import PainelFiltroCatalogo
from src.view.widgets.catalogo.subcomponents.PainelLivrosCatalogo import PainelLivrosCatalogo
from src.view.utils.container import verticalFrame
from src.view.utils.imageTools import relHeight


class ConteudoCatalogo(QtWidgets.QFrame):
    """
    Conteúdo do "Catálogo" onde estão dispostos os painéis de filtro e livro
    """
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()

        # CONFIGURAÇÕES -------------------------------------------

        self.setParent(parent)


        # LAYOUT --------------------------------------------------

        conteudoCatalogoLayout = QtWidgets.QVBoxLayout()
        conteudoCatalogoLayout.setSpacing(0)
        self.setLayout(conteudoCatalogoLayout)


        # LABEL ("Catálogo") --------------------------------------

        conteinerLabelCatalogo = QtWidgets.QHBoxLayout()
        conteudoCatalogoLayout.addLayout(conteinerLabelCatalogo)

        labelCatalogo = QtWidgets.QLabel("CATÁLOGO")
        labelCatalogo.setObjectName("labelConteudo")
        labelCatalogo.setStyleSheet(f"""
        font-size: {relHeight(30, 1080)}px;
        """)
        labelCatalogo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        labelCatalogo.setMinimumHeight(relHeight(60, 1080))
        conteinerLabelCatalogo.addWidget(labelCatalogo)


        # CONTAINER DE PAINÉIS ------------------------------------

        groupPaineis = QtWidgets.QHBoxLayout()
        groupPaineis.setSpacing(0)
        conteudoCatalogoLayout.addLayout(groupPaineis)

        # Painel de filtragem
        painelFiltro = PainelFiltroCatalogo(self)
        painelFiltro.setObjectName("painelFiltroCatalogo")
        painelFiltro.setStyleSheet(f"""
            border-bottom-left-radius: {relHeight(15, 1080)}px;
            border-top-left-radius: {relHeight(15, 1080)}px;
            border-bottom-right-radius: 0px;
        """)
        groupPaineis.addWidget(painelFiltro)

        # Painel de livros

        containerPainelLivros = verticalFrame(self, "containerPainelLivros")
        containerPainelLivros.setStyleSheet(f"""
            border-top-right-radius: {relHeight(15, 1080)}px;
            border-top-left-radius: 0;
            border-bottom-right-radius: {relHeight(15, 1080)}px;
            border-bottom-left-radius: 0;
        """)

        painelLivros = PainelLivrosCatalogo(self)
        painelLivros.setObjectName("painelLivrosCatalogo")
        containerPainelLivros.layout().addWidget(painelLivros)

        groupPaineis.addWidget(containerPainelLivros)


        # PROPORÇÃO DOS PAINÉIS ------------------------------------

        groupPaineis.setStretch(0, 41)
        groupPaineis.setStretch(1, 100)
