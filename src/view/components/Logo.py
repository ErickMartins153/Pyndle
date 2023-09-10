from PyQt6 import QtWidgets, QtGui, QtCore
from src.view.utils import imageTools

class Logo(QtWidgets.QLabel):
    def __init__(self, width: int, height: int):
        """
        Logo do pyndle

        :param width: define a largura
        :param height: define a altura
        """
        super().__init__()
        # Configurações
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Carregando imagem -----------------------------------------------------------
        with open("src/view/assets/images/Logo.jpg", "rb") as arquivo:
            self.imagemLogo = arquivo.read()
            resizedImagemLogo = imageTools.getResizedImage(self.imagemLogo, width, height)

        # Gerando pixmap com bordas arredondadas ---------------------------------------
        roundedLogo = imageTools.getRoundedPixmap(resizedImagemLogo, 30, 30)

        # Definindo logo --------------------------------------------------------------
        self.setPixmap(roundedLogo)
