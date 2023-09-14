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
)
from PyQt6.QtGui import QImage, QPixmap, QIntValidator
from PyQt6.QtCore import Qt
from src.controller.telaPreviaLivro import dadosLivro
from src.controller.telaPrincipal import uploadLivro, apagarLivro, updateGenero
from src.view.utils.imageTools import relHeight, relWidth, getResizedImage
from src.view.utils.widgetSearch import getAncestrais


class FormularioLivro(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.setStyleSheet(open("src/view/assets/styles/popup.css").read())
        self.parent = parent
        self.setWindowTitle("Adicionar Livro")
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setFixedSize(700, 700)
        self.setWindowFlag(Qt.WindowType.Window, False)

        self.generoEscolhido = None
        self.ArquivoSelecionado = None
        self.idLivro = None
        self.contemPDF = False

        entradasHeight = relHeight(40, 1080)

        layout = QHBoxLayout()
        layout.setObjectName("fundo")
        self.setLayout(layout)

        groupImagemBotao = QFrame(self)
        groupImagemBotao.setObjectName("groupImagemBotao")
        groupImagemBotao.setFixedSize(300, 610)
        groupImagemBotao.setStyleSheet(
            f"""
        border-radius: {relHeight(20, 1080)}px;
        """
        )
        layout.addWidget(groupImagemBotao)

        ImagemBotaoLayout = QVBoxLayout()
        ImagemBotaoLayout.setObjectName("ImagemBotaoLayout")
        ImagemBotaoLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        groupImagemBotao.setLayout(ImagemBotaoLayout)

        # imagemCapaLivro = QImage()
        self.capa = QLabel(self)

        # colocar um espaço em cima e embaixo da capa, garantindo que ela fique no centro do frame
        ImagemBotaoLayout.addStretch()
        ImagemBotaoLayout.addWidget(self.capa, alignment=Qt.AlignmentFlag.AlignCenter)
        ImagemBotaoLayout.addStretch()

        botaoAdicionarPDF = QPushButton(self)
        botaoAdicionarPDF.setText("Adicionar PDF")
        botaoAdicionarPDF.clicked.connect(self.adicionarPDF)
        ImagemBotaoLayout.addWidget(botaoAdicionarPDF)

        groupInfos = QFrame(self)
        groupInfos.setObjectName("groupTexto")
        layout.addWidget(groupInfos)

        groupLabelInput = QFrame(self)
        groupLabelInput.setObjectName("groupLabelInput")
        # groupLabelInput.setLayout(layoutFrame)

        infosLayout = QVBoxLayout()
        layout.setSpacing(-10)
        infosLayout.setObjectName("infosLayout")
        groupInfos.setLayout(infosLayout)

        h1 = QLabel("Informações do livro")
        infosLayout.addWidget(h1)
        h1.setObjectName("h1")
        h1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        h1.setMaximumHeight(50)

        tituloLabel = QLabel("Titulo:")
        tituloLabel.setObjectName("info")
        tituloLabel.setMaximumHeight(20)
        infosLayout.addWidget(tituloLabel)

        self.entradaTitulo = QLineEdit(self)
        self.entradaTitulo.setObjectName("caixaEntrada")
        self.entradaTitulo.setStyleSheet(
            f"""
         font-size: {relHeight(25, 1080)};
         border-radius: {relHeight(20, 1080)}px;
         padding: {relHeight(2, 1080)}px {relWidth(10, 1920)}px;
        
        """
        )
        self.entradaTitulo.setMaximumHeight(entradasHeight)
        infosLayout.addWidget(self.entradaTitulo)

        generoLabel = QLabel(f"Gênero:")
        generoLabel.setObjectName("info")
        generoLabel.setMaximumHeight(20)
        infosLayout.addWidget(generoLabel)

        # criar opcão de comboBox(similar ao select do html)
        self.entradaGenero = QComboBox(self)

        # criar valor inicial que não pode ser selecionado depois
        self.entradaGenero.addItem("")
        self.entradaGenero.setCurrentIndex(0)
        self.entradaGenero.view().setRowHidden(0, True)

        self.entradaGenero.addItem("Drama")
        self.entradaGenero.addItem("Hentai")
        self.entradaGenero.activated.connect(self.handleEscolha)
        infosLayout.addWidget(self.entradaGenero)

        autorLabel = QLabel(f"Autor:")
        autorLabel.setMaximumHeight(20)
        autorLabel.setObjectName("info")
        infosLayout.addWidget(autorLabel)

        self.entradaAutor = QLineEdit(self)
        self.entradaAutor.setObjectName("caixaEntrada")
        self.entradaAutor.setStyleSheet(
            f"""
         font-size: {relHeight(25, 1080)};
         border-radius: {relHeight(20, 1080)}px;
         padding: {relHeight(2, 1080)}px {relWidth(10, 1920)}px;
        
        """
        )
        self.entradaAutor.setMaximumHeight(entradasHeight)
        infosLayout.addWidget(self.entradaAutor)

        anoLabel = QLabel(f"Ano:")
        anoLabel.setMaximumHeight(20)
        anoLabel.setObjectName("info")
        infosLayout.addWidget(anoLabel)

        self.entradaAno = QLineEdit(self)
        self.entradaAno.setValidator(QIntValidator())
        self.entradaAno.setObjectName("caixaEntrada")
        self.entradaAno.setStyleSheet(
            f"""
         font-size: {relHeight(25, 1080)};
         border-radius: {relHeight(20, 1080)}px;
         padding: {relHeight(2, 1080)}px {relWidth(10, 1920)}px;
        
        """
        )
        self.entradaAno.setMaximumHeight(entradasHeight)
        infosLayout.addWidget(self.entradaAno)

        self.qtdPaginasLabel = QLabel(f"Total de páginas: adicione arquivo PDF!")
        self.qtdPaginasLabel.setMaximumHeight(20)
        self.qtdPaginasLabel.setObjectName("info")
        infosLayout.addWidget(self.qtdPaginasLabel)

        button = QPushButton("Cadastrar Livro", self)
        button.clicked.connect(self.cadastrarLivro)
        infosLayout.addWidget(button)
        self.setLayout(layout)

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
                apagarLivro(self.idLivro)
                self.entradaAutor.clear()
                self.entradaAno.clear()
                self.entradaGenero.clear()
                self.entradaTitulo.clear()
                self.contemPDF = False

            if extensao == "pdf" and ArquivoSelecionado and self.contemPDF is False:
                self.idLivro = uploadLivro(ArquivoSelecionado)
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

    def cadastrarLivro(self, selectedFile):
        if self.generoEscolhido and self.ArquivoSelecionado:
            updateGenero(self.generoEscolhido, self.idLivro)
            self.contemPDF = False
            self.parent.conteudoCatalogo.painelLivros.atualizarLivros()
            self.accept()

    def keyPressEvent(self, event):
        """Checa se algum arquivo pdf foi upado sem\n
        finalizar o cadastro apertando a tecla esc"""
        if event.key() != Qt.Key.Key_Escape:
            return
        if event.key() == Qt.Key.Key_Escape and self.idLivro:
            apagarLivro(self.idLivro)
        self.accept()

    def closeEvent(self, event):
        """Checa se algum arquivo pdf foi upado \n
        sem finalizar o cadastro apertando o X"""
        if self.idLivro:
            apagarLivro(self.idLivro)
        event.accept()
