from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from src.view.widgets.pesquisa.subcomponents.PainelFiltro import PainelFiltro
from src.view.widgets.pesquisa.subcomponents.PainelLivrosResultado import PainelLivrosResultado
from src.view.utils.widgetSearch import getAncestrais
from src.view.utils.container import verticalFrame
from src.view.utils.imageTools import relHeight


class ConteudoFiltro(QtWidgets.QFrame):
    """
    Conteúdo do "Pesquisa" onde estão dispostos os painéis de filtro e os livros encontrados
    """
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()

        # CONFIGURAÇÕES -------------------------------------------

        self.setParent(parent)
        self.idLivrosFiltro = getAncestrais(self)["mainWindow"].dashboard.menu.sinalPesquisa.connect(self.getPesquisaFiltro)

        # LAYOUT --------------------------------------------------

        conteudoFiltroLayout = QtWidgets.QVBoxLayout()
        conteudoFiltroLayout.setSpacing(0)
        self.setLayout(conteudoFiltroLayout)


        # LABEL ("Catálogo") --------------------------------------

        conteinerLabelFiltro = QtWidgets.QHBoxLayout()
        conteudoFiltroLayout.addLayout(conteinerLabelFiltro)

        labelFiltro = QtWidgets.QLabel("RESULTADOS FILTRO")
        labelFiltro.setObjectName("labelConteudo")
        labelFiltro.setStyleSheet(f"""
        font-size: {relHeight(30, 1080)}px;
        """)
        labelFiltro.setAlignment(Qt.AlignmentFlag.AlignCenter)
        labelFiltro.setMinimumHeight(relHeight(60, 1080))
        conteinerLabelFiltro.addWidget(labelFiltro)


        # CONTAINER DE PAINÉIS ------------------------------------

        self.groupPaineis = QtWidgets.QHBoxLayout()
        self.groupPaineis.setSpacing(0)
        conteudoFiltroLayout.addLayout(self.groupPaineis)

        # Painel de filtragem
        painelFiltro = PainelFiltro(self)
        painelFiltro.setObjectName("painelFiltro")
        painelFiltro.setStyleSheet(f"""
            border-bottom-left-radius: {relHeight(15, 1080)}px;
            border-top-left-radius: {relHeight(15, 1080)}px;
            border-bottom-right-radius: 0px;
        """)
        self.groupPaineis.addWidget(painelFiltro)

        # Painel de livros
        painelLivros = PainelLivrosResultado(self, "")
        painelLivros.setObjectName("painelLivrosResultado")
        self.groupPaineis.addWidget(painelLivros)
       


        # PROPORÇÃO DOS PAINÉIS ------------------------------------

        self.groupPaineis.setStretch(0, 41)
        self.groupPaineis.setStretch(1, 100)
    
    def getPesquisaFiltro(self, textoPesquisa: str):
        self.groupPaineis.itemAt(1).widget().deleteLater()

        painelLivros = PainelLivrosResultado(self, textoPesquisa)
        painelLivros.setObjectName("painelLivrosResultado")
        self.groupPaineis.addWidget(painelLivros)
