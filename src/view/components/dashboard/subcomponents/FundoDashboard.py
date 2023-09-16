from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import Qt
from src.view.components.BotaoImagem import BotaoImagem
from src.controller import telaPrincipal
from src.view.components.ModuloLivro.Popup import Popup
from src.view.utils import widgetSearch
from src.view.utils.container import verticalFrame, horizontalFrame
from src.view.utils.imageTools import relHeight, relWidth


class FundoDashboard(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget):
        """
        Widget que compõe o conteúdo da tela principal | Contém a "Minha Biblioteca" e "Catálogo"

        :param parent: define o parente do widget

        Métodos:
            - setNomeUsuario(): atualiza o nome de usuário nas saudações da tela principal
        """
        # Atributos
        self.livrosDispostos = 0

        # Configurações
        super().__init__()
        self.setParent(parent)
        self.setStyleSheet(
            open("src/view/assets/styles/dashboard/dashboard.css").read()
        )
        self.setContentsMargins(
            relWidth(0, 1920), relHeight(20, 1080), relWidth(20, 1920), 0
        )

        # Definição do Layout
        fundoLayout = QtWidgets.QVBoxLayout()
        self.setLayout(fundoLayout)

        # Label (Bem vindo) --------------------------------------------------
        self.saudacao = QtWidgets.QLabel(self)
        self.saudacao.setObjectName("saudacao")
        self.saudacao.setStyleSheet(
            f"""
        font-size: {relHeight(25, 1080)}px;
        """
        )
        fundoLayout.addWidget(self.saudacao)

        self.saudacao.setText(f"Bem vindo, <usuario>!")
        self.saudacao.setMaximumHeight(relHeight(35, 1080))
        self.saudacao.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # QFrame (Container: Minha Biblioteca) ----------------------------------
        ContainerMinhaBiblioteca = verticalFrame(self, "ContainerConteudo")
        ContainerMinhaBiblioteca.setMinimumHeight(relHeight(100, 1080))
        ContainerMinhaBiblioteca.layout().setSpacing(relHeight(14, 1080))
        fundoLayout.addWidget(ContainerMinhaBiblioteca)

        # Label (Minha Biblioteca)
        myBibliotecaLabel = QtWidgets.QLabel(ContainerMinhaBiblioteca)
        myBibliotecaLabel.setObjectName("labelFrameLivros")
        myBibliotecaLabel.setStyleSheet(
            f"""
        font-size: {relHeight(25, 1080)}
        """
        )
        myBibliotecaLabel.setMaximumHeight(relHeight(35, 1080))
        myBibliotecaLabel.setText("Minha Biblioteca")
        ContainerMinhaBiblioteca.layout().addWidget(myBibliotecaLabel)

        # QFrame (Meus Livros): Frame com o grupo de livros e o botão "Ver Mais"
        meusLivrosFrame = horizontalFrame(ContainerMinhaBiblioteca, "frameLivros")
        meusLivrosFrame.setMinimumHeight(relHeight(300, 1080))
        meusLivrosFrame.layout().setContentsMargins(
            relWidth(50, 1920),
            relHeight(5, 1080),
            relWidth(50, 1920),
            relHeight(5, 1080),
        )
        meusLivrosFrame.setStyleSheet(
            f"""
        border-radius: {relHeight(15, 1080)}px;
        """
        )
        ContainerMinhaBiblioteca.layout().addWidget(meusLivrosFrame)

        # QFrame (Grupo: Meus Livros): grupo onde os livros são dispostos
        self.groupMeusLivros = horizontalFrame(meusLivrosFrame)
        meusLivrosFrame.layout().addWidget(self.groupMeusLivros)

        # Lista de botoesLivros (Meus Livros)
        self.listaMeusLivros = list()  # Para acessar ou definir os botões em funções

        # Ver mais
        botaoVerMais1 = QtWidgets.QPushButton(meusLivrosFrame)
        botaoVerMais1.setObjectName("botaoVerMais")
        botaoVerMais1.setStyleSheet(
            f"""
        width: {relWidth(150, 1920)}px;
        height: {relHeight(150, 1080)}px;
        """
        )
        botaoVerMais1.clicked.connect(self.clickVerMaisMinhaBiblioteca)
        botaoVerMais1.setMaximumWidth(relWidth(100, 1920))
        meusLivrosFrame.layout().addWidget(botaoVerMais1)

        # QFrame (Container: Catálogo) ----------------------------------------------------
        containerCatalogo = verticalFrame(self, "ContainerConteudo")
        containerCatalogo.layout().setSpacing(relHeight(14, 1080))
        containerCatalogo.setMinimumHeight(relHeight(100, 1080))
        fundoLayout.addWidget(containerCatalogo)

        # Label (Catálogo)
        catalogoLabel = QtWidgets.QLabel(containerCatalogo)
        catalogoLabel.setStyleSheet(
            f"""
        font-size: {relHeight(25, 1080)}
        """
        )
        catalogoLabel.setMaximumHeight(relHeight(35, 1080))
        catalogoLabel.setObjectName("labelFrameLivros")
        catalogoLabel.setText("Catálogo")
        containerCatalogo.layout().addWidget(catalogoLabel)

        # QFrame (Catalogo): Frame com o grupo de livros e o botão "Ver Mais"
        catalogoFrame = horizontalFrame(containerCatalogo, "frameLivros")
        catalogoFrame.setMinimumHeight(relHeight(300, 1080))
        catalogoFrame.layout().setContentsMargins(
            relWidth(50, 1920),
            relHeight(5, 1080),
            relWidth(50, 1920),
            relHeight(5, 1080),
        )
        catalogoFrame.setStyleSheet(
            f"""
        border-radius: {relHeight(15, 1080)}px;
        """
        )
        containerCatalogo.layout().addWidget(catalogoFrame)

        # QFrame (Grupo: livros do catálogo): grupo onde os livros são dispostos
        self.groupCatalogoLivros = horizontalFrame(catalogoFrame)
        catalogoFrame.layout().addWidget(self.groupCatalogoLivros)

        # Lista dos botoesLivro (Catálogo)
        self.listaLivrosCatalogo = (
            list()
        )  # Para acessar ou definir os botões em funções

        # Ver mais
        botaoVerMais2 = QtWidgets.QPushButton()
        botaoVerMais2.setObjectName("botaoVerMais")
        botaoVerMais2.setStyleSheet(
            f"""
        width: {relWidth(150, 1920)}px;
        height: {relHeight(150, 1080)}px;
        """
        )
        botaoVerMais2.clicked.connect(self.clickVerMaisCatalogo)
        botaoVerMais2.setMaximumWidth(relWidth(100, 1920))
        catalogoFrame.layout().addWidget(botaoVerMais2)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        mainWindow = widgetSearch.getAncestrais(self)[
            "mainWindow"
        ]  # mainWindow para identificar redimensionamentos

        # Redimensionamento dos livros
        if mainWindow.width() >= relWidth(
            1600, 1920
        ):  # Redimensiona de acordo com o tamanho da janela
            if (
                self.livrosDispostos != 5 and mainWindow.getUsuario()
            ):  # Também verifica se o usuário logou
                self.getLivrosDashboard(5)  # Dispõe 5 livros

            for livroCatalogo in self.listaLivrosCatalogo:
                livroCatalogo.resizeButton(relWidth(220, 1920), relHeight(308, 1080))

            for livroMyLivro in self.listaMeusLivros:
                livroMyLivro.resizeButton(relWidth(220, 1920), relHeight(308, 1080))
        else:
            if (
                self.livrosDispostos != 4 and mainWindow.getUsuario()
            ):  # Também verifica se o usuário logou
                self.getLivrosDashboard(4)  # Dispõe 4 livros
            for livroCatalogo in self.listaLivrosCatalogo:
                livroCatalogo.resizeButton(relWidth(200, 1920), relHeight(280, 1080))
            for livroMyLivro in self.listaMeusLivros:
                livroMyLivro.resizeButton(relWidth(200, 1920), relHeight(280, 1080))

    def setNomeUsuario(self, usuarioAtual: str):
        usuarioAtual = usuarioAtual
        self.saudacao.setText(f"Bem vindo, {usuarioAtual.capitalize()}!")

    def getLivrosDashboard(self, qntLivros: int):
        # Obtendo o usuário atual
        usuarioAtual = widgetSearch.getAncestrais(self)["mainWindow"].getUsuario()

        # Deleta os botões existentes e limpa a lista de botões
        for livroCatalogo in self.listaLivrosCatalogo:
            livroCatalogo.deleteLater()
        for livroBiblioteca in self.listaMeusLivros:
            livroBiblioteca.deleteLater()
        self.listaLivrosCatalogo.clear()
        self.listaMeusLivros.clear()

        # Definindo Catálogo
        for dictLivro in telaPrincipal.filtrarCatalogo()[
            :qntLivros
        ]:  # Itera a lista de livros do catálogo
            livroCatalogo = BotaoImagem(dictLivro["idLivro"], dictLivro["capaLivro"])
            livroCatalogo.setObjectName("livroBotao")

            # Ação do botão
            livroCatalogo.clicked.connect(self.botaoApertado)

            self.listaLivrosCatalogo.append(livroCatalogo)
            self.groupCatalogoLivros.layout().addWidget(livroCatalogo)

        # Definindo "Minha Biblioteca"
        if usuarioAtual:
            for tuplaLivro in telaPrincipal.filtrarBiblioteca(
                usuarioAtual["idUsuario"]
            )[:qntLivros]:
                meuLivro = BotaoImagem(tuplaLivro["idLivro"], tuplaLivro["capaLivro"])
                meuLivro.setObjectName("livroBotao")

                meuLivro.clicked.connect(self.botaoApertado)  # Conectando ação

                self.listaMeusLivros.append(meuLivro)
                self.groupMeusLivros.layout().addWidget(meuLivro)

        # Informa quantidade de livros dispostos após operação
        self.livrosDispostos = qntLivros

    def botaoApertado(self):
        mainWindow = widgetSearch.getAncestrais(self)["mainWindow"]
        usuarioAtual = mainWindow.getUsuario()["login"]
        popup = Popup(usuarioAtual, self.sender().getID(), self)
        popup.exec()

    def clickVerMaisMinhaBiblioteca(self):
        mainWindow = widgetSearch.getAncestrais(self)["mainWindow"]
        painelLivrosBiblioteca = widgetSearch.getDescendentes(mainWindow)[
            "painelLivrosBiblioteca"
        ]

        painelLivrosBiblioteca.getLivrosMinhaBiblioteca()
        painelLivrosBiblioteca.resizeEvent(None)
        widgetSearch.getDescendentes(mainWindow)["paginas"].setCurrentIndex(2)

    def clickVerMaisCatalogo(self):
        mainWindow = widgetSearch.getAncestrais(self)["mainWindow"]
        painelLivrosCatalogo = widgetSearch.getDescendentes(mainWindow)[
            "painelLivrosCatalogo"
        ]

        painelLivrosCatalogo.getLivrosCatalogo()
        painelLivrosCatalogo.resizeEvent(None)
        widgetSearch.getDescendentes(mainWindow)["paginas"].setCurrentIndex(3)
