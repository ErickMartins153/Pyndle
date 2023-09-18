from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QLabel,
    QPushButton,
    QFileDialog,
    QLineEdit,
    QComboBox,
    QSpacerItem
)
from PyQt6.QtGui import QImage, QPixmap, QIntValidator
from PyQt6.QtCore import Qt
from src.controller.telaPreviaLivro import dadosLivro
from src.controller.telaPrincipal import (
    uploadLivro,
    apagarLivro,
    updateDados,
    getGeneros,
)
from src.view.utils.imageTools import relHeight, relWidth, getResizedImage
from src.view.utils.widgetSearch import getAncestrais
from src.view.utils.container import verticalFrame


# noinspection PyAttributeOutsideInit
class FormularioLivro(QDialog):
    def __init__(self, parent):
        """
        PopUp para registro de livro pelo usuário
        :param parent:
        """
        super().__init__()

        # ATRIBUTOS --------------------------------------------

        self.parent = parent
        self.idUsuario = getAncestrais(self.parent)["mainWindow"].getUsuario()[
            "idUsuario"
        ]
        self.generoEscolhido = None
        self.ArquivoSelecionado = None
        self.idLivro = None
        self.contemPDF = False
        self.generos = getGeneros()

        # CONFIGURAÇÕES --------------------------------------

        self.setStyleSheet(open("src/view/assets/styles/popup.css").read())
        self.setWindowTitle("Adicionar Livro")
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, True)
        self.setWindowTitle("Adicionar Livro")
        self.setFixedSize(relWidth(550, 1366), relHeight(450, 768))


        # LAYOUT --------------------------------------------------------------

        layout = QHBoxLayout()
        layout.setObjectName("fundo")
        self.setLayout(layout)

        # CONTAINER (Frame com capa do livro e botão de adicionar) -----------------------

        groupImagemBotao = verticalFrame(self)
        groupImagemBotao.setMinimumWidth(relWidth(275, 1366))
        groupImagemBotao.setObjectName("groupImagemBotao")
        groupImagemBotao.setStyleSheet(f"""
            border-radius: {relHeight(20, 1080)}px;
        """)
        layout.addWidget(groupImagemBotao)

        groupImagemBotao.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)

        # CAPA DO LIVRO -------------------------------------------------------

        self.capa = QLabel(self)
        self.capa.setMinimumSize(relWidth(340, 1920), relHeight(476, 1080))
        self.capa.setAlignment(Qt.AlignmentFlag.AlignCenter)
        groupImagemBotao.layout().addWidget(self.capa, alignment=Qt.AlignmentFlag.AlignCenter)


        # SPACER --------------------------------------------------------------

        spacer = QSpacerItem(0, relHeight(25, 1080))
        groupImagemBotao.layout().addSpacerItem(spacer)

        # BOTÃO DE ADICIONAR LIVRO --------------------------------------------

        containerBotaoAdicionar = QVBoxLayout()
        containerBotaoAdicionar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        groupImagemBotao.layout().addLayout(containerBotaoAdicionar)

        botaoAdicionarPDF = QPushButton(groupImagemBotao)
        botaoAdicionarPDF.setText("Adicionar PDF")
        botaoAdicionarPDF.clicked.connect(self.adicionarPDF)
        containerBotaoAdicionar.layout().addWidget(botaoAdicionarPDF)


        # CONTAINER (Onde os metadados são dispostos e botão de registrar) --------------------------

        groupInfos = verticalFrame(self)
        groupInfos.setObjectName("groupTexto")
        layout.addWidget(groupInfos)
        groupInfos.layout().setObjectName("infosLayout")


        # CONTAINER (Grupo com os labels de metadados) ------------------------------

        groupMetadado = verticalFrame(groupInfos)
        groupMetadado.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
        groupMetadado.layout().setSpacing(0)
        groupInfos.layout().addWidget(groupMetadado)


        # LABEL (Informações do livro) ----------------------------------------------

        h1 = QLabel("Informações do livro")
        h1.setStyleSheet(f"""
            font-size: {relHeight(32, 1080)}px;
        """)
        groupMetadado.layout().addWidget(h1)
        h1.setObjectName("h1")
        h1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        h1.setMaximumHeight(relHeight(50, 1080))

        # METADADOS DO PDF ----------------------------------------------------------

        # MEDIDAS DAS ENTRADAS ------------------------------------------------

        entradasHeight = relHeight(40, 1080)


        # TÍTULO --------------------------------------------------------------------

        # Grupo de título
        groupTitulo = verticalFrame(groupMetadado)
        groupTitulo.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        groupMetadado.layout().addWidget(groupTitulo)

        # Label de título
        tituloLabel = QLabel("Titulo:")
        tituloLabel.setObjectName("info")
        tituloLabel.setMaximumHeight(20)
        groupTitulo.layout().addWidget(tituloLabel)

        # Entrada de título

        self.entradaTitulo = QLineEdit(self)
        self.entradaTitulo.setObjectName("caixaEntrada")
        self.entradaTitulo.setStyleSheet(f"""
             font-size: {relHeight(25, 1080)};
             border-radius: {relHeight(20, 1080)}px;
             padding: {relHeight(2, 1080)}px {relWidth(10, 1920)}px;
        """)
        self.entradaTitulo.setMinimumHeight(entradasHeight)
        groupTitulo.layout().addWidget(self.entradaTitulo)


        # GÊNERO ---------------------------------------------------------------------

        # Grupo de gênero
        groupGenero = verticalFrame(groupMetadado)
        groupGenero.layout().setAlignment(Qt.AlignmentFlag.AlignVCenter)
        groupMetadado.layout().addWidget(groupGenero)

        # Label de gênero
        generoLabel = QLabel(f"Gênero:")
        generoLabel.setObjectName("info")
        generoLabel.setMaximumHeight(20)
        groupGenero.layout().addWidget(generoLabel)

        # criar opcão de comboBox(similar ao select do html)
        self.entradaGenero = QComboBox(self)

        # criar valor inicial que não pode ser selecionado depois
        self.entradaGenero.addItem("")
        self.entradaGenero.setCurrentIndex(0)
        self.entradaGenero.view().setRowHidden(0, True)

        for genero in self.generos:
            self.entradaGenero.addItem(genero)

        self.entradaGenero.activated.connect(self.handleEscolha)
        groupGenero.layout().addWidget(self.entradaGenero)


        # AUTOR -------------------------------------------------------

        # Grupo de Autor
        groupAutor = verticalFrame(groupMetadado)
        groupAutor.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        groupMetadado.layout().addWidget(groupAutor)

        # Label de autor
        autorLabel = QLabel(f"Autor:")
        autorLabel.setMaximumHeight(20)
        autorLabel.setObjectName("info")
        groupAutor.layout().addWidget(autorLabel)

        # Entrada de autor
        self.entradaAutor = QLineEdit(self)
        self.entradaAutor.setObjectName("caixaEntrada")
        self.entradaAutor.setStyleSheet(f"""
             font-size: {relHeight(25, 1080)};
             border-radius: {relHeight(20, 1080)}px;
             padding: {relHeight(2, 1080)}px {relWidth(10, 1920)}px;
        """)
        self.entradaAutor.setMinimumHeight(entradasHeight)
        groupAutor.layout().addWidget(self.entradaAutor)


        # ANO DE PUBLICAÇÃO ------------------------------------------------

        # Grupo de ano
        groupAno = verticalFrame(groupMetadado)
        groupAno.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        groupMetadado.layout().addWidget(groupAno)

        # Label de ano
        anoLabel = QLabel(f"Ano:")
        anoLabel.setMaximumHeight(20)
        anoLabel.setObjectName("info")
        groupAno.layout().addWidget(anoLabel)

        # Entrada de ano
        self.entradaAno = QLineEdit(self)
        self.entradaAno.setValidator(QIntValidator())
        self.entradaAno.setObjectName("caixaEntrada")
        self.entradaAno.setStyleSheet(f"""
             font-size: {relHeight(25, 1080)};
             border-radius: {relHeight(20, 1080)}px;
             padding: {relHeight(2, 1080)}px {relWidth(10, 1920)}px;
        """)
        self.entradaAno.setMinimumHeight(entradasHeight)
        groupAno.layout().addWidget(self.entradaAno)


        # QUANTIDADE DE PÁGINAS ------------------------------------------------------

        # Label de páginas
        self.qtdPaginasLabel = QLabel(f"Total de páginas: adicione arquivo PDF!")
        self.qtdPaginasLabel.setStyleSheet(f"""
            font-size: {relHeight(16, 1080)}px;
        """)
        self.qtdPaginasLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.qtdPaginasLabel.setMinimumHeight(50)
        self.qtdPaginasLabel.setObjectName("info")
        groupMetadado.layout().addWidget(self.qtdPaginasLabel)


        # BOTÃO DE CADASTRAR LIVRO --------------------------------------------------

        # Container de botão de registrar
        containerBotaoRegistrar = QVBoxLayout()
        containerBotaoRegistrar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        groupInfos.layout().addLayout(containerBotaoRegistrar)

        # Definindo botão
        button = QPushButton("Cadastrar Livro", self)
        button.clicked.connect(self.cadastrarLivro)
        containerBotaoRegistrar.layout().addWidget(button)
        self.setLayout(layout)


        # DEFININDO PROPORÇÃO DO CONTAINER DE METADADOS ---------------------------
        groupInfos.layout().setStretch(0, 120)
        groupInfos.layout().setStretch(1, 20)


    # MÉTODOS -------------------------------------------


    def handleEscolha(self):
        self.generoEscolhido = self.sender().currentText()

    def adicionarPDF(self):
        janelaUploadPDF = QFileDialog()
        janelaUploadPDF.setFileMode(QFileDialog.FileMode.ExistingFiles)
        janelaUploadPDF.setNameFilter("Arquivos PDF (*.pdf)")
        janelaUploadPDF.setViewMode(QFileDialog.ViewMode.List)

        if janelaUploadPDF.exec() == QFileDialog.DialogCode.Accepted:
            ArquivoSelecionado = janelaUploadPDF.selectedFiles()[0]
            self.ArquivoSelecionado = ArquivoSelecionado
            extensao = ArquivoSelecionado.split(".")[-1]
            if self.contemPDF:
                apagarLivro(self.idLivro, self.idUsuario)
                self.entradaAutor.clear()
                self.entradaAno.clear()
                self.entradaGenero.setCurrentIndex(0)
                self.entradaTitulo.clear()
                self.contemPDF = False

            if extensao == "pdf" and ArquivoSelecionado and self.contemPDF is False:
                self.idUsuario = getAncestrais(self.parent)["mainWindow"].getUsuario()[
                    "idUsuario"
                ]

                self.idLivro = uploadLivro(ArquivoSelecionado, self.idUsuario)
                self.atualizarDados(self.idLivro)
                self.contemPDF = True

    def atualizarDados(self, idLivro):
        self.dadosLivro = dadosLivro(idLivro)
        if not self.entradaTitulo.text():
            self.entradaTitulo.setText(self.dadosLivro["titulo"])
        if not self.entradaAutor.text():
            self.entradaAutor.setText(self.dadosLivro["autor"])
        if not self.entradaAno.text():
            self.entradaAno.setText(self.dadosLivro["anoPublicacao"])
        self.qtdPaginasLabel.setText(f'Total de páginas: {self.dadosLivro["pagTotal"]}')

        resizedImage = getResizedImage(
            self.dadosLivro["capaLivro"], relWidth(340, 1920), relHeight(476, 1080)
        )
        self.capa.setPixmap(QPixmap.fromImage(QImage.fromData(resizedImage)))

    def cadastrarLivro(self):
        if self.generoEscolhido and self.ArquivoSelecionado:
            self.dadosAtualizados = {
                "titulo": self.entradaTitulo.text(),
                "genero": self.entradaGenero.currentText(),
                "autor": self.entradaAutor.text(),
                "ano": self.entradaAno.text(),
            }
            updateDados(self.dadosAtualizados, self.idLivro)
            self.contemPDF = False
            self.accept()
            self.parent.botaoFiltrarClicado()  # Atualiza o livros de "Minha Biblioteca"

    def keyPressEvent(self, event):
        """Checa se algum arquivo pdf foi upado sem\n
        finalizar o cadastro apertando a tecla esc"""
        if event.key() != Qt.Key.Key_Escape:
            return
        if event.key() == Qt.Key.Key_Escape and self.idLivro:
            apagarLivro(self.idLivro, self.idUsuario)
        self.accept()

    def closeEvent(self, event):
        """Checa se algum arquivo pdf foi upado \n
        sem finalizar o cadastro apertando o X"""
        if self.idLivro:
            apagarLivro(self.idLivro, self.idUsuario)
        event.accept()
