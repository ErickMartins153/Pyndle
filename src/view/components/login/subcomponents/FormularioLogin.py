from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import Qt
from src.view.components.Logo import Logo
from src.controller import telaInicial
from src.view.utils import widgetSearch
from src.view.utils import imageTools


class FormularioLogin(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget):
        """
        QFrame constituido pelos widgets que serão preenchidos com as informações para logar ou registrar

        :param parent: Define o parente do widget

        Métodos:
            - logarBotaoCliclado(): verifica o usuário e muda para a tela principal
        """
        # Configurações

        super().__init__()
        self.setParent(parent)
        self.setContentsMargins(20, 60, 20, 60)

        # Definição do layout do formulário
        formLayout = QtWidgets.QVBoxLayout()
        formLayout.setSpacing(40)
        #formLayout.setContentsMargins(0, 0, 0, 40)
        formLayout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.setLayout(formLayout)


        # LOGO -----------------------------------------

        self.logo = Logo(480, 200)
        self.logo.setObjectName("logo")
        self.logo.setMinimumHeight(200)
        self.logo.setMaximumHeight(200)
        formLayout.addWidget(self.logo)


        # ENTRADAS -------------------------------------

        # Frame

        entradasFrame = QtWidgets.QFrame(self)
        entradasFrame.setMinimumHeight(400)
        formLayout.addWidget(entradasFrame)

        entradasLayout = QtWidgets.QVBoxLayout(self)
        entradasLayout.setContentsMargins(150, 0, 150, 0)
        entradasLayout.setSpacing(25)
        entradasFrame.setLayout(entradasLayout)

        # elementos

        entradasHeight = 40
        espacoLabelEntrada = 30

        groupUsuario = QtWidgets.QVBoxLayout()
        groupUsuario.setSpacing(5)
        entradasLayout.addLayout(groupUsuario)

        usuarioLabel = QtWidgets.QLabel(entradasFrame)
        usuarioLabel.setText("Usuário")
        usuarioLabel.setMaximumHeight(espacoLabelEntrada)
        usuarioLabel.setObjectName("labelCaixa")
        groupUsuario.addWidget(usuarioLabel)

        self.entradaUsuario = QtWidgets.QLineEdit(entradasFrame)
        self.entradaUsuario.setMinimumHeight(entradasHeight)
        self.entradaUsuario.setObjectName("caixaEntrada")
        groupUsuario.addWidget(self.entradaUsuario)

        groupSenha = QtWidgets.QVBoxLayout()
        groupSenha.setSpacing(5)
        entradasLayout.addLayout(groupSenha)

        senhaLabel = QtWidgets.QLabel(entradasFrame)
        senhaLabel.setText("Senha")
        senhaLabel.setMaximumHeight(espacoLabelEntrada)
        senhaLabel.setObjectName("labelCaixa")
        groupSenha.addWidget(senhaLabel)

        self.entradaSenha = QtWidgets.QLineEdit(entradasFrame)
        self.entradaSenha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.entradaSenha.returnPressed.connect(self.logarBotaoCliclado)
        self.entradaSenha.setObjectName("caixaEntrada")
        self.entradaSenha.setMaximumHeight(entradasHeight)
        self.entradaSenha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        groupSenha.addWidget(self.entradaSenha)

        # BOTÕES --------------------------

        # Frame
        botoesFrame = QtWidgets.QFrame(self)
        botoesFrameLayout = QtWidgets.QVBoxLayout(botoesFrame)
        botoesFrameLayout.setContentsMargins(80, 10, 80, 10)
        botoesFrameLayout.setSpacing(10)
        botoesFrame.setLayout(botoesFrameLayout)
        entradasLayout.addWidget(botoesFrame)

        self.logarBotao = QtWidgets.QPushButton(botoesFrame)
        self.logarBotao.setObjectName("logarBotao")
        self.logarBotao.setMinimumHeight(50)
        self.logarBotao.setText("Logar")
        self.logarBotao.clicked.connect(self.logarBotaoCliclado)
        botoesFrameLayout.addWidget(self.logarBotao)

        self.registrarBotao = QtWidgets.QPushButton(botoesFrame)
        self.registrarBotao.setObjectName("registrarBotao")
        self.registrarBotao.setMinimumHeight(50)
        self.registrarBotao.setText("Registrar")
        self.registrarBotao.clicked.connect(self.registrarBotaoClicado)
        botoesFrameLayout.addWidget(self.registrarBotao)


    # Métodos

    def logarBotaoCliclado(self):
        """
        - Verifica se as informações de login e senha correspondem a algum usuário registrado no banco de dados\n
        - Depois muda para a tela principal da aplicação
        """
        usuario = self.entradaUsuario.text()
        senha = self.entradaSenha.text()

        try:
            status = telaInicial.checar(usuario, senha)
            if status is True:

                # mainWindow para definir o usuario
                mainWindow = widgetSearch.getAncestrais(self)["mainWindow"]
                mainWindow.setUsuario(telaInicial.getTuplaUsuario(usuario))
                # Mudando para a tela principal
                widgetSearch.getAncestrais(self)["paginas"].setCurrentIndex(1)
                # Define o nome de usuário no "bem vindo" da tela principal
                widgetSearch.getDescendentes(mainWindow)["fundoDashboard"].setNomeUsuario(usuario)

            else:
                pass
        except IndexError:
            print("Usuário não encontrado")

    def registrarBotaoClicado(self):
        self.entradaSenha.clear()
        self.entradaUsuario.clear()
        self.hide()
        widgetSearch.getIrmaos(self)["formularioRegistro"].show()
