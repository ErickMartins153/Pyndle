from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
from src.view.components.Logo import Logo
from src.view.components.login.subcomponents.FotoPerfil import FotoPerfil
from src.controller import telaInicial
from src.view.utils import widgetSearch


class FormularioRegistro(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()
        # Atributos
        self.binaryFoto = b""

        # Configurações
        self.setParent(parent)
        self.setContentsMargins(20, 40, 20, 60)
        self.hide()
        self.setAcceptDrops(True)

        formLayout = QtWidgets.QVBoxLayout()
        formLayout.setSpacing(20)
        self.setLayout(formLayout)

        # LOGO -----------------------------------------

        self.logo = Logo(240, 100)
        self.logo.setObjectName("logo")
        self.logo.setMinimumHeight(100)
        self.logo.setMaximumHeight(100)
        formLayout.addWidget(self.logo)

        # ENTRADAS -------------------------------------
        # Foto de perfil
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.foto = FotoPerfil()
        self.foto.setAcceptDrops(True)
        self.tornarFotoPerfilPadrao()
        self.foto.setMaximumHeight(100)
        layout.addWidget(self.foto)
        formLayout.addLayout(layout)

        # LABEL ERRO
        mensagemErroLayout = QtWidgets.QHBoxLayout()
        formLayout.addLayout(mensagemErroLayout)

        self.mensagemDeErroLabel = QtWidgets.QLabel(" ")
        self.mensagemDeErroLabel.setMaximumSize(300, 25)
        self.mensagemDeErroLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        mensagemErroLayout.addWidget(self.mensagemDeErroLabel)

        # Frame das entradas
        entradasFrame = QtWidgets.QFrame(self)
        entradasFrame.setMinimumHeight(400)
        formLayout.addWidget(entradasFrame)
        self.entradasLayout = QtWidgets.QVBoxLayout(self)
        self.entradasLayout.setSpacing(10)
        self.entradasLayout.setContentsMargins(150, 0, 150, 0)
        entradasFrame.setLayout(self.entradasLayout)

        # elementos

        entradasHeight = 40
        espacoLabelEntrada = 30

        groupUsuario = QtWidgets.QVBoxLayout()
        groupUsuario.setSpacing(5)
        self.entradasLayout.addLayout(groupUsuario)

        usuarioLabel = QtWidgets.QLabel(entradasFrame)
        usuarioLabel.setObjectName("labelCaixa")
        usuarioLabel.setText("Usuário")
        usuarioLabel.setMaximumHeight(espacoLabelEntrada)
        groupUsuario.addWidget(usuarioLabel)

        self.entradaUsuario = QtWidgets.QLineEdit(entradasFrame)
        self.entradaUsuario.setObjectName("caixaEntrada")
        self.entradaUsuario.setMaximumHeight(entradasHeight)
        groupUsuario.addWidget(self.entradaUsuario)

        groupSenha = QtWidgets.QVBoxLayout()
        groupSenha.setSpacing(5)
        self.entradasLayout.addLayout(groupSenha)

        senhaLabel = QtWidgets.QLabel(entradasFrame)
        senhaLabel.setObjectName("labelCaixa")
        senhaLabel.setMaximumHeight(espacoLabelEntrada)
        senhaLabel.setText("Senha")
        groupSenha.addWidget(senhaLabel)

        self.entradaSenha = QtWidgets.QLineEdit(entradasFrame)
        self.entradaSenha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.entradaSenha.setObjectName("caixaEntrada")
        self.entradaSenha.setMaximumHeight(entradasHeight)
        groupSenha.addWidget(self.entradaSenha)

        groupRepetirSenha = QtWidgets.QVBoxLayout()
        groupRepetirSenha.setSpacing(5)
        self.entradasLayout.addLayout(groupRepetirSenha)

        repetirSenhaLabel = QtWidgets.QLabel(entradasFrame)
        repetirSenhaLabel.setObjectName("labelCaixa")
        repetirSenhaLabel.setText("Repita sua senha")
        repetirSenhaLabel.setMaximumHeight(espacoLabelEntrada)
        groupRepetirSenha.addWidget(repetirSenhaLabel)

        self.entradaRepetirSenha = QtWidgets.QLineEdit(entradasFrame)
        self.entradaRepetirSenha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.entradaRepetirSenha.setObjectName("caixaEntrada")
        self.entradaRepetirSenha.setMinimumHeight(entradasHeight)
        groupRepetirSenha.addWidget(self.entradaRepetirSenha)

        # BOTÕES --------------------------
        # Frame
        botoesFrame = QtWidgets.QFrame(self)
        self.entradasLayout.addWidget(botoesFrame)

        botoesFrameLayout = QtWidgets.QVBoxLayout(botoesFrame)
        botoesFrameLayout.setContentsMargins(80, 0, 80, 0)
        botoesFrameLayout.setSpacing(10)
        botoesFrame.setLayout(botoesFrameLayout)

        self.registrarBotao = QtWidgets.QPushButton(botoesFrame)
        self.registrarBotao.setObjectName("registrarBotao")
        self.registrarBotao.setMinimumHeight(50)
        self.registrarBotao.setText("Registrar")
        self.registrarBotao.clicked.connect(self.checarRegistro)
        botoesFrameLayout.addWidget(self.registrarBotao)

        self.telaLoginBotao = QtWidgets.QPushButton(botoesFrame)
        self.telaLoginBotao.setObjectName("logarBotao")
        self.telaLoginBotao.setMinimumHeight(50)
        self.telaLoginBotao.setText("Tela de Login")
        self.telaLoginBotao.clicked.connect(self.voltarTelaLogin)
        botoesFrameLayout.addWidget(self.telaLoginBotao)

    # Funções ------------------------------------------------------------
    def checarRegistro(self):
        """
        Checa se usuário/senha/repetir senha existem, se o usuário já consta no banco de dados \n
        e se as senhas são iguais
        """
        usuario = self.entradaUsuario.text()
        senha = self.entradaSenha.text()
        repetirSenha = self.entradaRepetirSenha.text()
        if senha == "" or usuario == "" or repetirSenha == "":
            return
        if senha == repetirSenha:
            if telaInicial.registrarUsuario(usuario, senha, self.binaryFoto) is True:
                self.limparLabelMensagemDeErro()
                self.voltarTelaLogin()
            else:
                self.printarMensagemDeErro("Usuário Já Cadastrado")
        else:
            self.printarMensagemDeErro("As senhas são diferentes")
            return

    def voltarTelaLogin(self):
        """
        voltar para a tela de login, limpando todos os inputs de login e senha previamente \n
        inseridos
        """
        self.entradaSenha.clear()
        self.entradaUsuario.clear()
        self.entradaRepetirSenha.clear()
        self.limparLabelMensagemDeErro()
        self.tornarFotoPerfilPadrao()

        self.hide()
        widgetSearch.getIrmaos(self)["formularioLogin"].show()

    def printarMensagemDeErro(self, mensagem):
        """
        printar um caixa com a mensagem de erro inserida, garantindo que apenas \n
        uma caixa aparece
        """
        if self.mensagemDeErroLabel.text().isspace():
            self.mensagemDeErroLabel.setObjectName("mensagemDeErro")
            self.setStyleSheet(open("src/view/assets/styles/login/telaLogin.css").read())

        self.mensagemDeErroLabel.setText(mensagem)

    def limparLabelMensagemDeErro(self):
        self.mensagemDeErroLabel.setText(" ")
        self.mensagemDeErroLabel.setObjectName(" ")
        self.setStyleSheet(open("src/view/assets/styles/login/telaLogin.css").read())

    def tornarFotoPerfilPadrao(self):
        """
        Função para deixar a foto do perfil como não definida
        """
        self.foto.removePhoto()
        self.binaryFoto = b""
        self.foto.setStyleSheet("""
        image: url("src/view/assets/icons/FotoNaoDefinida.svg");
        width: 100px;
        height: 100px;
        background-color: transparent;
        """)

    # Eventos ----------------------------------------------------------

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.DropAction.CopyAction)
            event.mimeData().urls()[0].toLocalFile()

            with open(f"{event.mimeData().urls()[0].toLocalFile()}", "rb") as arquivos:
                newBimage = arquivos.read()

            # Define o atributo binaryFoto com o diretório da foto recebida
            self.binaryFoto = newBimage

            self.foto.setStyleSheet("""
            background-color: transparent;
            """)
            self.foto.changePhoto(newBimage)
            # self.foto.resizePhoto(1, 1)
            event.accept()

        else:
            event.ignore()
