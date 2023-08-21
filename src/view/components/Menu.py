from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
import sys


class Menu(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget):
        """
        Widget utilizado para modelar o Menu/NavBar do aplicativo

        :param parent: Define o parente do widget
        """

        super().__init__()
        self.setParent(parent)
        self.setStyleSheet(open("src/view/assets/styles/menu.css").read())
        self.setMaximumHeight(70)

        menuLayout = QtWidgets.QHBoxLayout()
        menuLayout.setContentsMargins(20, 15, 20, 15)
        self.setLayout(menuLayout)

        # Logo -------------------------------
        fundoLogo = QtWidgets.QFrame(self)
        fundoLogo.setObjectName("fundoLogo")
        menuLayout.addWidget(fundoLogo)

        fundoLogoLayout = QtWidgets.QHBoxLayout()
        fundoLogoLayout.setContentsMargins(5, 0, 5, 0)
        fundoLogoLayout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        fundoLogo.setLayout(fundoLogoLayout)

        pyndleLogo = QtWidgets.QLabel(fundoLogo)
        pyndleLogo.setObjectName("pyndleLogo")
        pyndleLogo.setText("Pyndle")
        fundoLogoLayout.addWidget(pyndleLogo)

        # Distancia1 ----------------------------
        distancia1 = QtWidgets.QSpacerItem(40, 40)
        menuLayout.addSpacerItem(distancia1)

        # QLineEdit (Barra Pesquisa) ------------
        pesquisa = QtWidgets.QLineEdit()
        menuLayout.addWidget(pesquisa)

        pesquisa.setObjectName("pesquisa")
        pesquisa.setMinimumSize(300, 25)
        pesquisa.setMaximumHeight(25)
        pesquisa.setPlaceholderText("Pesquisar")

        # Distancia2 ----------------------------
        distancia2 = QtWidgets.QSpacerItem(300, 40)
        menuLayout.addSpacerItem(distancia2)

        # Perfil
        botao = QtWidgets.QPushButton("Acessar Perfil")
        menuLayout.addWidget(botao)

        self.menu = QtWidgets.QMenu(self)
        deslogar = QtGui.QAction("Deslogar", self.menu)
        deslogar.triggered.connect(self.deslogar)
        self.menu.addAction("Deslogar")

        botao.pressed.connect(self.abrirMenu)

    def abrirMenu(self):
        self.menu.exec(
            self.sender().mapToGlobal(
                self.sender().rect().bottomLeft() + QtCore.QPoint(-15, 0)
            )
        )

    def deslogar(self):
        pass
