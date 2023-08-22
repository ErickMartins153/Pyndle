from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
import sys
from src.controller.telaInicial import checar


class Registrar(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()
        self.setParent(parent)
        self.setContentsMargins(165, 60, 160, 60)
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
        self.entradaSenha.setObjectName("caixaEntrada")
        self.entradasLayout.addWidget(self.entradaSenha)

        repetirSenhaLabel = QtWidgets.QLabel(entradasFrame)
        repetirSenhaLabel.setText("Repita sua senha")
        repetirSenhaLabel.setObjectName("labelCaixa")
        self.entradasLayout.addWidget(repetirSenhaLabel)

        self.repetirEntradaSenha = QtWidgets.QLineEdit(entradasFrame)
        self.repetirEntradaSenha.setObjectName("caixaEntrada")
        self.entradasLayout.addWidget(self.repetirEntradaSenha)

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

    # Funções

    def checarRegistro(self):
        usuario = self.entradaUsuario.text()
        senha = self.entradaSenha.text()
        repetirSenha = self.repetirEntradaSenha.text()

        if senha == repetirSenha:
            print(self.parent().parent().parent().objectName)
            self.parent().parent().parent().setCurrentIndex(1)
        else:
            if self.findChild(QtWidgets.QLabel, "repetirSenhaLabel") == None:
                repetirSenhaLabel = QtWidgets.QLabel(self)
                repetirSenhaLabel.setText("As senhas são diferentes")
                repetirSenhaLabel.setObjectName("repetirSenhaLabel")
                self.entradasLayout.addWidget(repetirSenhaLabel)

        try:
            status = checar(usuario, senha)
            if status is True:
                self.parent().parent().parent().setCurrentIndex(1)
            else:
                pass
        except IndexError:
            print("Usuário não encontrado")
