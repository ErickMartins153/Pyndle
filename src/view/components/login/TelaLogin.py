from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
import sys
from src.view.components.login.Formulario import Formulario
from src.view.components.login.TelaRegistro import TelaRegistro


class TelaLogin(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()
        self.setParent(parent)
        self.setStyleSheet(open("src/view/assets/styles/telaLogin.css").read())

        loginLayout = QtWidgets.QVBoxLayout()
        self.setLayout(loginLayout)

        # QFrame (fundo)
        fundo = QtWidgets.QFrame(self)
        fundo.setObjectName("fundo")
        loginLayout.addWidget(fundo)

        fundoLayout = QtWidgets.QVBoxLayout()
        fundoLayout.setContentsMargins(200, 20, 200, 20)
        fundo.setLayout(fundoLayout)

        # QFrame (formulario)
        formulario = Formulario(self)
        formulario.setObjectName("formulario")
        fundoLayout.addWidget(formulario)

        # QFrame (registrar)
        self.TelaRegistro = TelaRegistro(self)
        self.TelaRegistro.setObjectName("formulario")
        fundoLayout.addWidget(self.TelaRegistro)
