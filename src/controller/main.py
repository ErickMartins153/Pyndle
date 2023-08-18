from PyQt6 import QtWidgets
import sys
from src.view.janelinha import Dashboard

application = QtWidgets.QApplication(sys.argv)
janela = Dashboard()
janela.show()
sys.exit(application.exec())
