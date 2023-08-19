from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
import sys
from src.controller.login import logar


class Formulario(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()
        self.setParent(parent)
        self.setContentsMargins(173, 60, 173, 115)

        formLayout = QtWidgets.QVBoxLayout()
        formLayout.setSpacing(40)
        self.setLayout(formLayout)

        # LOGO -----------------------------------------
        logoFrame = QtWidgets.QFrame(self)
        logoFrame.setMinimumSize(200, 100)
        logoFrame.setMaximumSize(600, 300)
        logoFrame.setObjectName("logoFrame")
        formLayout.addWidget(logoFrame)

        fundoLogoLayout = QtWidgets.QHBoxLayout()
        fundoLogoLayout.setContentsMargins(5, 0, 5, 0)
        fundoLogoLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
        botoesFrameLayout.addWidget(self.registrarBotao)

    # Funções

    def logarBotaoCliclado(self):
        usuario = self.entradaUsuario.text()
        senha = self.entradaSenha.text()

        try:
            status = logar(usuario, senha)
            if status is True:
                self.parent().parent().parent().setCurrentIndex(1)
            else:
                pass
        except IndexError:
            print("Usuário não encontrado")
