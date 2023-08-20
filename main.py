from PyQt6 import QtWidgets
import sys
from src.view.MainWindow import MainWindow

if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    janela = MainWindow()
    janela.show()
    sys.exit(application.exec())
