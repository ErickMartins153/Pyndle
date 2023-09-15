import copy

from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
from src.view.utils.imageTools import relHeight, relWidth

class BotaoAvaliacao(QtWidgets.QHBoxLayout):
    def __init__(self):
        super().__init__()
        # Atributos
        self.avaliacao = 0

        # Configurando
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # Definindo botões de avaliação
        self.listaBotoes = list()

        for nota in range(5):
            botaoAvaliacao = QtWidgets.QPushButton()
            botaoAvaliacao.setStyleSheet("""
            image: url(src/view/assets/icons/estrelaUnfill.svg);
            background-color: transparent;
            """)

            botaoAvaliacao.clicked.connect(lambda x="", nota=nota: self.setAvaliacao(nota+1))

            self.listaBotoes.append(botaoAvaliacao)
            self.addWidget(botaoAvaliacao)


    def setAvaliacao(self, avaliacao: int):
        if avaliacao == self.avaliacao:
            self.avaliacao = 0
            for botao in self.listaBotoes:
                botao.setStyleSheet("""
                image: url(src/view/assets/icons/estrelaUnfill.svg);
                background-color: transparent;
                """)

        else:
            self.avaliacao = avaliacao

            for contador, botao in enumerate(self.listaBotoes):
                if contador+1 <= avaliacao:
                    botao.setStyleSheet("""
                    image: url(src/view/assets/icons/estrelaFill.svg);
                    background-color: transparent;
                    """)
                else:
                    botao.setStyleSheet("""
                    image: url(src/view/assets/icons/estrelaUnfill.svg);
                    background-color: transparent;
                    """)


    def getAvaliacao(self):
        return self.avaliacao


    def getBotoes(self):
        return self.listaBotoes
