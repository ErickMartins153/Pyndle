from PyQt6 import QtWidgets
from PyQt6.QtCore import QObject

def getAncestrais(objeto: QtWidgets.QWidget):
    """
    Retorna todos os ancestrais daquele widget

    :param objeto: Widget a partir do qual deseja procurar ancestrais
    :return: Dicionário com os objectNames e as instâncias dos ancestrais {"ObjectName": Object}
    """
    ancestrais = list()
    widget = objeto
    while widget:
        widget = widget.parent()
        if widget:
            ancestrais.append((widget.objectName(), widget))
    return dict(ancestrais)

def getDescendentes(objeto: QtWidgets.QWidget):
    """
    Retorna todos os descendentes daquele widget

    :param objeto: widget a partir do qual você deseja obter os descendentes
    :return: Dicionário com os objectName e instãncias de todos os descendentes {"ObjectName": Object"}
    """
    descendentes = list()

    for filho in objeto.findChildren(QObject):  # Itera todos os descendentes
        # Filtra apenas os Widgets/Contêiners
        if isinstance(filho, QtWidgets.QWidget) or isinstance(filho, QtWidgets.QFrame) or isinstance(filho, QtWidgets.QStackedWidget):
            descendentes.append((filho.objectName(), filho))
            if filho.findChildren(QObject):
                getDescendentes(filho)  # Recursão para obter descendentes dos descendentes, caso existam

    return dict(descendentes)

def getIrmaos(objeto: QtWidgets.QWidget):
    """
    Retorna os irmãos daquele widget

    :param objeto: Widget a partir do qual você deseja obter os irmãos
    :return: Dicionário com os objectName e instãncias de todos os irmãos {"ObjectName": Object"}
    """
    irmaos = list()

    for irmao in objeto.parent().findChildren(QObject):
        # Filtra apenas os Widgets/Contêiners
        if (isinstance(irmao, QtWidgets.QWidget) or isinstance(irmao, QtWidgets.QFrame) or isinstance(irmao, QtWidgets.QStackedWidget) and irmao !=
                objeto):
            irmaos.append((irmao.objectName(), irmao))

    return dict(irmaos)
