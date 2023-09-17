from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import Qt
from src.view.components.BotaoImagem import BotaoImagem
from src.controller import telaPrincipal
from src.view.widgets.moduloLivro.Popup import Popup
from src.view.widgets.catalogo.subcomponents.popupCatalogo import PopupCatalogo
from src.view.utils import widgetSearch
from src.view.utils.container import verticalFrame, horizontalFrame
from src.view.utils.imageTools import relHeight, relWidth


class FundoDashboard(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget):
        """
        Widget que compõe o conteúdo da Dashboard
        :param parent: define o parente do widget

        ATRIBUTOS:
            - livrosDispostos: quantidade de livros que estão dispostos nos frames da "Dashboard"
        """

        # ATRIBUTOS ----------------------------------------
        self.livrosDispostos = 0

        # CONFIGURAÇÕES ------------------------------------
        super().__init__()
        self.setParent(parent)
        self.setStyleSheet(open("src/view/assets/styles/dashboard/dashboard.css").read())
        self.setContentsMargins(
            relWidth(0, 1920),
            relHeight(20, 1080),
            relWidth(20, 1920),
            0
        )

        # CONTAINER PRINCIPAL -----------------------------------------
        fundoLayout = QtWidgets.QVBoxLayout()
        self.setLayout(fundoLayout)

        # Label (Bem vindo)

        self.saudacao = QtWidgets.QLabel(self)
        self.saudacao.setObjectName("saudacao")
        self.saudacao.setStyleSheet(f"""
            font-size: {relHeight(25, 1080)}px;
        """)
        fundoLayout.addWidget(self.saudacao)

        self.saudacao.setText(f"Bem vindo, <usuario>!")
        self.saudacao.setMaximumHeight(relHeight(35, 1080))
        self.saudacao.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # CONTAINER (MINHA BIBLIOTECA) ----------------------------------------

        ContainerMinhaBiblioteca = verticalFrame(self, "ContainerConteudo")
        ContainerMinhaBiblioteca.setMinimumHeight(relHeight(100, 1080))
        ContainerMinhaBiblioteca.layout().setSpacing(relHeight(14, 1080))
        fundoLayout.addWidget(ContainerMinhaBiblioteca)

        # Label (Minha Biblioteca)
        myBibliotecaLabel = QtWidgets.QLabel(ContainerMinhaBiblioteca)
        myBibliotecaLabel.setObjectName("labelFrameLivros")
        myBibliotecaLabel.setStyleSheet(f"""
            font-size: {relHeight(25, 1080)}
        """)
        myBibliotecaLabel.setMaximumHeight(relHeight(45, 1080))
        myBibliotecaLabel.setText("Minha Biblioteca")
        ContainerMinhaBiblioteca.layout().addWidget(myBibliotecaLabel)

        # CONTAINER (Frame com o grupo de livros e o botão "Ver Mais") --------------------------

        meusLivrosFrame = horizontalFrame(ContainerMinhaBiblioteca, "frameLivros")
        meusLivrosFrame.setStyleSheet(f"""
                    border-radius: {relHeight(15, 1080)}px;
                """)

        meusLivrosFrame.setMinimumHeight(relHeight(300, 1080))
        meusLivrosFrame.layout().setContentsMargins(
            relWidth(50, 1920),
            relHeight(5, 1080),
            relWidth(50, 1920),
            relHeight(5, 1080),
        )

        ContainerMinhaBiblioteca.layout().addWidget(meusLivrosFrame)

        # CONTAINER (Grupo onde os livros da "minha biblioteca" são dispostos) ---------------------

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

        # CONTAINER (CATALOGO) ----------------------------------------------------
        containerCatalogo = verticalFrame(self, "ContainerConteudo")
        containerCatalogo.layout().setSpacing(relHeight(14, 1080))
        containerCatalogo.setMinimumHeight(relHeight(100, 1080))
        fundoLayout.addWidget(containerCatalogo)

        # Label (Catálogo)
        catalogoLabel = QtWidgets.QLabel(containerCatalogo)
        catalogoLabel.setStyleSheet(f"""
            font-size: {relHeight(25, 1080)}
        """)
        catalogoLabel.setMaximumHeight(relHeight(45, 1080))
        catalogoLabel.setObjectName("labelFrameLivros")
        catalogoLabel.setText("Catálogo")
        containerCatalogo.layout().addWidget(catalogoLabel)

        # CONTAINER (Frame com o grupo de livros e o botão "Ver Mais") --------------------
        catalogoFrame = horizontalFrame(containerCatalogo, "frameLivros")
        catalogoFrame.setMinimumHeight(relHeight(300, 1080))
        catalogoFrame.layout().setContentsMargins(
            relWidth(50, 1920),
            relHeight(5, 1080),
            relWidth(50, 1920),
            relHeight(5, 1080),
        )
        catalogoFrame.setStyleSheet(f"""
        border-radius: {relHeight(15, 1080)}px;
        """)

        containerCatalogo.layout().addWidget(catalogoFrame)

        # CONTAINER (grupo onde os livros do catálogo são dispostos) ------------------------

        self.groupCatalogoLivros = horizontalFrame(catalogoFrame)
        catalogoFrame.layout().addWidget(self.groupCatalogoLivros)

        # Lista dos botoesLivro (Catálogo)
        self.listaLivrosCatalogo = (list())  # Para acessar ou definir os botões em funções

        # Ver mais
        botaoVerMais2 = QtWidgets.QPushButton()
        botaoVerMais2.setObjectName("botaoVerMais")
        botaoVerMais2.setStyleSheet(f"""
            width: {relWidth(150, 1920)}px;
            height: {relHeight(150, 1080)}px;
        """)
        botaoVerMais2.clicked.connect(self.clickVerMaisCatalogo)
        botaoVerMais2.setMaximumWidth(relWidth(100, 1920))

        catalogoFrame.layout().addWidget(botaoVerMais2)

    # (EVENTOS) ---------------------------------------------------------

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        """
        Evento de redimensionamento de tela
        """
        self.resizeAndDisplayLivros()


    # (MÉTODOS) ---------------------------------------------------------

    def resizeAndDisplayLivros(self):
        """
        Redimensiona os livros de acordo com a resolução da tela e \n
        dispõe os livros de "Minha Biblioteca" e "Catálogo" da Dashboard
        """

        # mainWindow para obter o tamanho da janela
        mainWindow = widgetSearch.getAncestrais(self)["mainWindow"]

        # Redimensiona os livros de acordo com o tamanho da janela
        if mainWindow.width() >= relWidth(1600, 1920):
            # Dispõe 5 livros e verifica se o usuário está logado
            if self.livrosDispostos != 5 and mainWindow.getUsuario():
                self.getLivrosDashboard(5)

            # Redimensionando livros do "Catálogo"
            for livroCatalogo in self.listaLivrosCatalogo:
                livroCatalogo.resizeButton(relWidth(220, 1920), relHeight(308, 1080))

            # Redimensionando livros de "Minha Biblioteca"
            for livroMyLivro in self.listaMeusLivros:
                livroMyLivro.resizeButton(relWidth(220, 1920), relHeight(308, 1080))

        else:
            # Dispõe 4 livros e verifica se o usuário está logado
            if self.livrosDispostos != 4 and mainWindow.getUsuario():
                self.getLivrosDashboard(4)

            # Redimensiona livros do "Catálogo"
            for livroCatalogo in self.listaLivrosCatalogo:
                livroCatalogo.resizeButton(relWidth(200, 1920), relHeight(280, 1080))

            # Redimensiona livros de "Minha Biblioteca"
            for livroMyLivro in self.listaMeusLivros:
                livroMyLivro.resizeButton(relWidth(200, 1920), relHeight(280, 1080))


    def setNomeUsuario(self, usuarioAtual: str):
        """
        Define o nome do usuário na saudação\n
        **OBS**: Utilizado ao usuário logar
        :param usuarioAtual: Usuário atual do aplicativo
        """

        self.saudacao.setText(f"Bem vindo, {usuarioAtual.capitalize()}!")


    def getLivrosDashboard(self, qntLivros: int):
        """
        Atualiza os livros do "Catálogo" e "Minha Biblioteca" e os dispõe
        de acordo com a quantidade especificada
        :param qntLivros: quantidade de livros que serão dispostos nos frames
        """
        # Obtendo o usuário atual
        usuarioAtual = widgetSearch.getAncestrais(self)["mainWindow"].getUsuario()

        # Deleta os botões existentes e limpa a lista de botões
        for livroCatalogo in self.listaLivrosCatalogo:
            livroCatalogo.hide()
            livroCatalogo.deleteLater()
        for livroBiblioteca in self.listaMeusLivros:
            livroBiblioteca.hide()
            livroBiblioteca.deleteLater()
        self.listaLivrosCatalogo.clear()
        self.listaMeusLivros.clear()

        # Definindo Catálogo
        for dictLivro in telaPrincipal.filtrarCatalogo()[:qntLivros]:  # Itera a lista de livros do catálogo
            livroCatalogo = BotaoImagem(dictLivro["idLivro"], dictLivro["capaLivro"])
            livroCatalogo.setObjectName("livroBotao")

            livroCatalogo.clicked.connect(self.livroCatalogoSelecionado)

            self.listaLivrosCatalogo.append(livroCatalogo)
            self.groupCatalogoLivros.layout().addWidget(livroCatalogo)

        # Definindo "Minha Biblioteca"
        if usuarioAtual:
            for dictLivro in telaPrincipal.filtrarBiblioteca(usuarioAtual["idUsuario"])[:qntLivros]:
                meuLivro = BotaoImagem(dictLivro["idLivro"], dictLivro["capaLivro"])
                meuLivro.setObjectName("livroBotao")

                meuLivro.clicked.connect(self.livroBibliotecaSelecionado)

                self.listaMeusLivros.append(meuLivro)
                self.groupMeusLivros.layout().addWidget(meuLivro)

        # Informa quantidade de livros dispostos após operação
        self.livrosDispostos = qntLivros


    def livroBibliotecaSelecionado(self):
        """
        Abre PopUp com para leitura e obtenção de informações do livro de "Minha Biblioteca"
        """

        # mainWindow para obter o login do usuário atual
        mainWindow = widgetSearch.getAncestrais(self)["mainWindow"]
        usuarioAtual = mainWindow.getUsuario()["login"]

        # Abrindo PopUp
        popupBiblioteca = Popup(usuarioAtual, self.sender().getID(), self)
        popupBiblioteca.sinalLivroApagado.connect(self.atualizarLivros)
        popupBiblioteca.exec()


    def livroCatalogoSelecionado(self):
        """
        Abre PopUp com informações do livro do "Catálogo"\n
        **OBS**: Caso o usuário já possua o livro, o PopUp normal de livros de "Minha Biblioteca" será aberto
        :return:
        """

        # mainWindow para obter login do usuário atual
        mainWindow = widgetSearch.getAncestrais(self)["mainWindow"]
        usuarioAtual = mainWindow.getUsuario()

        # Caso o usuário já possua o livro, abre o PopUp de "Minha Biblioteca"
        if telaPrincipal.checarRelacaoUsuarioLivro(usuarioAtual["idUsuario"], self.sender().getID()):
            popupBiblioteca = Popup(usuarioAtual["login"], self.sender().getID(), self)
            popupBiblioteca.sinalLivroApagado.connect(self.atualizarLivros)
            popupBiblioteca.exec()
        # Caso contrário, abre o PopUp do "Catálogo" com informações do usuário
        else:
            popupCatalogo = PopupCatalogo(usuarioAtual["login"], self.sender().getID(), self)
            popupCatalogo.sinalLivroAdicionado.connect(self.atualizarLivros)
            popupCatalogo.exec()


    def atualizarLivros(self):
        """
        Utilizado quando um livro do catalogo é adicionado para atualizar os livros de "Minha Biblioteca"
        ou quando um livro de "Minha Biblioteca" é apagado
        """
        self.livrosDispostos = 0
        self.resizeAndDisplayLivros()


    def clickVerMaisMinhaBiblioteca(self):
        """
        Ação para quando o botão de "Ver Mais" de "Minha Bibliteca" é clicado\n
        **OBS**: Direciona para a janela "Minha Biblioteca"
        """

        # Obtém o painelLivrosBiblioteca a partir da mainWindow para atualizar e dispor livros
        self.livrosDispostos = 0
        mainWindow = widgetSearch.getAncestrais(self)["mainWindow"]
        painelLivrosBiblioteca = widgetSearch.getDescendentes(mainWindow)["painelLivrosBiblioteca"]

        # Atualiza e dispões livros da janela "Minha Biblioteca"
        painelLivrosBiblioteca.getLivrosMinhaBiblioteca()
        painelLivrosBiblioteca.resizeEvent(None)

        # Muda a janela para "Minha Biblioteca"
        widgetSearch.getDescendentes(mainWindow)["paginas"].setCurrentIndex(2)

    def clickVerMaisCatalogo(self):
        """
        Ação para quando o botão de "Ver Mais" de "Catálogo" é clicado\n
        **OBS**: Direciona para a janela "Catálogo"
        """

        # Obtém o painelLivrosCatalogo a partir da mainWindow para atualizar e dispor livros
        self.livrosDispostos = 0
        mainWindow = widgetSearch.getAncestrais(self)["mainWindow"]
        painelLivrosCatalogo = widgetSearch.getDescendentes(mainWindow)["painelLivrosCatalogo"]

        # Atualiza e dispõe livros da janela "Catálogo"
        painelLivrosCatalogo.getLivrosCatalogo()
        painelLivrosCatalogo.resizeEvent(None)

        # Muda a janela para "Catálogo"
        widgetSearch.getDescendentes(mainWindow)["paginas"].setCurrentIndex(3)
