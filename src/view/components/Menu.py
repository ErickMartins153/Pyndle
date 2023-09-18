from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal
from src.controller.telaInicial import dadosUsuario
from src.controller.telaPrincipal import pesquisarLivro
from src.view.components.FotoPerfil import FotoPerfil
from src.view.utils.widgetSearch import getAncestrais, getDescendentes
from src.view.utils.imageTools import relHeight, relWidth
from src.view.components.Logo import Logo
from src.view.utils.widgetSearch import getAncestrais
import PIL
import sqlite3

class Menu(QtWidgets.QFrame):
    #Sinal para enviar o resultado da pesquisa para a telaPesquisa
    sinalPesquisa = pyqtSignal(list)

    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()
        self.setParent(parent)
        self.setStyleSheet(open("src/view/assets/styles/menu.css").read())
        self.setStyleSheet(open("src/view/assets/styles/menu.css").read())
        self.setMaximumHeight(70)

        menuLayout = QtWidgets.QHBoxLayout()
        self.setLayout(menuLayout)

        # Logo -------------------------------
        self.logo = Logo(relWidth(120, 1920), relHeight(50, 1080), relHeight(10, 1080))
        self.logo.setObjectName("logo")
        self.logo.setFixedHeight(relHeight(50, 1080))
        menuLayout.addWidget(self.logo)

        # Distancia1 ----------------------------
        distancia1 = QtWidgets.QSpacerItem(40, 40)
        menuLayout.addSpacerItem(distancia1)

        # QLineEdit (Barra Pesquisa) ------------
        self.pesquisa = QtWidgets.QLineEdit()  # Definindo self.pesquisa como um atributo da classe
        menuLayout.addWidget(self.pesquisa)

        self.pesquisa.setObjectName("pesquisa")
        self.pesquisa.setMinimumSize(200, 37)
        self.pesquisa.setMaximumHeight(37)
        self.pesquisa.setPlaceholderText("Pesquisar")

        botaoPesquisa = QtWidgets.QPushButton()
        botaoPesquisa.setText("🔍")
        botaoPesquisa.setObjectName("botaoPesquisa")
        botaoPesquisa.clicked.connect(self.pesquisaLivro)
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

    def pesquisaLivro(self):
        
        textoPesquisa = self.pesquisa.text()
        resultadoPesquisa = pesquisarLivro(textoPesquisa)
        self.sinalPesquisa.emit(resultadoPesquisa)
        mainWindow = getAncestrais(self)["mainWindow"]
        mainWindow.paginas.setCurrentIndex(4)
