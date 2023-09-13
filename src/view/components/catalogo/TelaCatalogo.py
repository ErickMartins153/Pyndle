from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
from src.view.components.Menu import Menu
from src.view.components.catalogo.FormularioLivro import FormularioLivro
from src.view.components.catalogo.subcomponents.ConteudoCatalogo import ConteudoCatalogo


class TelaCatalogo(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()

        # Configurações
        self.setParent(parent)
        self.setStyleSheet(
            open("src/view/assets/styles/catalogo/telaCatalogo.css").read()
        )

        # Definição do layout
        telaCatalogoLayout = QtWidgets.QVBoxLayout()
        telaCatalogoLayout.setSpacing(0)
        self.setLayout(telaCatalogoLayout)

        # QFrame (Menu)
        menu = Menu(self)
        menu.setObjectName("menu")
        telaCatalogoLayout.addWidget(menu)

        # QFrame (ConteudoCatalogo)
        conteudoCatalogo = ConteudoCatalogo(self)
        conteudoCatalogo.setObjectName("conteudoCatalogo")
        telaCatalogoLayout.addWidget(conteudoCatalogo)

        botaoAdicionarLivro = QtWidgets.QPushButton(self)
        botaoAdicionarLivro.setText("adicionar livro")
        telaCatalogoLayout.addWidget(botaoAdicionarLivro)
        botaoAdicionarLivro.clicked.connect(self.adicionarLivro)

    def adicionarLivro(self):
        popup = FormularioLivro(self)
        popup.exec()
