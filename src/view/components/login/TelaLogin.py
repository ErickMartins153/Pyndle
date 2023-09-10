from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from src.view.components.login.subcomponents.FormularioRegistro import FormularioRegistro
from src.view.components.login.subcomponents.FormularioLogin import FormularioLogin


class TelaLogin(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget):
        """
        Tela de login com os formulários de login e registro
        :param parent: define o parente do widget
        """
        # Configurações
        super().__init__()
        self.setParent(parent)
        self.setStyleSheet(open("src/view/assets/styles/login/telaLogin.css").read())

        # Definição do layout
        loginLayout = QtWidgets.QVBoxLayout()
        loginLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(loginLayout)

        # QFrame (fundo)
        fundo = QtWidgets.QFrame(self)
        fundo.setObjectName("fundo")
        loginLayout.addWidget(fundo)

        fundoLayout = QtWidgets.QVBoxLayout()
        fundoLayout.setContentsMargins(30, 40, 30, 40)
        fundoLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        fundo.setLayout(fundoLayout)

        # QFrame (fundoFormulario)
        fundoFormulario = QtWidgets.QFrame(fundo)
        fundoFormulario.setObjectName("fundoFormulario")
        fundoFormulario.setMaximumSize(800, 900)
        fundoLayout.addWidget(fundoFormulario)

        fundoFormularioLayout = QtWidgets.QVBoxLayout()
        fundoFormularioLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        fundoFormularioLayout.setContentsMargins(30, 20, 30, 20)
        fundoFormulario.setLayout(fundoFormularioLayout)

        # QFrame (formularioLogin)
        formularioLogin = FormularioLogin(fundoFormulario)
        formularioLogin.setObjectName("formularioLogin")
        fundoFormularioLayout.addWidget(formularioLogin)

        # QFrame (registrar)
        self.formularioRegistro = FormularioRegistro(self)
        self.formularioRegistro.setObjectName("formularioRegistro")
        fundoFormularioLayout.addWidget(self.formularioRegistro)
