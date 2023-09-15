from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal
from src.controller.telaPreviaLivro import pegarAvaliacao


class BotaoAvaliacao(QtWidgets.QHBoxLayout):
    mudancaAvaliacao = pyqtSignal(int)

    def __init__(self, estrelasPreenchidas: int):
        super().__init__()
        # Atributos
        self.avaliacao = estrelasPreenchidas

        # Configurando
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # Definindo botões de avaliação
        self.listaBotoes = list()

        for nota in range(5):
            botaoAvaliacao = QtWidgets.QPushButton()
            botaoAvaliacao.setStyleSheet(
                """
            image: url(src/view/assets/icons/estrelaUnfill.svg);
            background-color: transparent;
            border: 0px none transparent;
            """
            )

            botaoAvaliacao.clicked.connect(
                lambda x="", nota=nota: self.setAvaliacao(nota + 1)
            )
            self.listaBotoes.append(botaoAvaliacao)
            self.addWidget(botaoAvaliacao)

        self.setAvaliacao(self.avaliacao)

    def setAvaliacao(self, estrelasPreenchidas: int):
        for contador, botao in enumerate(self.listaBotoes):
            if contador + 1 <= estrelasPreenchidas:
                botao.setStyleSheet(
                    """
                image: url(src/view/assets/icons/estrelaFill.svg);
                background-color: transparent;
                border: 0px none transparent;
                """
                )
            else:
                botao.setStyleSheet(
                    """
                image: url(src/view/assets/icons/estrelaUnfill.svg);
                background-color: transparent;
                border: 0px none transparent;
                """
                )

        self.mudancaAvaliacao.emit(estrelasPreenchidas)

    # def alterarAvaliacao(self):
    #   avaliacao = self.avaliacao
    #  self.mudancaAvaliacao.emit(avaliacao)
