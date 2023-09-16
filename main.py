
from PyQt6 import QtWidgets, QtCore
import sys
from src.view.widgets.MainWindow import MainWindow

if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)

    # Fixando o DPI da aplicação
    application.setHighDpiScaleFactorRoundingPolicy(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.Round)

    janela = MainWindow()
    janela.show()
    sys.exit(application.exec())
