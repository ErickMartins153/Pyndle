from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from src.view.components.Logo import Logo
from src.view.components.FotoPerfil import FotoPerfil
from src.controller import telaInicial
from src.view.utils import widgetSearch
from src.view.utils.imageTools import relHeight, relWidth

import pyautogui

tela = pyautogui.size()
width, height = tela


class FormularioRegistro(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()
        # Atributos
        self.binaryFoto = b""

        # Configurações
        self.setParent(parent)
        self.setContentsMargins(
            relWidth(20, 1920),
            relHeight(40, 1080),
            relWidth(20, 1920),
            relHeight(60, 1080),
        )
        self.hide()
        self.setAcceptDrops(True)

        formLayout = QtWidgets.QVBoxLayout()
        formLayout.setSpacing(relHeight(20, 1080))
        self.setLayout(formLayout)

        # LOGO -----------------------------------------

        # self.logo = Logo(240, 100)
        self.logo = Logo(relWidth(240, 1920), relHeight(100, 1080), relHeight(30, 1080))
        self.logo.setObjectName("logo")
        self.logo.setFixedHeight(relHeight(100, 1080))
        formLayout.addWidget(self.logo)

        # ENTRADAS -------------------------------------
        # Foto de perfil
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.foto = FotoPerfil()
        self.foto.setAcceptDrops(True)
        self.tornarFotoPerfilPadrao()
        self.foto.setMaximumHeight(relHeight(100, 1080))
        layout.addWidget(self.foto)
        formLayout.addLayout(layout)

        # LABEL ERRO
        mensagemErroLayout = QtWidgets.QHBoxLayout()
        formLayout.addLayout(mensagemErroLayout)

        self.mensagemDeErroLabel = QtWidgets.QLabel(" ")
        self.mensagemDeErroLabel.setMaximumSize(
            relWidth(300, 1920), relHeight(25, 1080)
        )
        self.mensagemDeErroLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        mensagemErroLayout.addWidget(self.mensagemDeErroLabel)

        # Frame das entradas
        entradasFrame = QtWidgets.QFrame(self)
        entradasFrame.setMinimumHeight(relHeight(400, 1080))
        formLayout.addWidget(entradasFrame)
        self.entradasLayout = QtWidgets.QVBoxLayout(self)
        self.entradasLayout.setSpacing(relHeight(10, 1080))
        self.entradasLayout.setContentsMargins(
            relWidth(150, 1920), 0, relWidth(150, 1920), 0
        )
        entradasFrame.setLayout(self.entradasLayout)

        # elementos

        entradasHeight = relHeight(40, 1080)
        espacoLabelEntrada = relHeight(30, 1080)

        groupUsuario = QtWidgets.QVBoxLayout()
        groupUsuario.setSpacing(relHeight(5, 1080))
        self.entradasLayout.addLayout(groupUsuario)

        usuarioLabel = QtWidgets.QLabel(entradasFrame)
        usuarioLabel.setObjectName("labelCaixa")
        usuarioLabel.setStyleSheet(f"font-size: {relHeight(30, 1080)}px")
        usuarioLabel.setText("Usuário")
        usuarioLabel.setMaximumHeight(espacoLabelEntrada)
        groupUsuario.addWidget(usuarioLabel)

        self.entradaUsuario = QtWidgets.QLineEdit(entradasFrame)
        self.entradaUsuario.setObjectName("caixaEntrada")
        self.entradaUsuario.setStyleSheet(
            f"""
        font-size: {relHeight(25, 1080)};
        border-radius: {relHeight(20, 1080)}px;
        padding: {relHeight(2, 1080)}px {relWidth(10, 1920)}px;
        """
        )
        self.entradaUsuario.setMaximumHeight(entradasHeight)
        groupUsuario.addWidget(self.entradaUsuario)

        groupSenha = QtWidgets.QVBoxLayout()
        groupSenha.setSpacing(relHeight(5, 1080))
        self.entradasLayout.addLayout(groupSenha)

        senhaLabel = QtWidgets.QLabel(entradasFrame)
        senhaLabel.setObjectName("labelCaixa")
        senhaLabel.setMaximumHeight(espacoLabelEntrada)
        senhaLabel.setText("Senha")
        groupSenha.addWidget(senhaLabel)

        self.entradaSenha = QtWidgets.QLineEdit(entradasFrame)
        self.entradaSenha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.entradaSenha.setObjectName("caixaEntrada")
        self.entradaSenha.setStyleSheet(
            f"""
                font-size: {relHeight(25, 1080)};
                border-radius: {relHeight(20, 1080)}px;
                padding: {relHeight(2, 1080)}px {relWidth(10, 1920)}px;
        """
        )
        self.entradaSenha.setMaximumHeight(entradasHeight)
        groupSenha.addWidget(self.entradaSenha)

        groupRepetirSenha = QtWidgets.QVBoxLayout()
        groupRepetirSenha.setSpacing(relHeight(5, 1080))
        self.entradasLayout.addLayout(groupRepetirSenha)

        repetirSenhaLabel = QtWidgets.QLabel(entradasFrame)
        repetirSenhaLabel.setObjectName("labelCaixa")
        repetirSenhaLabel.setStyleSheet(f"font-size: {relHeight(30, 1080)}px")
        repetirSenhaLabel.setText("Repita sua senha")
        repetirSenhaLabel.setMaximumHeight(espacoLabelEntrada)
        groupRepetirSenha.addWidget(repetirSenhaLabel)

        self.entradaRepetirSenha = QtWidgets.QLineEdit(entradasFrame)
        self.entradaRepetirSenha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.entradaRepetirSenha.setObjectName("caixaEntrada")
        self.entradaRepetirSenha.setStyleSheet(
            f"""
                font-size: {relHeight(25, 1080)};
                border-radius: {relHeight(20, 1080)}px;
                padding: {relHeight(2, 1080)}px {relWidth(10, 1920)}px;
        """
        )
        self.entradaRepetirSenha.setMaximumHeight(entradasHeight)
        groupRepetirSenha.addWidget(self.entradaRepetirSenha)

        # BOTÕES --------------------------
        # Frame
        botoesFrame = QtWidgets.QFrame(self)
        self.entradasLayout.addWidget(botoesFrame)

        botoesFrameLayout = QtWidgets.QVBoxLayout(botoesFrame)
        botoesFrameLayout.setContentsMargins(80, 0, 80, 0)
        botoesFrameLayout.setContentsMargins(
            relWidth(80, 1920), 0, relWidth(80, 1920), 0
        )
        botoesFrameLayout.setSpacing(relHeight(10, 1080))
        botoesFrame.setLayout(botoesFrameLayout)

        self.registrarBotao = QtWidgets.QPushButton(botoesFrame)
        self.registrarBotao.setObjectName("registrarBotao")
        self.registrarBotao.setStyleSheet(
            f"""
        border-radius: {relHeight(25, 1080)}px;
        font-size: {relHeight(30, 1080)}px;
        """
        )
        self.registrarBotao.setMinimumHeight(relHeight(50, 1080))
        self.registrarBotao.setText("Registrar")
        self.registrarBotao.clicked.connect(self.checarRegistro)
        botoesFrameLayout.addWidget(self.registrarBotao)

        self.telaLoginBotao = QtWidgets.QPushButton(botoesFrame)
        self.telaLoginBotao.setObjectName("logarBotao")
        self.telaLoginBotao.setStyleSheet(
            f"""
        border-radius: {relHeight(25, 1080)}px;
        font-size: {relHeight(30, 1080)}px;
        """
        )
        self.telaLoginBotao.setMinimumHeight(relHeight(50, 1080))
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
        if telaInicial.checar(usuario):
            self.printarMensagemDeErro("O usuário já existe 😢")
            return

        if senha == repetirSenha:
            if telaInicial.registrarUsuario(usuario, senha, self.binaryFoto) is True:
                self.limparLabelMensagemDeErro()
                self.voltarTelaLogin()
        else:
            self.printarMensagemDeErro("As senhas são diferentes 🤦‍♀️")
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
            self.setStyleSheet(
                open("src/view/assets/styles/login/telaLogin.css").read()
            )

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
        self.foto.setStyleSheet(
            """
        image: url("src/view/assets/icons/FotoNaoDefinida.svg");
        width: 100px;
        height: 100px;
        background-color: transparent;
        """
        )

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
            self.foto.changePhoto(newBimage, 100)
            event.accept()

        else:
            event.ignore()
