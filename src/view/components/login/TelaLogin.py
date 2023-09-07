from PyQt6 import QtWidgets
<<<<<<< HEAD
from src.view.components.login.subcomponents.Formulario import Formulario
from src.view.components.login.TelaRegistro import TelaRegistro

=======
from src.view.components.login.subcomponents.FormularioLogin import Formulario
>>>>>>> luan

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

        # QFrame (registrar)
        self.TelaRegistro = TelaRegistro(self)
        self.TelaRegistro.setObjectName("formulario")
        fundoLayout.addWidget(self.TelaRegistro)
