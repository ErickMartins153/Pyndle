from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
from src.controller import telaInicial


class TelaRegistro(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()
        self.setParent(parent)
        self.setContentsMargins(165, 60, 160, 30)
        self.hide()

        formLayout = QtWidgets.QVBoxLayout()
        formLayout.setSpacing(40)
        self.setLayout(formLayout)

        # LOGO -----------------------------------------
        logoFrame = QtWidgets.QFrame(self)
        logoFrame.setMinimumSize(200, 100)
        logoFrame.setMaximumSize(225, 111)
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
        self.entradasLayout = QtWidgets.QVBoxLayout(self)
        self.entradasLayout.setSpacing(5)
        entradasFrame.setLayout(self.entradasLayout)

        # elementos

        usuarioLabel = QtWidgets.QLabel(entradasFrame)
        usuarioLabel.setText("Usuário")
        usuarioLabel.setObjectName("labelCaixa")
        self.entradasLayout.addWidget(usuarioLabel)

        self.entradaUsuario = QtWidgets.QLineEdit(entradasFrame)
        self.entradaUsuario.setObjectName("caixaEntrada")
        self.entradasLayout.addWidget(self.entradaUsuario)

        senhaLabel = QtWidgets.QLabel(entradasFrame)
        senhaLabel.setText("Senha")
        senhaLabel.setObjectName("labelCaixa")
        self.entradasLayout.addWidget(senhaLabel)

        self.entradaSenha = QtWidgets.QLineEdit(entradasFrame)
        self.entradaSenha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.entradaSenha.setObjectName("caixaEntrada")
        self.entradasLayout.addWidget(self.entradaSenha)

        repetirSenhaLabel = QtWidgets.QLabel(entradasFrame)
        repetirSenhaLabel.setText("Repita sua senha")
        repetirSenhaLabel.setObjectName("labelCaixa")
        self.entradasLayout.addWidget(repetirSenhaLabel)

        self.entradaRepetirSenha = QtWidgets.QLineEdit(entradasFrame)
        self.entradaRepetirSenha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.entradaRepetirSenha.setObjectName("caixaEntrada")
        self.entradasLayout.addWidget(self.entradaRepetirSenha)

        # BOTÕES --------------------------
        # Frame
        botoesFrame = QtWidgets.QFrame(self)
        self.entradasLayout.addWidget(botoesFrame)
        botoesFrameLayout = QtWidgets.QVBoxLayout(botoesFrame)
        botoesFrame.setLayout(botoesFrameLayout)

        self.registrarBotao = QtWidgets.QPushButton(botoesFrame)
        self.registrarBotao.setText("Registrar")
        self.registrarBotao.setObjectName("registrarBotao")
        self.registrarBotao.clicked.connect(self.checarRegistro)
        botoesFrameLayout.addWidget(self.registrarBotao)

        self.telaLoginBotao = QtWidgets.QPushButton(botoesFrame)
        self.telaLoginBotao.setText("Tela de Login")
        self.telaLoginBotao.setObjectName("voltarLoginBotao")
        self.telaLoginBotao.clicked.connect(self.voltarTelaLogin)
        botoesFrameLayout.addWidget(self.telaLoginBotao)

    # Funções

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
            if telaInicial.registrarUsuario(usuario, senha) is True:
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
        self.hide()
        formulario = self.parent().parent().findChild(QtWidgets.QFrame, "formulario")
        formulario.show()

    def printarMensagemDeErro(self, mensagem):
        """
        printar um caixa com a mensagem de erro inserida, garantindo que apenas \n
        uma caixa aparece
        """
        labelExistente = self.findChild(QtWidgets.QLabel, "mensagemDeErro")
        if labelExistente != None:
            labelExistente.setText(mensagem)
            return
        mensagemDeErroLabel = QtWidgets.QLabel(self)
        mensagemDeErroLabel.setText(mensagem)
        mensagemDeErroLabel.setObjectName("mensagemDeErro")
        mensagemDeErroLabel.setStyleSheet(
            "QLabel#mensagemDeErro {border-radius: 10px;}"
        )
        mensagemDeErroLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entradasLayout.addWidget(mensagemDeErroLabel)

    def limparLabelMensagemDeErro(self):
        labelExistente = self.findChild(QtWidgets.QLabel, "mensagemDeErro")
        if labelExistente != None:
            labelExistente.deleteLater()
            return
