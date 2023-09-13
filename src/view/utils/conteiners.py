from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QSizePolicy
from PyQt6.QtCore import Qt


class verticalFrame(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QFrame | QtWidgets.QWidget, objectName: str = ""):
        """
        Frame com layout vertical embutido
        :param parent: parente do frame, objeto no qual estará inserido
        :param objectName: objectName para identificar no QSS ou buscas do WidgetSearch
        """
        super().__init__()
        # Configurando
        self.setParent(parent)
        self.setObjectName(objectName)

        # Definindo Layout
        self.layoutVertical = QtWidgets.QVBoxLayout()
        self.setLayout(self.layoutVertical)

    def layout(self):
        """
        Retorna o layout do frame
        """
        return self.layoutVertical


class horizontalFrame(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QFrame | QtWidgets.QWidget, objectName: str):
        """
        Frame com layout horizontal embutido
        :param parent: parente do frame, objeto no qual estará inserido
        :param objectName: objectName para identificar no QSS ou buscas do WidgetSearch
        """
        super().__init__()
        # Configurando
        self.setParent(parent)
        self.setObjectName(objectName)

        # Definindo Layout
        self.layoutHorizontal = QtWidgets.QHBoxLayout()
        self.setLayout(self.layoutHorizontal)

    def layout(self):
        """
        Retorna o layout do frame
        """
        return self.layoutHorizontal


class gridFrame(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QFrame | QtWidgets.QWidget, objectName: str):
        """
        Frame com layout de grid embutido
        :param parent: parente do frame, objeto no qual estará inserido
        :param objectName: objectName para identificar no QSS ou buscas do WidgetSearch
        """
        super().__init__()
        # Configurando
        self.setParent(parent)
        self.setObjectName(objectName)

        # Definindo Layout
        self.layoutGrid = QtWidgets.QGridLayout()
        self.setLayout(self.layoutGrid)

    def layout(self):
        """
        Retorna o layout do frame
        """
        return self.layoutGrid


class verticalWidget(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QFrame | QtWidgets.QWidget, objectName: str):
        """
        Widget com layout vertical embutido
        :param parent: parente do frame, objeto no qual estará inserido
        :param objectName: objectName para identificar no QSS ou buscas do WidgetSearch
        """
        super().__init__()
        # Configurando
        self.setParent(parent)
        self.setObjectName(objectName)

        # Definindo Layout
        self.layoutVertical = QtWidgets.QVBoxLayout()
        self.setLayout(self.layoutVertical)

    def layout(self):
        """
        Retorna o layout do widget
        """
        return self.layoutVertical


class horizontalWidget(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QFrame | QtWidgets.QWidget, objectName: str):
        """
        Widget com layout horizontal embutido
        :param parent: parente do frame, objeto no qual estará inserido
        :param objectName: objectName para identificar no QSS ou buscas do WidgetSearch
        """
        super().__init__()
        # Configurando
        self.setParent(parent)
        self.setObjectName(objectName)

        # Definindo Layout
        self.layoutHorizontal = QtWidgets.QHBoxLayout()
        self.setLayout(self.layoutHorizontal)

    def layout(self):
        """
        Retorna o layout do widget
        """
        return self.layoutHorizontal


class gridWidget(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QFrame | QtWidgets.QWidget, objectName: str):
        """
        Widget com layout de grid embutido
        :param parent: parente do frame, objeto no qual estará inserido
        :param objectName: objectName para identificar no QSS ou buscas do WidgetSearch
        """
        super().__init__()
        # Configurando
        self.setParent(parent)
        self.setObjectName(objectName)

        # Definindo Layout
        self.layoutGrid = QtWidgets.QGridLayout()
        self.setLayout(self.layoutGrid)

    def layout(self):
        """
        Retorna o layout do widget
        """
        return self.layoutGrid
