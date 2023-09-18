from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
import sys
from PIL import Image
import pyautogui
import io


def getFormatedImage(bimage: bytes, format: str = 'JPEG'):
    """
    Formata a imagem em binário para o formato desejado
    :param bimage: bytes da imagem a ser formatada
    :param format: formato do arquivo retornado (JPEG ou pNG)
    :return:
    """
    imageObject = Image.open(io.BytesIO(bimage))


    if format == "JPEG":
        imageObject = imageObject.convert("RGB")


    output_stream = io.BytesIO()
    imageObject.save(output_stream, format)
    imageObject = output_stream.getvalue()

    return imageObject

def getResizedImage(bimage: bytes, width: int, height: int, format: str = 'JPEG'):
    """
    Redimensiona imagens a partir da imagem em binário
    :param bimage: bytes da imagem a ser redimensionada
    :param width: largura redimensionada
    :param height: altura redimensionada
    :param format: formato do arquivo retornado (JPEG ou PNG)
    :return: retorna bytes da imagem redimensionada
    """

    formatedImage = Image.open(io.BytesIO(getFormatedImage(bimage, format)))
    resizedImage = formatedImage.resize((width, height))


    output_stream = io.BytesIO()
    resizedImage.save(output_stream, format)
    resizedBimage = output_stream.getvalue()

    return resizedBimage

def getCroppedImageFromCenter(bimage: bytes, width: int, height: int, format: str = 'JPEG'):
    """
    Recorta uma imagem com base no tamanho desejado (a partir do centro)
    :param bimage: bytes da imagem a ser recortada a partir do centro
    :param width: largura da imagem recortada
    :param height: altura da imagem recortada
    :param format:
    :return: retorna bytes da imagem recorta a partir do centro
    """

    pixmap = QtGui.QPixmap.fromImage(QtGui.QImage.fromData(bimage))

    if width > pixmap.width():
        width = pixmap.width()

    if height > pixmap.height():
        height = pixmap.height()

    moldura = QtGui.QPixmap(width, height)
    moldura.fill(QtGui.QColor("transparent"))

    mascara = QtCore.QRect(0, 0, width, height)
    mascara.moveCenter(pixmap.rect().center())

    painter = QtGui.QPainter(moldura)
    painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
    painter.drawPixmap(moldura.rect(), pixmap, mascara)
    painter.end()

    byteArray = QtCore.QByteArray()

    buffer = QtCore.QBuffer(byteArray)
    buffer.open(QtCore.QBuffer.OpenModeFlag.WriteOnly)

    moldura.save(buffer, "PNG")

    buffer.close()

    cropedBimage = byteArray.data()

    return cropedBimage

def getRoundedPixmap(bimage: bytes, hRound: int, vRound: int):
    """
    Cria um pixmap com bordas arredondadas a partir de uma imagem em formato binário

    :param bimage: imagem que deseja arredondar as bordas
    :param vRound: grau de arredondamento vertical
    :param hRound: grau de arredondamento horizontal
    :return:
    """

    # Criando pixmap --------------------------------------------------------------
    pixmap = QtGui.QPixmap(QtGui.QImage.fromData(bimage))

    # Criando moldura -------------------------------------------------------------
    moldura = QtGui.QPixmap(pixmap.size())
    moldura.fill(QtGui.QColor("transparent"))

    # Aplicando pixmap arredondado na moldura -------------------------------------
    painter = QtGui.QPainter(moldura)
    painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
    painter.setBrush(QtGui.QBrush(pixmap))
    painter.setPen(QtCore.Qt.PenStyle.NoPen)
    painter.drawRoundedRect(pixmap.rect(), hRound, vRound)
    del painter

    return moldura

def getCircularPixmap(bimage: bytes, size: int):
    """
    Cria um pixmap em formato circular a partir de uma imagem em formato binário
    :param bimage: bytes da imagem a partir da qual deseja formar o pixmap circular
    :param size: diâmetro do círculo
    :return: retorna um pixmap circular
    """
    pixmap = QtGui.QPixmap.fromImage(QtGui.QImage.fromData(bimage))

    # Recortando a imagem
    baseSize = min(pixmap.width(), pixmap.height())
    cropedBimage = getCroppedImageFromCenter(bimage, baseSize, baseSize)

    # Redimensionando a imagem
    resizedImage = getResizedImage(cropedBimage, size, size)

    # Gerando pixmap circular
    pixmap = QtGui.QPixmap.fromImage(QtGui.QImage.fromData(resizedImage))

    moldura = QtGui.QPixmap(size, size)
    moldura.fill(QtGui.QColor("transparent"))

    painter = QtGui.QPainter(moldura)
    painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
    mascara = QtGui.QPainterPath()
    mascara.addEllipse(0, 0, size, size)
    painter.setClipPath(mascara)

    painter.drawPixmap(moldura.rect(), pixmap)

    return moldura

def relWidth(numerador: int, denominador: int):
    """
    Retorna o comprimento da tela reajustado de acordo com uma proporção definida [numerador // denominador]\n
    OBS: o valor retornado sempre é arredondado
    """
    width = pyautogui.size()[0]

    rWidth = width * numerador // denominador

    return rWidth


def relHeight(numerador: int, denominador: int):
    """
    Retorna o altura da tela reajustado de acordo com uma proporção definida [numerador // denominador]\n
    OBS: o valor retornado sempre é arredondado
    """
    height = pyautogui.size()[1]

    rHeight = height * numerador // denominador

    return rHeight


def getScreenResolution():
    """
    Função para obter a resolução da tela atual em forma de dicionário
    """
    width, height = pyautogui.size()
    return {"width": width, "height": height}
