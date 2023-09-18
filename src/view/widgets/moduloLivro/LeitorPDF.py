import fitz as PyMuPDF
from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QScrollArea,
    QWidget
)
from PyQt6.QtCore import pyqtSignal, Qt, QBuffer, QByteArray, QIODevice
from PyQt6.QtGui import QImage, QPixmap
from src.controller.telaPreviaLivro import setPagAtual, getPagAtual
from src.view.widgets.moduloLivro.DisplayPDF import DisplayPDF
from src.view.utils.imageTools import relHeight, relWidth, getScreenResolution, getResizedImage
from src.view.utils.container import verticalFrame, horizontalFrame


# ATENÇÃO: OS BOTÕES DE PASSAR PÁGINA E VOLTAR PÁGINA FORAM COMENTADOS PARA INUTILIZAR ELES E ASSIM
# ELES NÃO APARECEREM NA TELA, POIS ELES ESTAVAM BUGANDO O LAYOUT, PARA PASSAR AS PÁGINAS USE O SEU
# TECLADO COM AS SETAS DA DIREITA E ESQUERDA


class LeitorPDF(QDialog):
    sinalPaginaAtual = pyqtSignal(int)

    def __init__(self, idUsuario, idLivro, livroPdf, tituloLivro, parent):
        super().__init__(parent)

        # CONFIGURAÇÕES ----------------------------------
        self.setWindowTitle(tituloLivro)
        self.setMinimumSize(relWidth(550, 1920), relHeight(770, 1080))
        self.setObjectName("LeitorPDF")
        self.setStyleSheet(open("src/view/assets/styles/leitorPDF/LeitorPDF.css").read())
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowMaximizeButtonHint | Qt.WindowType.WindowMinimizeButtonHint)

        # Centralizando janela
        self.move(
            (getScreenResolution()["width"] - self.width()) // 2,
            (getScreenResolution()["height"] - self.height()) // 2
        )

        # LAYOUT -------------------------------------------

        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # ATRIBUTOS --------------------------------------
        self.idUsuario = idUsuario
        self.idLivro = idLivro
        self.paginaAtual = getPagAtual(self.idLivro, self.idUsuario)
        self.documentoPdf = PyMuPDF.open(stream=livroPdf, filetype="pdf")
        self.totalPaginas = len(self.documentoPdf)

        # NAVBAR -----------------------------------------
        navBar = horizontalFrame(self, "navBar")
        navBar.setFixedHeight(relHeight(60, 1080))
        navBar.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(navBar)

        # Definindo botão de avançar
        self.botaoPaginaAnterior = QPushButton("<", navBar)
        self.botaoPaginaAnterior.clicked.connect(self.voltarPagina)
        self.botaoPaginaAnterior.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        navBar.layout().addWidget(self.botaoPaginaAnterior)

        # Definindo marcador de página
        self.labelPagina = QLabel(f"{self.paginaAtual} / {self.totalPaginas}")
        self.labelPagina.setObjectName("labelPagina")

        self.labelPagina.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelPagina.setMinimumWidth(relWidth(150, 1920))
        self.labelPagina.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.labelPagina.setStyleSheet(f"""
            font-size: {relHeight(20, 1080)}px;
            border-radius: {relHeight(10, 1080)}px;
        """)

        navBar.layout().addWidget(self.labelPagina)

        # Definindo botão de voltar
        self.botaoProximaPagina = QPushButton(">", navBar)
        self.botaoProximaPagina.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.botaoProximaPagina.clicked.connect(self.passarPagina)
        navBar.layout().addWidget(self.botaoProximaPagina)

        # DISPLAY DO LIVRO ---------------------------------------

        self.displayPDF = DisplayPDF(self, "DisplayPDF")
        self.layout.addWidget(self.displayPDF)

        # DEFININDO PÁGINA
        self.mostrarPagina()

        # Defina o foco do teclado na janela
        self.setFocus()

    def mostrarPagina(self):
        if self.paginaAtual == self.totalPaginas:
            self.paginaAtual -= 1
        if self.documentoPdf is not None and 0 <= self.paginaAtual < self.totalPaginas:
            # Obtendo página
            pagina = self.documentoPdf[self.paginaAtual]

            # Extraindo pixmap da páginas
            imagem_pymupdf = pagina.get_pixmap()

            # Criando QImage
            imagem_qt = QImage(
                imagem_pymupdf.samples,
                imagem_pymupdf.width,
                imagem_pymupdf.height,
                imagem_pymupdf.stride,
                QImage.Format.Format_RGB888,
            )

            # Definindo QPixmap
            pixmap = QPixmap.fromImage(imagem_qt)

            if pixmap.height() < getScreenResolution()["height"]:
                # Obtendo proporção
                height = pixmap.height() * getScreenResolution()["height"] // pixmap.height()
                print(height)
                width = pixmap.width() * getScreenResolution()["height"] // pixmap.height()
                print(width)
                # Redimensionando
                resizedPixmap = self.getResizedPixmap(pixmap, width, height)

                # Envia o pixmap redimensionado
                self.displayPDF.definirPagina(resizedPixmap)
                return

            # Enviando QPixmap para o display de pdf
            self.displayPDF.definirPagina(pixmap)


    def passarPagina(self):
        if self.documentoPdf is not None and self.paginaAtual < self.totalPaginas - 1:
            self.paginaAtual += 1
            self.labelPagina.setText(f"{self.paginaAtual} / {self.totalPaginas}")
            self.mostrarPagina()

    def voltarPagina(self):
        if self.documentoPdf is not None and self.paginaAtual > 0:
            self.paginaAtual -= 1
            self.labelPagina.setText(f"{self.paginaAtual} / {self.totalPaginas}")
            self.mostrarPagina()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Right or event.key() == 68:
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

    def getResizedPixmap(self, pixmap: QPixmap, width: int, height: int):

        ba = QByteArray()
        buff = QBuffer(ba)
        buff.open(QIODevice.OpenModeFlag.WriteOnly)
        pixmap.save(buff, "PNG")

        bimage = ba.data()

        resizedBimage = getResizedImage(bimage, width, height)

        resizedPixmap = QPixmap().fromImage(QImage.fromData(resizedBimage))

        return resizedPixmap