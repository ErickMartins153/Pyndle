from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
import sys

class BotaoImagem(QtWidgets.QPushButton):
    def __init__(self, id: int):
        """
        - Botão para a disposição dos livros na "dashboard", "minhabiblioteca" e "catalogo"\n
        - Guarda o id do livro para que suas informações possam ser acessadas

        :param id: ID do livro representado pelo botão
        """
        super().__init__()
        self.id = id

    def getID(self):
        return self.id
