from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QMessageBox
from src.view.components.Logo import Logo
from src.controller import telaInicial
from src.view.utils import widgetSearch
from src.view.utils.imageTools import relHeight, relWidth
from src.view.utils.container import verticalFrame


class FormularioLogin(QtWidgets.QFrame):
    # SINAIS
    AtualizacaoUsuario = pyqtSignal(str)

    def __init__(self, parent: QtWidgets.QWidget):
        """
        QFrame constituido pelos widgets que serão preenchidos com as informações para logar ou registrar

        :param parent: Define o parente do widget

        Métodos:
            - logarBotaoCliclado(): verifica o usuário e muda para a tela principal
        """

        # CONFIGURAÇÕES ----------------------------------------------------
        super().__init__()
        self.setParent(parent)
        self.setContentsMargins(
            relWidth(20, 1920),
            relHeight(60, 1080),
            relWidth(20, 1920),
            relHeight(60, 1080),
        )

        # LAYOUT ------------------------------------------------------------
        formLayout = QtWidgets.QVBoxLayout()
        formLayout.setSpacing(relHeight(40, 1080))
        formLayout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.setLayout(formLayout)


        # LOGO --------------------------------------------------------------

        self.logo = Logo(relWidth(480, 1920), relHeight(200, 1080), relHeight(30, 1080))
        self.logo.setObjectName("logo")
        self.logo.setFixedHeight(relHeight(200, 1080))
        formLayout.addWidget(self.logo)


        # CONTAINER DAS ENTRADAS -------------------------------------------------------------------

        entradasFrame = verticalFrame(self)
        entradasFrame.setMinimumHeight(relHeight(400, 1080))
        formLayout.addWidget(entradasFrame)

        entradasFrame.layout().setContentsMargins(
            relWidth(150, 1920),
            0,
            relWidth(150, 1920),
            0
        )
        entradasFrame.layout().setSpacing(relHeight(25, 1080))
        entradasFrame.setLayout(entradasFrame.layout())

        # TAMANHOS DAS ENTRADAS ---------------------------------------------------------------------

        entradasHeight = relHeight(40, 1080)
        espacoLabelEntrada = relHeight(30, 1080)


        # USUÁRIO ------------------------------------------------------------

        # Definindo layout para agrupar Label e Entrada
        groupUsuario = QtWidgets.QVBoxLayout()
        groupUsuario.setSpacing(relHeight(5, 1080))
        entradasFrame.layout().addLayout(groupUsuario)

        # Definindo label ("Usuário")
        usuarioLabel = QtWidgets.QLabel(entradasFrame)
        usuarioLabel.setText("Usuário")
        usuarioLabel.setStyleSheet(f"font-size: {relHeight(30, 1080)}px")
        usuarioLabel.setMaximumHeight(espacoLabelEntrada)
        usuarioLabel.setObjectName("labelCaixa")
        groupUsuario.addWidget(usuarioLabel)

        # Criando entrada de usuário
        self.entradaUsuario = QtWidgets.QLineEdit(entradasFrame)
        self.entradaUsuario.setFixedHeight(entradasHeight)
        self.entradaUsuario.setObjectName("caixaEntrada")
        self.entradaUsuario.setStyleSheet(f"""
            font-size: {relHeight(25, 1080)};
            border-radius: {relHeight(20, 1080)}px;
            padding: {relHeight(2, 1080)}px {relWidth(10, 1920)}px;
        """)
        groupUsuario.addWidget(self.entradaUsuario)


        # SENHA ---------------------------------------------------------------

        # Criando layout para agrupar label e entrada da senha
        groupSenha = QtWidgets.QVBoxLayout()
        groupSenha.setSpacing(relHeight(5, 1080))
        entradasFrame.layout().addLayout(groupSenha)

        # Definindo label ("senha")
        senhaLabel = QtWidgets.QLabel(entradasFrame)
        senhaLabel.setText("Senha")
        senhaLabel.setFixedHeight(espacoLabelEntrada)
        senhaLabel.setObjectName("labelCaixa")
        senhaLabel.setStyleSheet(f"font-size: {relHeight(30, 1080)}px")
        groupSenha.addWidget(senhaLabel)

        # Definindo entrada de senha
        self.entradaSenha = QtWidgets.QLineEdit(entradasFrame)
        self.entradaSenha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.entradaSenha.returnPressed.connect(self.logarBotaoCliclado)
        self.entradaSenha.setObjectName("caixaEntrada")
        self.entradaSenha.setStyleSheet(
            f"""
        font-size: {relHeight(25, 1080)};
        border-radius: {relHeight(20, 1080)}px;
        padding: {relHeight(2, 1080)}px {relWidth(10, 1920)}px;
        """
        )
        self.entradaSenha.setFixedHeight(entradasHeight)
        self.entradaSenha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        groupSenha.addWidget(self.entradaSenha)


        # BOTÕES --------------------------

        # CONTAINER (Onde os botões são agrupados) -------------------------------------
        botoesFrame = verticalFrame(self)

        botoesFrame.layout().setContentsMargins(
            relWidth(80, 1920),
            relHeight(10, 1080),
            relWidth(80, 1920),
            relHeight(10, 1080),
        )
        botoesFrame.layout().setSpacing(relHeight(10, 1080))

        entradasFrame.layout().addWidget(botoesFrame)

        # Definindo botão de login
        self.logarBotao = QtWidgets.QPushButton(botoesFrame)
        self.logarBotao.setObjectName("logarBotao")
        self.logarBotao.setStyleSheet(
            f"""
        border-radius: {relHeight(25, 1080)}px;
        font-size: {relHeight(30, 1080)}px;
        """
        )
        self.logarBotao.setMinimumHeight(relHeight(50, 1080))
        self.logarBotao.setText("Logar")
        self.logarBotao.clicked.connect(self.logarBotaoCliclado)
        botoesFrame.layout().addWidget(self.logarBotao)

        # Definindo botão de registro
        self.registrarBotao = QtWidgets.QPushButton(botoesFrame)
        self.registrarBotao.setObjectName(f"registrarBotao")
        self.registrarBotao.setStyleSheet(
            f"""
        border-radius: {relHeight(25, 1080)}px;
        font-size: {relHeight(30, 1080)}px;
        """
        )
        self.registrarBotao.setMinimumHeight(relHeight(50, 1080))
        self.registrarBotao.setText("Registrar")
        self.registrarBotao.clicked.connect(self.registrarBotaoClicado)
        botoesFrame.layout().addWidget(self.registrarBotao)


    # (MÉTODOS) -------------------------------------------------------

    def logarBotaoCliclado(self):
        """
        - Verifica se as informações de login e senha correspondem a algum usuário registrado no banco de dados\n
        - Depois muda para a tela principal da aplicação
        """
        usuario = self.entradaUsuario.text()
        senha = self.entradaSenha.text()

        try:
            status = telaInicial.checarLogin(usuario, senha)
            if status == 1:
                # mainWindow para definir o usuario
                mainWindow = widgetSearch.getAncestrais(self)["mainWindow"]
                mainWindow.setUsuario(telaInicial.dadosUsuario(usuario))
                # Mudando para a tela principal
                widgetSearch.getAncestrais(self)["paginas"].setCurrentIndex(1)
                # Define o nome de usuário no "bem vindo" da tela principal
                widgetSearch.getDescendentes(mainWindow)[
                    "fundoDashboard"
                ].setNomeUsuario(usuario)

                self.AtualizacaoUsuario.emit(usuario)
                self.entradaSenha.clear()
                self.entradaUsuario.clear()
            elif status == 0:
                QMessageBox.critical(self, "Erro", "Informe seu login")
            elif status == 2:
                QMessageBox.critical(self, "Erro", "Senha incompatível")
            elif status == 3:
                QMessageBox.critical(self, "Erro", "Informe seu login e senha")
            elif status == 4:
                QMessageBox.critical(self, "Erro", "Informe sua senha")
            elif status == 5:
                QMessageBox.critical(self, "Erro", "Usuário não cadastrado")
            elif status == 6:
                QMessageBox.critical(self, "Erro", "Usuário não cadastrado")

        except IndexError:
            pass


    def registrarBotaoClicado(self):
        """
        Limpa as caixas de entrada e muda para a tela de registro
        """

        # Limpando entradas
        self.entradaSenha.clear()
        self.entradaUsuario.clear()

        # Escondendo formulário de login
        self.hide()

        # Trocando para tela de registro
        widgetSearch.getIrmaos(self)["formularioRegistro"].show()
