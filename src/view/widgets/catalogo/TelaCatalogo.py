from PyQt6 import QtWidgets
from src.view.components.Menu import Menu
from src.view.widgets.catalogo.subcomponents.ConteudoCatalogo import ConteudoCatalogo
from src.view.utils.imageTools import relHeight, relWidth

class TelaCatalogo(QtWidgets.QFrame):
    """
    Tela que contém o conteúdo do "Catálogo"
    """
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()

        # CONFIGURAÇÕES ----------------------------------------

        self.setParent(parent)
        self.setStyleSheet(open("src/view/assets/styles/catalagoEMinhaBiblioteca/telaCatalogoBiblioteca.css").read())


        # LAYOUT -----------------------------------------------

        telaCatalogoLayout = QtWidgets.QVBoxLayout()
        telaCatalogoLayout.setSpacing(0)
        self.setLayout(telaCatalogoLayout)


        # MENU -------------------------------------------------

        menu = Menu(self)
        menu.setObjectName("menu")
        telaCatalogoLayout.addWidget(menu)


        # CONTEÚDO DO CATÁLOGO ---------------------------------

        conteudoCatalogo = ConteudoCatalogo(self)
        conteudoCatalogo.setObjectName("conteudoFrame")
        conteudoCatalogo.setStyleSheet(f"""
            border-bottom-left-radius: {relWidth(15, 1080)}px;
            border-bottom-right-radius: {relHeight(15, 1080)}px;
        """)
        telaCatalogoLayout.addWidget(conteudoCatalogo)
