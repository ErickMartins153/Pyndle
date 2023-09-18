from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from src.view.components.FotoPerfil import FotoPerfil
from src.controller.telaInicial import dadosUsuario
from src.view.utils.widgetSearch import getAncestrais, getDescendentes
from src.view.utils.imageTools import relHeight, relWidth
from src.view.components.Logo import Logo
from src.view.utils.widgetSearch import getAncestrais
import PIL


class Menu(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget):
        """
        Widget utilizado para modelar o Menu/NavBar do aplicativo

        :param parent: Define o parente do widget
        """

        super().__init__()
        self.setParent(parent)
        self.setStyleSheet(open("src/view/assets/styles/menu.css").read())
        self.setStyleSheet(open("src/view/assets/styles/menu.css").read())
        self.setMaximumHeight(70)

        menuLayout = QtWidgets.QHBoxLayout()
        # menuLayout.setContentsMargins(20, 15, 20, 15)
        self.setLayout(menuLayout)

        # Logo -------------------------------
        self.logo = Logo(relWidth(120, 1920), relHeight(50, 1080), relHeight(10, 1080))
        self.logo.setObjectName("logo")
        self.logo.setFixedHeight(relHeight(50, 1080))
        menuLayout.addWidget(self.logo)
        """
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
"""
        # Distancia1 ----------------------------
        distancia1 = QtWidgets.QSpacerItem(40, 40)
        menuLayout.addSpacerItem(distancia1)

        # QLineEdit (Barra Pesquisa) ------------
        pesquisa = QtWidgets.QLineEdit()
        menuLayout.addWidget(pesquisa)

        pesquisa.setObjectName("pesquisa")
        pesquisa.setMinimumSize(200, 37)
        pesquisa.setMaximumHeight(37)
        pesquisa.setPlaceholderText("Pesquisar")

        botaoPesquisa = QtWidgets.QPushButton()
        botaoPesquisa.setText("🔍")
        botaoPesquisa.setObjectName("botaoPesquisa")
        menuLayout.addWidget(botaoPesquisa)

        # Distancia2 ----------------------------
        distancia2 = QtWidgets.QSpacerItem(300, 40)
        menuLayout.addSpacerItem(distancia2)

        # foto de perfil
        fotoPerfilLayout = QtWidgets.QVBoxLayout()
        fotoPerfilLayout.setAlignment(Qt.AlignmentFlag.AlignAbsolute)
        menuLayout.addLayout(fotoPerfilLayout)

        self.fotoPerfil = FotoPerfil()
        self.fotoPerfil.setObjectName("fotoPerfil")
        fotoPerfilLayout.addWidget(self.fotoPerfil)

        mainWindow = getAncestrais(self)["mainWindow"]
        self.usuarioAtual = mainWindow.getUsuario()
        formularioLogin = getDescendentes(mainWindow)["formularioLogin"]
        formularioLogin.AtualizacaoUsuario.connect(self.getFotoPerfil)

        # Distancia3 ----------------------------
        distancia3 = QtWidgets.QSpacerItem(25, 0)
        menuLayout.addSpacerItem(distancia3)

        # botão de logout simplificado
        botao = QtWidgets.QPushButton()
        botao.setText("Logout")
        botao.setObjectName("logout")
        menuLayout.addWidget(botao)
        botao.clicked.connect(self.deslogar)


    def deslogar(self):
        mainWindow = getAncestrais(self)["mainWindow"]
        mainWindow.paginas.setCurrentIndex(0)

    def getFotoPerfil(self, nomeUsuario):
        try:
            imagemUsuario = dadosUsuario(nomeUsuario)["fotoPerfil"]
            self.fotoPerfil.changePhoto(imagemUsuario, 50)
        except (PIL.UnidentifiedImageError, TypeError):
            with open('src/view/assets/images/default_user.jpg', 'rb') as img_file:
                imagemUsuario = img_file.read()
                self.fotoPerfil.changePhoto(imagemUsuario, 50)

