from PyQt6 import QtWidgets, QtGui, QtCore, QtSvg
from PyQt6.QtCore import Qt
from src.view.utils import imageTools


class FotoPerfil(QtWidgets.QPushButton):
    def __init__(self, bimage: bytes = b""):
        super().__init__()
        # Atributos
        self.bimage = bimage

        # Definindo icon
        if self.bimage != b"":
            self.changePhoto(bimage)

    def resizePhoto(self, width: int, height: int, diametro: int):
        """
        Redimensiona o tamanho da foto
        **Obs: Pode gerar distorções**
        :param width: largura do botão
        :param height: altura do botão
        """
        resizedBimage = imageTools.getResizedImage(self.bimage, width, height)
        self.changePhoto(resizedBimage, diametro)

    def changePhoto(self, newBimage: bytes, diametro: int):
        self.bimage = newBimage

        if (
            b"<?xml" in newBimage
            or b"<!DOCTYPE svg" in newBimage
            or b"<svg" in newBimage
        ):
            pixmap = QtGui.QPixmap.fromImage(QtGui.QImage.fromData(newBimage))
            self.setIcon(QtGui.QIcon(pixmap))
            self.setIconSize(QtCore.QSize(pixmap.width(), pixmap.height()))
            self.setFixedSize(pixmap.width(), pixmap.height())
        else:
            roundedPixmap = imageTools.getCircularPixmap(newBimage, diametro)

            self.setIcon(QtGui.QIcon(roundedPixmap))
            self.setIconSize(
                QtCore.QSize(roundedPixmap.width(), roundedPixmap.height())
            )
            self.setFixedSize(roundedPixmap.width(), roundedPixmap.height())

    def removePhoto(self):
        self.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(QtGui.QImage())))
