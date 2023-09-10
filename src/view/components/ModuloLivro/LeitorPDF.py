import fitz  # PyMuPDF
from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QTextBrowser,
    QPushButton,
)


class LeitorPDF(QDialog):
    def __init__(self, livroPdf, tituloLivro):
        super().__init__()

        self.setWindowTitle(tituloLivro)
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout(self)

        self.text_browser = QTextBrowser(self)
        self.layout.addWidget(self.text_browser)

        self.botaoProximaPagina = QPushButton("Próxima Página", self)
        self.botaoProximaPagina.clicked.connect(self.passarPagina)
        self.layout.addWidget(self.botaoProximaPagina)

        self.botaoPaginaAnterior = QPushButton("Página Anterior", self)
        self.botaoPaginaAnterior.clicked.connect(self.voltarPagina)
        self.layout.addWidget(self.botaoPaginaAnterior)

        self.paginaAtual = 0
        self.pdf_document = fitz.open(stream=livroPdf, filetype="pdf")
        self.mostrarPagina()

    def mostrarPagina(self):
        if self.pdf_document is not None and 0 <= self.paginaAtual < len(
            self.pdf_document
        ):
            page = self.pdf_document[self.paginaAtual]
            text = page.get_text()
            self.text_browser.setPlainText(text)

    def passarPagina(self):
        if (
            self.pdf_document is not None
            and self.paginaAtual < len(self.pdf_document) - 1
        ):
            self.paginaAtual += 1
            self.mostrarPagina()

    def voltarPagina(self):
        if self.pdf_document is not None and self.paginaAtual > 0:
            self.paginaAtual -= 1
            self.mostrarPagina()
