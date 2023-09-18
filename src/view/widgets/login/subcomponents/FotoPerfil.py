from PyQt6 import QtWidgets, QtGui, QtCore, QtSvg
from PyQt6.QtCore import Qt
from src.view.utils import imageTools

class FotoPerfil(QtWidgets.QPushButton):
    def __init__(self, bimage: bytes = b""):
        """
        Gera um pixmap circular com base na imagem fornecida
        :param bimage: imagem de perfil em bytes
        """
        super().__init__()

        # Atributos
        self.bimage = bimage

        # Definindo icon
        if self.bimage != b"":
            self.changePhoto(bimage)


    # MÉTODOS --------------------------------------------

    def resizePhoto(self, width: int, height: int):
        """
        Redimensiona o tamanho da foto
        **Obs: Pode gerar distorções**
        :param width: largura do botão
        :param height: altura do botão
        """
        resizedBimage = imageTools.getResizedImage(self.bimage, width, height)
        self.changePhoto(resizedBimage)


    def changePhoto(self, newBimage: bytes):
        """
        Altera a foto de perfil atual
        :param newBimage: nova imagem de perfil em bytes
        """

        # Atualizando atributos bimage com a nova foto
        self.bimage = newBimage

        # Verifica se a imagem é um SVG
        if b"<?xml" in newBimage or b"<!DOCTYPE svg" in newBimage or b"<svg" in newBimage:
            pixmap = QtGui.QPixmap.fromImage(QtGui.QImage.fromData(newBimage))
            self.setIcon(QtGui.QIcon(pixmap))
            self.setIconSize(QtCore.QSize(pixmap.width(), pixmap.height()))
            self.setFixedSize(pixmap.width(), pixmap.height())

        # Caso, contrário, trata como arquivo de imagem normal
        else:
            roundedPixmap = imageTools.getCircularPixmap(newBimage, 100)

            self.setIcon(QtGui.QIcon(roundedPixmap))
            self.setIconSize(QtCore.QSize(roundedPixmap.width(), roundedPixmap.height()))
            self.setFixedSize(roundedPixmap.width(), roundedPixmap.height())


    def removePhoto(self):
        """
        Remove foto de perfil atual e volta com a imagem padrão
        """
        self.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(QtGui.QImage())))
