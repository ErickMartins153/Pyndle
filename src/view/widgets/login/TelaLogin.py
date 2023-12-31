from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from src.view.widgets.login.subcomponents.FormularioRegistro import (
    FormularioRegistro,
)
from src.view.widgets.login.subcomponents.FormularioLogin import FormularioLogin
from src.view.utils.imageTools import relWidth, relHeight


class TelaLogin(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget):
        """
        Tela de login com os formulários de login e registro
        :param parent: define o parente do widget
        """
        # CONFIGURAÇÕES ----------------------------------------------------------
        super().__init__()
        self.setParent(parent)
        self.setStyleSheet(open("src/view/assets/styles/login/telaLogin.css").read())


        # LAYOUT -----------------------------------------------------------------
        loginLayout = QtWidgets.QVBoxLayout()
        loginLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(loginLayout)


        # FRAME FUNDO 1 ----------------------------------------------------------
        fundo = QtWidgets.QFrame(self)
        fundo.setObjectName("fundo")
        loginLayout.addWidget(fundo)

        fundoLayout = QtWidgets.QVBoxLayout()
        fundoLayout.setContentsMargins(
            relWidth(30, 1920),
            relHeight(40, 1080),
            relWidth(30, 1920),
            relHeight(40, 1080),
        )
        fundoLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        fundo.setLayout(fundoLayout)


        # FRAME (Fundo do formulário) ---------------------------------------------
        fundoFormulario = QtWidgets.QFrame(fundo)
        fundoFormulario.setObjectName("fundoFormulario")
        fundoFormulario.setMaximumSize(relWidth(800, 1920), relHeight(900, 1080))
        fundoLayout.addWidget(fundoFormulario)

        fundoFormularioLayout = QtWidgets.QVBoxLayout()
        fundoFormularioLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        fundoFormularioLayout.setContentsMargins(
            relWidth(30, 1920),
            relHeight(20, 1080),
            relWidth(30, 1920),
            relHeight(20, 1080),
        )
        fundoFormulario.setLayout(fundoFormularioLayout)


        # FORMULÁRIO DE LOGIN ------------------------------------------------------
        formularioLogin = FormularioLogin(fundoFormulario)
        formularioLogin.setObjectName("formularioLogin")
        fundoFormularioLayout.addWidget(formularioLogin)


        # FORMULÁRIO DE REGISTRO ---------------------------------------------------
        self.formularioRegistro = FormularioRegistro(self)
        self.formularioRegistro.setObjectName("formularioRegistro")
        fundoFormularioLayout.addWidget(self.formularioRegistro)
