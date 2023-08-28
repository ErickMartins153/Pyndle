from PyQt6 import QtWidgets, QtGui, QtCore
import sys
from src.view.components.dashboard.Dashboard import Dashboard
from src.view.components.login.TelaLogin import TelaLogin
from src.view.components.login.TelaRegistro import TelaRegistro
from src.view.assets.styles import non_css_styles


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(open("src/view/assets/styles/style.css").read())
        self.setMinimumSize(1024, 650)

        # Central QWidget (mainWindowSpace)
        mainWindowSpace = QtWidgets.QWidget(self)
        mainWindowSpace.setObjectName("mainWindowSpace")
        self.setCentralWidget(mainWindowSpace)

        # mainWindowLayout
        mainWindowLayout = QtWidgets.QVBoxLayout()
        mainWindowSpace.setLayout(mainWindowLayout)

        # QStackedWidget (paginas) ---------------------------------
        self.paginas = QtWidgets.QStackedWidget()
        mainWindowLayout.addWidget(self.paginas)
        self.paginas.setGraphicsEffect(
            non_css_styles.BoxShadow(QtGui.QColor(0, 0, 0, 85), 4, 5, 4)
        )

        # Instância login
        telaLogin = TelaLogin(self.paginas)
        self.paginas.addWidget(telaLogin)
        # Instância dashboard (pagina)
        dashboard = Dashboard(self.paginas)
        self.paginas.addWidget(dashboard)
        # Instância biblioteca (pagina)
        biblioteca = QtWidgets.QWidget(self.paginas)
        self.paginas.addWidget(biblioteca)
        # Instância catalogo (pagina)
        catalogo = QtWidgets.QWidget(self.paginas)
        self.paginas.addWidget(catalogo)
        # Instância Registro
        telaRegistro = TelaRegistro(self.paginas)
        self.paginas.addWidget(telaRegistro)
