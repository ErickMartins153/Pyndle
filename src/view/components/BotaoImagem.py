from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
import sys
from src.view.utils import imageTools

class BotaoImagem(QtWidgets.QPushButton):
    def __init__(self, id: int, bimage: bytes):
        """
        - Botão para a disposição dos livros na "dashboard", "minhabiblioteca" e "catalagoEMinhaBiblioteca"\n
        - Guarda o id do livro para que suas informações possam ser acessadas
        - O botão assume o tamanho da imagem

        :param id: ID do livro representado pelo botão
        :param bimage: Byte com a imagem do botão
        """
        super().__init__()
        self.id = id
        self.bimage = bimage

        qimage = QtGui.QImage.fromData(self.bimage)
        self.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(qimage)))
        self.setIconSize(QtCore.QSize(qimage.width(), qimage.height()))
        self.setFixedSize(qimage.width(), qimage.height())


    def getID(self):
        return self.id

    def resizeButton(self, width: int, height: int):
        """
        Redimensiona o tamanho do botão com a imagem
        **Obs: Pode gerar distorções**
        :param width: largura do botão
        :param height: altura do botão
        """
        resizedBimage = imageTools.getResizedImage(self.bimage, width, height)
        qimage = QtGui.QImage.fromData(resizedBimage)
        self.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(qimage)))
        self.setIconSize(QtCore.QSize(qimage.width(), qimage.height()))
        self.setFixedSize(qimage.width(), qimage.height())
