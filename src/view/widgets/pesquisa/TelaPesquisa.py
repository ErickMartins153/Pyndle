from PyQt6 import QtWidgets

from src.view.components.Menu import Menu
from src.view.widgets.pesquisa.subcomponents.ConteudoFiltro import ConteudoFiltro
from src.view.utils.imageTools import relHeight, relWidth
from src.view.utils.widgetSearch import getAncestrais

class TelaPesquisa(QtWidgets.QFrame):
    """
    Tela que contém o conteúdo do "Catálogo"
    """

    
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()

        # CONFIGURAÇÕES ----------------------------------------
        
        self.setParent(parent)
        self.setStyleSheet(open("src/view/assets/styles/catalagoEMinhaBiblioteca/telaCatalogoBiblioteca.css").read())
    
        # LAYOUT -----------------------------------------------

        telaFiltroLayout = QtWidgets.QVBoxLayout()
        telaFiltroLayout.setSpacing(0)
        self.setLayout(telaFiltroLayout)


        # MENU -------------------------------------------------

        menu = Menu(self)
        menu.setObjectName("menu")
        telaFiltroLayout.addWidget(menu)


        # CONTEÚDO DO FILTRO ---------------------------------

        conteudoFiltro = ConteudoFiltro(self)
        conteudoFiltro.setObjectName("conteudoFrame")
        conteudoFiltro.setStyleSheet(f"""
            border-bottom-left-radius: {relWidth(15, 1080)}px;
            border-bottom-right-radius: {relHeight(15, 1080)}px;
        """)
        telaFiltroLayout.addWidget(conteudoFiltro)

    def mostrarLivrosPesquisa(self, texto):
        print(texto)
    