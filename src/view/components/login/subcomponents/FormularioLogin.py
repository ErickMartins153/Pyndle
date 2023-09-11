from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import Qt
from src.view.components.Logo import Logo
from src.controller import telaInicial
from src.view.utils import widgetSearch
from src.view.utils import imageTools
from src.view.utils.imageTools import relHeight, relWidth


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
        self.setContentsMargins(relWidth(20, 1920), relHeight(60, 1080), relWidth(20, 1920), relHeight(60, 1080))

        # Definição do layout do formulário
        formLayout = QtWidgets.QVBoxLayout()
        formLayout.setSpacing(relHeight(40, 1080))
        formLayout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.setLayout(formLayout)


        # LOGO -----------------------------------------
        #480x200
        self.logo = Logo(relWidth(480, 1920), relHeight(200, 1080))
        self.logo.setObjectName("logo")
        self.logo.setFixedHeight(relHeight(200, 1080))
        formLayout.addWidget(self.logo)


        # ENTRADAS -------------------------------------

        # Frame

        entradasFrame = QtWidgets.QFrame(self)
        entradasFrame.setMinimumHeight(relHeight(400, 1080))
        formLayout.addWidget(entradasFrame)

        entradasLayout = QtWidgets.QVBoxLayout(self)
        entradasLayout.setContentsMargins(relWidth(150, 1920), 0, relWidth(150, 1920), 0)
        entradasLayout.setSpacing(relHeight(25, 1080))
        entradasFrame.setLayout(entradasLayout)

        # elementos

        entradasHeight = relHeight(40, 1080)
        espacoLabelEntrada = relHeight(30, 1080)

        groupUsuario = QtWidgets.QVBoxLayout()
        groupUsuario.setSpacing(relHeight(5, 1080))
        entradasLayout.addLayout(groupUsuario)

        usuarioLabel = QtWidgets.QLabel(entradasFrame)
        usuarioLabel.setText("Usuário")
        usuarioLabel.setStyleSheet(f"font-size: {relHeight(30, 1080)}px")
        usuarioLabel.setMaximumHeight(espacoLabelEntrada)
        usuarioLabel.setObjectName("labelCaixa")
        groupUsuario.addWidget(usuarioLabel)

        self.entradaUsuario = QtWidgets.QLineEdit(entradasFrame)
        self.entradaUsuario.setMinimumHeight(entradasHeight)
        self.entradaUsuario.setObjectName("caixaEntrada")
        self.entradaUsuario.setStyleSheet(f"""
        font-size: {relHeight(25, 1080)};
        border-radius: {relHeight(20, 1080)}px;
        padding: {relHeight(2, 1080)}px {relWidth(10, 1920)}px;
        """)
        groupUsuario.addWidget(self.entradaUsuario)

        groupSenha = QtWidgets.QVBoxLayout()
        groupSenha.setSpacing(relHeight(5, 1080))
        entradasLayout.addLayout(groupSenha)

        senhaLabel = QtWidgets.QLabel(entradasFrame)
        senhaLabel.setText("Senha")
        senhaLabel.setMaximumHeight(espacoLabelEntrada)
        senhaLabel.setObjectName("labelCaixa")
        senhaLabel.setStyleSheet(f"font-size: {relHeight(30, 1080)}px")
        groupSenha.addWidget(senhaLabel)

        self.entradaSenha = QtWidgets.QLineEdit(entradasFrame)
        self.entradaSenha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.entradaSenha.returnPressed.connect(self.logarBotaoCliclado)
        self.entradaSenha.setObjectName("caixaEntrada")
        self.entradaSenha.setStyleSheet(f"""
        font-size: {relHeight(25, 1080)};
        border-radius: {relHeight(20, 1080)}px;
        padding: {relHeight(2, 1080)}px {relWidth(10, 1920)}px;
        """)
        self.entradaSenha.setMinimumHeight(entradasHeight)
        self.entradaSenha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        groupSenha.addWidget(self.entradaSenha)

        # BOTÕES --------------------------

        # Frame
        botoesFrame = QtWidgets.QFrame(self)
        botoesFrameLayout = QtWidgets.QVBoxLayout(botoesFrame)
        botoesFrameLayout.setContentsMargins(relWidth(80, 1920), relHeight(10, 1080), relWidth(80, 1920), relHeight(10, 1080))
        botoesFrameLayout.setSpacing(relHeight(10, 1080))
        botoesFrame.setLayout(botoesFrameLayout)
        entradasLayout.addWidget(botoesFrame)

        self.logarBotao = QtWidgets.QPushButton(botoesFrame)
        self.logarBotao.setObjectName("logarBotao")
        self.logarBotao.setStyleSheet(f"""
        border-radius: {relHeight(25, 1080)}px;
        font-size: {relHeight(30, 1080)}px;
        """)
        self.logarBotao.setMinimumHeight(relHeight(50, 1080))
        self.logarBotao.setText("Logar")
        self.logarBotao.clicked.connect(self.logarBotaoCliclado)
        botoesFrameLayout.addWidget(self.logarBotao)

        self.registrarBotao = QtWidgets.QPushButton(botoesFrame)
        self.registrarBotao.setObjectName(f"registrarBotao")
        self.registrarBotao.setStyleSheet(f"""
        border-radius: {relHeight(25, 1080)}px;
        font-size: {relHeight(30, 1080)}px;
        """)
        self.registrarBotao.setMinimumHeight(relHeight(50, 1080))
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
