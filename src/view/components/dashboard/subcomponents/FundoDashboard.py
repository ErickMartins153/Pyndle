from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
from src.view.components.Menu import Menu
from src.view.components.BotaoImagem import BotaoImagem
from src.controller import telaPrincipal
from src.view.utils import imageTools
from myfiles.bimages import getImages
from src.view.utils import widgetSearch

counter = 0
class FundoDashboard(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget):
        """
        Widget que compõe o conteúdo da tela principal | Contém a "Minha Biblioteca" e "Catálogo"

        :param parent: define o parente do widget

        Métodos:
            - setNomeUsuario(): atualiza o nome de usuário nas saudações da tela principal
        """
        # Configurações
        super().__init__()
        self.setParent(parent)
        self.setContentsMargins(20, 20, 20, 0)
        self.setStyleSheet(open('src/view/assets/styles/fundo_dashboard.css').read())

        # Definição do Layout
        fundoLayout = QtWidgets.QVBoxLayout()
        self.setLayout(fundoLayout)

        # Label (Bem vindo) -----------------------------------------------
        self.saudacao = QtWidgets.QLabel(self)
        self.saudacao.setObjectName("saudacao")
        fundoLayout.addWidget(self.saudacao)

        self.saudacao.setText(f"Bem vindo, <usuario>!")
        self.saudacao.setMaximumHeight(20)
        self.saudacao.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # QFrame (Grupo: Minha Biblioteca) ----------------------------------
        groupMyBiblioteca = QtWidgets.QFrame(self)
        groupMyBiblioteca.setObjectName("groupMyBiblioteca")
        fundoLayout.addWidget(groupMyBiblioteca)

        myBibliotecaLayout = QtWidgets.QVBoxLayout()
        myBibliotecaLayout.setSpacing(14)
        groupMyBiblioteca.setLayout(myBibliotecaLayout)

        # Label (Minha Biblioteca)
        myBibliotecaLabel = QtWidgets.QLabel(groupMyBiblioteca)
        myBibliotecaLabel.setObjectName("indicadorListaLivros")
        myBibliotecaLabel.setMaximumHeight(25)
        myBibliotecaLabel.setText("Minha Biblioteca")
        myBibliotecaLayout.addWidget(myBibliotecaLabel)

        # QFrame (Meus Livros)
        meusLivros = QtWidgets.QFrame(groupMyBiblioteca)
        meusLivros.setMinimumHeight(200)
        meusLivros.setObjectName("listaLivros")
        myBibliotecaLayout.addWidget(meusLivros)

        meusLivrosLayout = QtWidgets.QHBoxLayout()
        meusLivros.setLayout(meusLivrosLayout)


        for tuplaLivro in telaPrincipal.livrosCatalogo():
            self.imageBotao = QtWidgets.QPushButton()
            qimage = QtGui.QImage.fromData(tuplaLivro[5])
            self.imageBotao.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(qimage)))
            self.imageBotao.setIconSize(QtCore.QSize(qimage.width(), qimage.height()))
            self.imageBotao.setFixedSize(qimage.width(), qimage.height())
            meusLivrosLayout.addWidget(self.imageBotao)

        # QFrame (Grupo: Catálogo) ----------------------------------------------------
        groupCatalogo = QtWidgets.QFrame(self)
        groupCatalogo.setObjectName("groupMyBiblioteca")
        fundoLayout.addWidget(groupCatalogo)

        catalogoLayout = QtWidgets.QVBoxLayout()
        catalogoLayout.setSpacing(14)
        groupCatalogo.setLayout(catalogoLayout)

        # Label (Catálogo)
        catalogoLabel = QtWidgets.QLabel(groupCatalogo)
        catalogoLabel.setMaximumHeight(30)
        catalogoLabel.setObjectName("indicadorListaLivros")
        catalogoLabel.setText("Catálogo")
        catalogoLayout.addWidget(catalogoLabel)

        # QFrame (Catalogo Livros)
        catalogoLivros = QtWidgets.QFrame(groupCatalogo)
        catalogoLivros.setMinimumHeight(200)
        catalogoLivros.setObjectName("listaLivros")
        catalogoLayout.addWidget(catalogoLivros)

        catalogoLivrosLayout = QtWidgets.QHBoxLayout()
        catalogoLivros.setLayout(catalogoLivrosLayout)

        # Definindo livros (imageButtons)
        self.listaLivros = []  # Para acessar os botões em alguma função

        for tuplaLivro in telaPrincipal.livrosCatalogo():  # Itera a lista de livros do catálogo

            self.imageBotao = BotaoImagem(tuplaLivro[0])
            resizedImage = imageTools.getResizedImage(tuplaLivro[5], 200, 280)
            self.qimage = QtGui.QImage.fromData(resizedImage)
            self.imageBotao.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(self.qimage)))
            self.imageBotao.setIconSize(QtCore.QSize(self.qimage.width(), self.qimage.height()))
            self.imageBotao.setFixedSize(self.qimage.width(), self.qimage.height())

            # Ação do botão
            self.imageBotao.clicked.connect(self.botaoApertado)

            self.listaLivros.append(self.imageBotao)
            catalogoLivrosLayout.addWidget(self.imageBotao)

        # Ver mais
        botaoVerMais = QtWidgets.QPushButton()
        botaoVerMais.setObjectName("botaoVerMais")
        botaoVerMais.setMaximumWidth(100)
        catalogoLivrosLayout.addWidget(botaoVerMais)


    def setNomeUsuario(self, usuarioAtual: str):
        usuarioAtual = usuarioAtual
        self.saudacao.setText(f"Bem vindo, {usuarioAtual}!")

    def botaoApertado(self):
        print(self.sender().getID())
