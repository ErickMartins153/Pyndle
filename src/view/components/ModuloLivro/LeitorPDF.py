import os
import fitz
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QMessageBox, QApplication, QFileDialog
from PyQt6.QtGui import QImage, QPixmap, QPainter
from PyQt6.QtCore import Qt

class PDFLabel(QLabel):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.GlobalColor.white)
        super().paintEvent(event)

class LeitorPDF(QMainWindow):
    def __init__(self, pdf_path):
        super().__init__()

        self.pdf_path = pdf_path
        self.pdf_document = None
        self.current_page = 0

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.label = PDFLabel()
        self.layout.addWidget(self.label)

        if self.load_pdf():
            self.load_page()

    def load_pdf(self):
        if not os.path.exists(self.pdf_path) or not self.pdf_path.lower().endswith(".pdf"):
            QMessageBox.critical(None, "Erro", "Arquivo PDF não encontrado ou inválido")
            return False

        self.pdf_document = fitz.open(self.pdf_path)
        return True

    def load_page(self):
        if 0 <= self.current_page < len(self.pdf_document):
            page = self.pdf_document.load_page(self.current_page)
            image = page.get_pixmap()
            qimage = QImage(image.samples, image.width, image.height, image.stride, QImage.Format.FormatRGB888)
            pixmap = QPixmap.fromImage(qimage)

            self.label.setPixmap(pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Right:
            if self.current_page < len(self.pdf_document) - 1:
                self.current_page += 1
                self.load_page()
        elif event.key() == Qt.Key.Key_Left:
            if self.current_page > 0:
                self.current_page -= 1
                self.load_page()
        elif event.key() == Qt.Key.Key_Escape:
            self.close()

if __name__ == "__main__":
    app = QApplication([])

    options = QFileDialog.Options()
    pdf_path, _ = QFileDialog.getOpenFileName(None, "Abrir Arquivo PDF", "", "Arquivos PDF (*.pdf);;Todos os arquivos (*)", options=options)

    if not pdf_path:
        QMessageBox.critical(None, "Erro", "Nenhum arquivo PDF selecionado")
    else:
        leitor_pdf = LeitorPDF(pdf_path)
        leitor_pdf.show()

    app.exec()
