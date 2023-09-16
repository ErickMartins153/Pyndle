from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from src.view.widgets.minhaBiblioteca.subcomponents.PainelFiltroBiblioteca import PainelFiltroBiblioteca
from src.view.widgets.minhaBiblioteca.subcomponents.PainelLivrosBiblioteca import PainelLivrosBiblioteca
from src.view.utils.container import verticalFrame
from src.view.utils.imageTools import relHeight


class ConteudoMinhaBiblioteca(QtWidgets.QFrame):
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

        labelCatalogo = QtWidgets.QLabel("MINHA BIBLIOTECA")
        labelCatalogo.setObjectName("labelConteudo")
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
        painelFiltro = PainelFiltroBiblioteca(self)
        painelFiltro.setObjectName("painelFiltroBiblioteca")
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

        painelLivrosBiblioteca = PainelLivrosBiblioteca(self)
        painelLivrosBiblioteca.setObjectName("painelLivrosBiblioteca")
        containerPainelLivros.layout().addWidget(painelLivrosBiblioteca)

        groupPaineis.addWidget(containerPainelLivros)

        groupPaineis.setStretch(0, 41)
        groupPaineis.setStretch(1, 100)
