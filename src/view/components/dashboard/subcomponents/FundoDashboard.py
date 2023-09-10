from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import Qt
from src.view.components.BotaoImagem import BotaoImagem
from src.controller import telaPrincipal
from src.view.utils import widgetSearch
from src.controller.telaPrincipal import livrosCatalogo
from src.view.components.ModuloLivro.Popup import Popup



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
        self.setStyleSheet(open("src/view/assets/styles/dashboard/dashboard.css").read())
        self.setContentsMargins(20, 20, 20, 0)

        # Definição do Layout
        fundoLayout = QtWidgets.QVBoxLayout()
        self.setLayout(fundoLayout)

        # Label (Bem vindo) -----------------------------------------------
        self.saudacao = QtWidgets.QLabel(self)
        self.saudacao.setObjectName("saudacao")
        fundoLayout.addWidget(self.saudacao)

        self.saudacao.setText(f"Bem vindo, <usuario>!")
        self.saudacao.setMaximumHeight(35)
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
        myBibliotecaLabel.setObjectName("labelFrameLivros")
        myBibliotecaLabel.setMaximumHeight(35)
        myBibliotecaLabel.setText("Minha Biblioteca")
        myBibliotecaLayout.addWidget(myBibliotecaLabel)

        # QFrame (Meus Livros)
        meusLivros = QtWidgets.QFrame(groupMyBiblioteca)
        meusLivros.setMinimumHeight(300)
        meusLivros.setObjectName("frameLivros")
        myBibliotecaLayout.addWidget(meusLivros)

        meusLivrosLayout = QtWidgets.QHBoxLayout()
        meusLivros.setLayout(meusLivrosLayout)

        # Definindo "Meus Livros"
        self.listaMeusLivros = list()
        for tuplaLivro in telaPrincipal.livrosCatalogo()[:4]:
            meuLivro = BotaoImagem(tuplaLivro[0], tuplaLivro[5])
            meuLivro.setObjectName("livroBotao")
            meuLivro.resizeButton(200, 280)

            meuLivro.clicked.connect(self.botaoApertado)  # Conectando ação

            self.listaMeusLivros.append(meuLivro)
            meusLivrosLayout.addWidget(meuLivro)

        # Ver mais
        botaoVerMais1 = QtWidgets.QPushButton()
        botaoVerMais1.setObjectName("botaoVerMais")
        botaoVerMais1.setMaximumWidth(100)
        meusLivrosLayout.addWidget(botaoVerMais1)


        # QFrame (Grupo: Catálogo) ----------------------------------------------------
        groupCatalogo = QtWidgets.QFrame(self)
        groupCatalogo.setObjectName("groupMyBiblioteca")
        fundoLayout.addWidget(groupCatalogo)

        catalogoLayout = QtWidgets.QVBoxLayout()
        catalogoLayout.setSpacing(14)
        groupCatalogo.setLayout(catalogoLayout)

        # Label (Catálogo)
        catalogoLabel = QtWidgets.QLabel(groupCatalogo)
        catalogoLabel.setMaximumHeight(35)
        catalogoLabel.setObjectName("labelFrameLivros")
        catalogoLabel.setText("Catálogo")
        catalogoLayout.addWidget(catalogoLabel)

        # QFrame (Catalogo Livros)
        catalogoLivros = QtWidgets.QFrame(groupCatalogo)
        catalogoLivros.setMinimumHeight(300)
        catalogoLivros.setObjectName("frameLivros")
        catalogoLayout.addWidget(catalogoLivros)

        catalogoLivrosLayout = QtWidgets.QHBoxLayout()
        catalogoLivros.setLayout(catalogoLivrosLayout)

        # Definindo livros (imageButtons)
        self.listaLivrosCatalogo = list()  # Para acessar os botões em alguma função

        for tuplaLivro in telaPrincipal.livrosCatalogo()[:4]:  # Itera a lista de livros do catálogo

            livroCatalogo = BotaoImagem(tuplaLivro[0], tuplaLivro[5])
            livroCatalogo.setObjectName("livroBotao")
            livroCatalogo.resizeButton(200, 280)  # Redimensionando imagem

            # Ação do botão
            livroCatalogo.clicked.connect(self.botaoApertado)

            self.listaLivrosCatalogo.append(livroCatalogo)
            catalogoLivrosLayout.addWidget(livroCatalogo)

        # Ver mais
        botaoVerMais2 = QtWidgets.QPushButton()
        botaoVerMais2.setObjectName("botaoVerMais")
        botaoVerMais2.clicked.connect(self.clickVerMaisCatalogo)
        botaoVerMais2.setMaximumWidth(100)
        catalogoLivrosLayout.addWidget(botaoVerMais2)


    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        mainWindow = widgetSearch.getAncestrais(self)['mainWindow']  # mainWindow para identificar redimensionamentos
        print(f"{mainWindow.width()}X{mainWindow.height()}")
        
        # Redimensionamento dos livros
        if mainWindow.width() >= 1600:  # Redimensiona de acordo com o tamanho da janela
            print("Escalado")
            for livroCatalogo in self.listaLivrosCatalogo:
                livroCatalogo.resizeButton(240, 336)
            for livroMyLivro in self.listaMeusLivros:
                livroMyLivro.resizeButton(240, 336)
        else:
            for livroCatalogo in self.listaLivrosCatalogo:
                livroCatalogo.resizeButton(200, 280)
            for livroMyLivro in self.listaMeusLivros:
                livroMyLivro.resizeButton(200, 280)


    def setNomeUsuario(self, usuarioAtual: str):
        usuarioAtual = usuarioAtual
        self.saudacao.setText(f"Bem vindo, {usuarioAtual.capitalize()}!")

    def botaoApertado(self):
        print(self.sender().getID())
        popup = Popup(self.sender().getID())
        popup.exec()

    def clickVerMaisCatalogo(self):
        mainWindow = widgetSearch.getAncestrais(self)["mainWindow"]
        widgetSearch.getDescendentes(mainWindow)["paginas"].setCurrentIndex(3)
