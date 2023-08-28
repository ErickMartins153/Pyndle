from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
from src.view.components.Menu import Menu
from src.view.components.BotaoImagem import BotaoImagem
from src.controller.telaPrincipal import livrosCatalogo
from myfiles.bimages import getImages


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
        meusLivros.setMinimumHeight(270)
        meusLivros.setObjectName("listaLivros")
        myBibliotecaLayout.addWidget(meusLivros)

        meusLivrosLayout = QtWidgets.QHBoxLayout()
        meusLivros.setLayout(meusLivrosLayout)

        for tuplaImagem in getImages():
            imageBotao = QtWidgets.QPushButton()
            qimage = QtGui.QImage.fromData(tuplaImagem[1])
            imageBotao.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(qimage)))
            imageBotao.setIconSize(QtCore.QSize(qimage.width(), qimage.height()))
            imageBotao.setFixedSize(qimage.width(), qimage.height())
            meusLivrosLayout.addWidget(imageBotao)

        # QFrame (Grupo: Catálogo) ----------------------------------------------------
        groupCatalogo = QtWidgets.QFrame(self)
        groupCatalogo.setObjectName("groupMyBiblioteca")
        fundoLayout.addWidget(groupCatalogo)

        catalogoLayout = QtWidgets.QVBoxLayout()
        catalogoLayout.setSpacing(14)
        groupCatalogo.setLayout(catalogoLayout)

        # Label (Catálogo)
        catalogoLabel = QtWidgets.QLabel(groupCatalogo)
        catalogoLabel.setMaximumHeight(25)
        catalogoLabel.setObjectName("indicadorListaLivros")
        catalogoLabel.setText("Catálogo")
        catalogoLayout.addWidget(catalogoLabel)

        # QFrame (Catalogo Livros)
        catalogoLivros = QtWidgets.QFrame(groupCatalogo)
        catalogoLivros.setMinimumHeight(270)
        catalogoLivros.setObjectName("listaLivros")
        catalogoLayout.addWidget(catalogoLivros)

        catalogoLivrosLayout = QtWidgets.QHBoxLayout()
        catalogoLivros.setLayout(catalogoLivrosLayout)

        for tuplaImagem in livrosCatalogo():  # Itera a lista de livros do catálogo
            imageBotao = BotaoImagem(tuplaImagem[0])
            qimage = QtGui.QImage.fromData(tuplaImagem[5])
            imageBotao.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(qimage)))
            imageBotao.setIconSize(QtCore.QSize(qimage.width(), qimage.height()))
            imageBotao.setFixedSize(qimage.width(), qimage.height())
            imageBotao.clicked.connect(self.botaoApertado)
            catalogoLivrosLayout.addWidget(imageBotao)


    def setNomeUsuario(self, usuarioAtual: str):
        usuarioAtual = usuarioAtual
        self.saudacao.setText(f"Bem vindo, {usuarioAtual}!")

    def botaoApertado(self):
        print(self.sender().getID())
