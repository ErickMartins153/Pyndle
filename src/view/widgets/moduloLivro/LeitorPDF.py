import fitz as PyMuPDF
from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QPushButton,
    QLabel,
)
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QImage, QPixmap
from src.controller.telaPreviaLivro import setPagAtual, getPagAtual

# ATENÇÃO: OS BOTÕES DE PASSAR PÁGINA E VOLTAR PÁGINA FORAM COMENTADOS PARA INUTILIZAR ELES E ASSIM
# ELES NÃO APARECEREM NA TELA, POIS ELES ESTAVAM BUGANDO O LAYOUT, PARA PASSAR AS PÁGINAS USE O SEU
# TECLADO COM AS SETAS DA DIREITA E ESQUERDA


class LeitorPDF(QDialog):
    sinalPaginaAtual = pyqtSignal(int)

    def __init__(self, idUsuario, idLivro, livroPdf, tituloLivro, parent):
        super().__init__(parent)
        self.setWindowTitle(tituloLivro)
        self.setGeometry(100, 30, 450, 700)
        self.layout = QVBoxLayout(self)
        self.setObjectName("LeitorPDF")

        self.idUsuario = idUsuario
        self.idLivro = idLivro

        self.paginaAtual = getPagAtual(self.idLivro, self.idUsuario)
        self.documentoPdf = PyMuPDF.open(stream=livroPdf, filetype="pdf")

        self.totalPaginas = len(self.documentoPdf)

        # Adicionando um QLabel para exibição de texto/imagem
        self.labelConteudo = QLabel(self)
        self.layout.addWidget(self.labelConteudo)

        # Adicione os botões à parte inferior do layout

        # self.botaoProximaPagina = QPushButton("Próxima Página", self)
        # self.botaoPaginaAnterior = QPushButton("Página Anterior", self)

        # self.layout.addWidget(self.botaoPaginaAnterior)
        # self.layout.addWidget(self.botaoProximaPagina)

        # Conecte os sinais após criar os botões

        # self.botaoProximaPagina.clicked.connect(self.passarPagina)
        # self.botaoPaginaAnterior.clicked.connect(self.voltarPagina)

        self.mostrarPagina()

        # Defina o foco do teclado na janela
        self.setFocus()

    def mostrarPagina(self):
        if self.paginaAtual == self.totalPaginas:
            self.paginaAtual -= 1
        if self.documentoPdf is not None and 0 <= self.paginaAtual < self.totalPaginas:
            pagina = self.documentoPdf[self.paginaAtual]

            
            imagem_pymupdf = pagina.get_pixmap()
            imagem_qt = QImage(
                imagem_pymupdf.samples,
                imagem_pymupdf.width,
                imagem_pymupdf.height,
                imagem_pymupdf.stride,
                QImage.Format.Format_RGB888,
            )
            pixmap = QPixmap.fromImage(imagem_qt)

            # Configurando o QLabel para exibir a imagem
            self.labelConteudo.setPixmap(pixmap)
            self.labelConteudo.setScaledContents(True)
            self.labelConteudo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
            # Atualize a visibilidade dos botões com base na página atual

            # self.botaoPaginaAnterior.setEnabled(self.paginaAtual > 0)
            # self.botaoProximaPagina.setEnabled(self.paginaAtual < self.totalPaginas - 1)

    def passarPagina(self):
        if self.documentoPdf is not None and self.paginaAtual < self.totalPaginas - 1:
            self.paginaAtual += 1
            self.mostrarPagina()

    def voltarPagina(self):
        if self.documentoPdf is not None and self.paginaAtual > 0:
            self.paginaAtual -= 1
            self.mostrarPagina()

    def keyPressEvent(self, event):
        """
        Navegar pelas páginas usando as teclas direita e esquerda.
        """
        if event.key() == Qt.Key.Key_Escape:
            return
        elif event.key() == Qt.Key.Key_Right or event.key() == 68:
            # Seta para a direita
            self.passarPagina()
        elif event.key() == Qt.Key.Key_Left or event.key() == 65:
            # Seta para a esquerda
            self.voltarPagina()

    def closeEvent(self, event):
        """
        Salvar em qual página o usuário estava ao fechar o PDF apertando o botão.
        """
        self.salvarPagina()
        event.accept()

    def salvarPagina(self):
        paginaAtual = self.paginaAtual
        if paginaAtual + 1 == self.totalPaginas:
            paginaAtual = self.totalPaginas
        setPagAtual(self.idUsuario, self.idLivro, paginaAtual)
        self.sinalPaginaAtual.emit(paginaAtual)
