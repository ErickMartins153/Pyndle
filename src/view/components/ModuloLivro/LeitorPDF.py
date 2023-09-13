import fitz as PyMuPDF
from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QTextBrowser,
    QPushButton,
)
from PyQt6.QtCore import pyqtSignal
from src.controller.telaPreviaLivro import salvarPagAtual, pegarPagAtual


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

        self.textoBrowser = QTextBrowser(self)
        self.layout.addWidget(self.textoBrowser)

        self.botaoProximaPagina = QPushButton("Próxima Página", self)
        self.botaoProximaPagina.clicked.connect(self.passarPagina)
        self.layout.addWidget(self.botaoProximaPagina)

        self.botaoPaginaAnterior = QPushButton("Página Anterior", self)
        self.botaoPaginaAnterior.clicked.connect(self.voltarPagina)
        self.layout.addWidget(self.botaoPaginaAnterior)

        self.paginaAtual = pegarPagAtual(self.idLivro, self.idUsuario)
        self.documentoPdf = PyMuPDF.open(stream=livroPdf, filetype="pdf")

        self.totalPaginas = len(self.documentoPdf)
        self.mostrarPagina()

    def mostrarPagina(self):
        if self.documentoPdf is not None and 0 <= self.paginaAtual < len(
            self.documentoPdf
        ):
            pagina = self.documentoPdf[self.paginaAtual]
            texto = pagina.get_text()
            self.textoBrowser.setPlainText(texto)

    def passarPagina(self):
        if self.documentoPdf is not None and self.paginaAtual < self.totalPaginas - 1:
            self.paginaAtual += 1
            self.mostrarPagina()

    def voltarPagina(self):
        if self.documentoPdf is not None and self.paginaAtual > 0:
            self.paginaAtual -= 1
            self.mostrarPagina()

    def closeEvent(self, event):
        """
        Salvar em qual página o usuário estava \n
        ao fechar o PDF
        """
        paginaAtual = self.paginaAtual
        salvarPagAtual(self.idUsuario, self.idLivro, paginaAtual)
        self.sinalPaginaAtual.emit(paginaAtual)
        event.accept()
