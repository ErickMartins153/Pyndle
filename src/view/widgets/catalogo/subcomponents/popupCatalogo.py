from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QLabel,
    QPushButton,
)
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import Qt, pyqtSignal
from src.view.widgets.moduloLivro.Popup import Popup
from src.controller.telaPreviaLivro import dadosLivro
from src.controller.telaInicial import dadosUsuario
from src.controller.telaPrincipal import adicionarlivrosPessoais
from src.view.utils.imageTools import getResizedImage, relHeight, relWidth
from src.view.utils import widgetSearch

class PopupCatalogo(QDialog):
    # Sinais
    sinalLivroAdicionado = pyqtSignal()

    def __init__(self, nomeUsuario: str, idLivro: int, parent):
        super().__init__()
        # atributos ----------------------------------------------
        self.idLivro = idLivro
        self.nomeUsuario = nomeUsuario
        self.idUsuario = dadosUsuario(nomeUsuario)["idUsuario"]
        self.parent = parent
        self.dadosLivro = dadosLivro(idLivro)
        self.titulo = self.dadosLivro["titulo"]
        self.genero = self.dadosLivro["genero"]
        self.autor = self.dadosLivro["autor"]
        self.anoPublicacao = self.dadosLivro["anoPublicacao"]
        self.capaLivro = getResizedImage(
            self.dadosLivro["capaLivro"], relWidth(240, 1920), relHeight(336, 1080)
        )
        self.arquivoPDF = self.dadosLivro["arquivoPdf"]
        self.qtdPaginas = self.dadosLivro["pagTotal"]

        # Configurações-------------------------------------------

        self.setStyleSheet(open("src/view/assets/styles/popup.css").read())
        self.setWindowTitle(self.titulo)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setFixedSize(700, 450)
        self.setWindowFlag(Qt.WindowType.Window, False)
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)


        # ---------------------------------------------------------
        layout = QHBoxLayout()
        layout.setObjectName("fundo")
        self.setLayout(layout)

        groupImagemBotao = QFrame(self)
        groupImagemBotao.setObjectName("groupImagemBotao")
        # groupImagemBotao.setFixedSize(300, 660)
        layout.addWidget(groupImagemBotao)

        ImagemBotaoLayout = QVBoxLayout()
        ImagemBotaoLayout.setObjectName("ImagemBotaoLayout")
        ImagemBotaoLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        groupImagemBotao.setLayout(ImagemBotaoLayout)

        imagemCapaLivro = QImage.fromData(self.capaLivro)
        capa = QLabel(self)
        pixmap = QPixmap.fromImage(imagemCapaLivro)
        capa.setPixmap(pixmap)

        # colocar um espaço em cima e embaixo da capa, garantindo que ela fique no centro do frame
        ImagemBotaoLayout.addStretch()
        ImagemBotaoLayout.addWidget(capa, alignment=Qt.AlignmentFlag.AlignCenter)
        ImagemBotaoLayout.addStretch()

        AdicionarBibliotecaBotao = QPushButton(groupImagemBotao)
        AdicionarBibliotecaBotao.setObjectName("lerLivroBotao")
        AdicionarBibliotecaBotao.setText("Adicionar livro")
        AdicionarBibliotecaBotao.clicked.connect(self.adicionarBiblioteca)
        ImagemBotaoLayout.addWidget(AdicionarBibliotecaBotao)

        groupInfos = QFrame(self)
        groupInfos.setObjectName("groupTexto")
        # groupInfos.setFixedHeight(660)
        layout.addWidget(groupInfos)

        infosLayout = QVBoxLayout()
        infosLayout.setObjectName("infosLayout")
        groupInfos.setLayout(infosLayout)

        h1 = QLabel("Informações do livro")
        infosLayout.addWidget(h1)
        h1.setObjectName("h1")
        h1.setMaximumHeight(50)

        tituloLabel = QLabel(f"Titulo: {self.titulo}")
        tituloLabel.setObjectName("info")
        tituloLabel.setMaximumHeight(20)
        infosLayout.addWidget(tituloLabel)

        generoLabel = QLabel(f"Gênero: {self.genero}")
        generoLabel.setObjectName("info")
        generoLabel.setMaximumHeight(20)
        infosLayout.addWidget(generoLabel)

        autorLabel = QLabel(f"Autor: {self.autor}")
        autorLabel.setMaximumHeight(20)
        autorLabel.setObjectName("info")
        infosLayout.addWidget(autorLabel)

        anoLabel = QLabel(f"Ano: {self.anoPublicacao}")
        anoLabel.setMaximumHeight(20)
        anoLabel.setObjectName("info")
        infosLayout.addWidget(anoLabel)

        qtdPaginasLabel = QLabel(f"Total de páginas: {self.qtdPaginas}")
        qtdPaginasLabel.setMaximumHeight(20)
        qtdPaginasLabel.setObjectName("info")
        infosLayout.addWidget(qtdPaginasLabel)

        layoutBotaoFechar = QVBoxLayout()
        layoutBotaoFechar.setAlignment(Qt.AlignmentFlag.AlignBottom)
        botaoFechar = QPushButton("Fechar", self)
        botaoFechar.clicked.connect(self.accept)
        layoutBotaoFechar.addWidget(botaoFechar)

        # Adicionar layout botão fechar ao layout principal
        infosLayout.addLayout(layoutBotaoFechar)
        self.setLayout(layout)


    def adicionarBiblioteca(self):
        adicionarlivrosPessoais(self.idUsuario, self.idLivro)
        self.hide()

        # Abre PopUp de "Minha Biblioteca"
        popUpBiblioteca = Popup(self.nomeUsuario, self.idLivro, self)
        # Quando o livro for apagado, manda sinal para atualizar a dashboard
        try:
            popUpBiblioteca.sinalLivroApagado.connect(self.parent.atualizarLivros)
        except AttributeError:
            pass

        #Emite sinal que o livro foi adicionado para atualizar a dashboard
        self.sinalLivroAdicionado.emit()
        popUpBiblioteca.exec()
        self.close()
