from PyQt6 import QtWidgets, QtGui, QtCore
import sys
from src.view.components.dashboard.Dashboard import Dashboard
from src.view.components.login.TelaLogin import TelaLogin
from src.view.assets.styles import non_css_styles


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        """
        Janela principal que contém todos os outros widgets e funcionalidades

        Atributos:
            - usuarioAtual (tuple): possui todas as informações do usuário atual. É definida após o ação de logar

        Métodos:
            - getUsuario(): retorna a tupla com as informações do usuário atual da aplicação
            - setUsuario(): define a tupla com as informações usuário atual da aplicação
        """
        # Atributos
        self.usuarioAtual = tuple()

        # Configurações
        super().__init__()
        self.setObjectName("mainWindow")
        self.setStyleSheet(open('src/view/assets/styles/style.css').read())
        self.setMinimumSize(1300, 900)

        # Central QWidget (mainWindowSpace)
        mainWindowSpace = QtWidgets.QWidget(self)
        mainWindowSpace.setObjectName("mainWindowSpace")
        self.setCentralWidget(mainWindowSpace)

        # mainWindowLayout
        mainWindowLayout = QtWidgets.QVBoxLayout()
        mainWindowSpace.setLayout(mainWindowLayout)

        # QStackedWidget (paginas) ---------------------------------
        self.paginas = QtWidgets.QStackedWidget(self)
        self.paginas.setObjectName("paginas")
        mainWindowLayout.addWidget(self.paginas)
        self.paginas.setGraphicsEffect(non_css_styles.BoxShadow(QtGui.QColor(0, 0, 0, 85), 4, 5, 4))


        # Instância login
        telaLogin = TelaLogin(self.paginas)
        telaLogin.setObjectName("telaLogin")
        self.paginas.addWidget(telaLogin)
        # Instância dashboard (pagina)
        dashboard = Dashboard(self.paginas)
        dashboard.setObjectName("dashboard")
        self.paginas.addWidget(dashboard)
        # Instância biblioteca (pagina)
        biblioteca = QtWidgets.QWidget(self.paginas)
        biblioteca.setObjectName("biblioteca")
        self.paginas.addWidget(biblioteca)
        # Instância catalogo (pagina)
        catalogo = QtWidgets.QWidget(self.paginas)
        catalogo.setObjectName("catalogo")
        self.paginas.addWidget(catalogo)

        self.paginas.setCurrentIndex(1)

    def getUsuario(self):
        return self.usuarioAtual

    def setUsuario(self, tuplaUsuario: tuple):
        self.usuarioAtual = tuplaUsuario
