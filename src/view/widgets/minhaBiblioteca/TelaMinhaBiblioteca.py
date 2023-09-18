from PyQt6 import QtWidgets
from src.view.components.Menu import Menu
from src.view.widgets.minhaBiblioteca.subcomponents.ConteudoMinhaBiblioteca import (
    ConteudoMinhaBiblioteca,
)
from src.view.utils.imageTools import relHeight, relWidth


class TelaMinhaBiblioteca(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget):
        """
        Widget onde estão dispostos o menu e o conteúdo de "Minha Biblioteca"
        :param parent: Parente do widget
        """
        super().__init__()

        # CONFIGURAÇÕES -----------------------------------
        self.setParent(parent)
        self.setStyleSheet(
            open("src/view/assets/styles/catalagoEMinhaBiblioteca/telaCatalogoBiblioteca.css").read())

        # LAYOUT -------------------------------------------

        telaCatalogoLayout = QtWidgets.QVBoxLayout()
        telaCatalogoLayout.setSpacing(0)
        self.setLayout(telaCatalogoLayout)


        # MENU ---------------------------------------------

        menu = Menu(self)
        menu.setObjectName("menu")
        telaCatalogoLayout.addWidget(menu)


        # CONTEÚDO DO CATÁLOGO -----------------------------

        conteudoMinhaBiblioteca = ConteudoMinhaBiblioteca(self)
        conteudoMinhaBiblioteca.setObjectName("conteudoFrame")
        conteudoMinhaBiblioteca.setStyleSheet(
            f"""
            border-bottom-left-radius: {relWidth(15, 1080)}px;
            border-bottom-right-radius: {relHeight(15, 1080)}px;
        """
        )
        telaCatalogoLayout.addWidget(conteudoMinhaBiblioteca)
