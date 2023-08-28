from PyQt6 import QtWidgets
from src.view.components.login.subcomponents.Formulario import Formulario

class TelaLogin(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget):
        """
        Tela de login com os formulários de login e registro
        :param parent: define o parente do widget
        """
        # Configurações
        super().__init__()
        self.setParent(parent)
        self.setStyleSheet(open("src/view/assets/styles/telaLogin.css").read())

        # Definição do layout
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
        formulario = Formulario(fundo)
        formulario.setObjectName("formulario")
        fundoLayout.addWidget(formulario)
