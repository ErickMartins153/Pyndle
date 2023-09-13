from PyQt6 import QtWidgets, QtGui, QtCore
import pyautogui
import sys
from src.view.components.login.TelaLogin import TelaLogin
from src.view.components.dashboard.Dashboard import Dashboard
from src.view.components.catalogo.TelaCatalogo import TelaCatalogo
from src.view.assets.styles import non_css_styles
from src.view.utils.imageTools import relHeight, relWidth


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
        self.setAcceptDrops(True)
        self.setObjectName("mainWindow")

        QtGui.QFontDatabase.addApplicationFont("src/view/assets/fonts/Baskervville.ttf")
        self.setStyleSheet(open('src/view/assets/styles/mainWindow.css').read())
        self.setMinimumSize(relWidth(1300, 1920), relHeight(980, 1080))
        #self.currentSize = {"width": self.width(), "height": self.height()}

        # Central QWidget (mainWindowSpace)
        mainWindowSpace = QtWidgets.QWidget(self)
        mainWindowSpace.setObjectName("mainWindowSpace")
        self.setCentralWidget(mainWindowSpace)

        # mainWindowLayout
        mainWindowLayout = QtWidgets.QVBoxLayout()
        mainWindowLayout.setContentsMargins(relWidth(25, 1920), relHeight(15, 1080), relWidth(25, 1920), relHeight(15, 1080))
        mainWindowSpace.setLayout(mainWindowLayout)

        # QStackedWidget (paginas) ---------------------------------
        self.paginas = QtWidgets.QStackedWidget(self)
        self.paginas.setObjectName("paginas")
        mainWindowLayout.addWidget(self.paginas)
        self.paginas.setGraphicsEffect(
            non_css_styles.BoxShadow(QtGui.QColor(0, 0, 0, 85), relWidth(4, 1920), relHeight(5, 1080), 4)
        )


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
        catalogo = TelaCatalogo(self.paginas)
        catalogo.setObjectName("catalogo")
        self.paginas.addWidget(catalogo)

        self.paginas.setCurrentIndex(0)


    def getUsuario(self):
        return self.usuarioAtual

    def setUsuario(self, tuplaUsuario: tuple):
        self.usuarioAtual = tuplaUsuario
