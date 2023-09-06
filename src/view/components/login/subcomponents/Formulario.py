from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from src.controller import telaInicial
from src.view.components.login.TelaRegistro import TelaRegistro
from src.view.utils import widgetSearch


class Formulario(QtWidgets.QFrame):
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
        self.setContentsMargins(173, 60, 173, 115)

        # Definição do layout do formulário
        formLayout = QtWidgets.QVBoxLayout()
        formLayout.setSpacing(40)
        formLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(formLayout)

        # LOGO -----------------------------------------
        logoFrame = QtWidgets.QFrame(self)
        logoFrame.setMinimumSize(200, 100)
        logoFrame.setMaximumSize(600, 300)
        logoFrame.setObjectName("logoFrame")
        formLayout.addWidget(logoFrame)

        fundoLogoLayout = QtWidgets.QHBoxLayout()
        fundoLogoLayout.setContentsMargins(5, 0, 5, 0)
        fundoLogoLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        logoFrame.setLayout(fundoLogoLayout)

        pyndleLogo = QtWidgets.QLabel(logoFrame)
        pyndleLogo.setObjectName("pyndleLogo")
        pyndleLogo.setText("Pyndle")
        fundoLogoLayout.addWidget(pyndleLogo)

        # ENTRADAS -------------------------------------
        # Frame
        entradasFrame = QtWidgets.QFrame(self)
        formLayout.addWidget(entradasFrame)
        entradasLayout = QtWidgets.QVBoxLayout(self)
        entradasLayout.setSpacing(5)
        entradasFrame.setLayout(entradasLayout)

        # elementos

        usuarioLabel = QtWidgets.QLabel(entradasFrame)
        usuarioLabel.setText("Usuário")
        usuarioLabel.setObjectName("labelCaixa")
        entradasLayout.addWidget(usuarioLabel)

        self.entradaUsuario = QtWidgets.QLineEdit(entradasFrame)
        self.entradaUsuario.setObjectName("caixaEntrada")
        entradasLayout.addWidget(self.entradaUsuario)

        senhaLabel = QtWidgets.QLabel(entradasFrame)
        senhaLabel.setText("Senha")
        senhaLabel.setObjectName("labelCaixa")
        entradasLayout.addWidget(senhaLabel)

        self.entradaSenha = QtWidgets.QLineEdit(entradasFrame)
        self.entradaSenha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.entradaSenha.setObjectName("caixaEntrada")
        entradasLayout.addWidget(self.entradaSenha)

        # BOTÕES --------------------------
        # Frame
        botoesFrame = QtWidgets.QFrame(self)
        entradasLayout.addWidget(botoesFrame)
        botoesFrameLayout = QtWidgets.QVBoxLayout(botoesFrame)
        botoesFrame.setLayout(botoesFrameLayout)

        self.logarBotao = QtWidgets.QPushButton(botoesFrame)
        self.logarBotao.setText("Logar")
        self.logarBotao.clicked.connect(self.logarBotaoCliclado)
        self.logarBotao.setObjectName("logarBotao")
        botoesFrameLayout.addWidget(self.logarBotao)

        self.registrarBotao = QtWidgets.QPushButton(botoesFrame)
        self.registrarBotao.setText("Registrar")
        self.registrarBotao.setObjectName("registrarBotao")
        self.registrarBotao.clicked.connect(self.registrarBotaoClicado)
        botoesFrameLayout.addWidget(self.registrarBotao)

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
                # Onde as páginas são guardadas
                stackedWidget = widgetSearch.getAncestrais(self)["paginas"]
                # Define o nome de usuário no "bem vindo" da tela principal
                widgetSearch.getDescendentes(stackedWidget)[
                    "fundoDashboard"
                ].setNomeUsuario(usuario)
                stackedWidget.setCurrentIndex(1)  # Muda para a página principal
                mainWindow.setUsuario(
                    telaInicial.getTuplaUsuario(usuario)
                )  # Define o usuário principal com as informações na mainWindow
            else:
                pass
        except IndexError:
            print("Usuário não encontrado")

    def registrarBotaoClicado(self):
        self.entradaSenha.clear()
        self.entradaUsuario.clear()
        self.hide()
        self.parent().findChild(TelaRegistro).show()
