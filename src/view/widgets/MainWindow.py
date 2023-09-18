from PyQt6 import QtWidgets, QtGui
from src.view.widgets.login.TelaLogin import TelaLogin
from src.view.widgets.dashboard.Dashboard import Dashboard
from src.view.widgets.minhaBiblioteca.TelaMinhaBiblioteca import TelaMinhaBiblioteca
from src.view.widgets.catalogo.TelaCatalogo import TelaCatalogo
from src.view.assets.styles import non_css_styles
from src.view.utils.imageTools import relHeight, relWidth
from src.view.utils.container import verticalWidget


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        """
        Janela principal que contém todos os outros widgets e funcionalidades

        ATRIBUTOS:
            - usuarioAtual (tuple): possui todas as informações do usuário atual. É definida após o ação de logar
        """
        # ATRIBUTOS ----------------------------------
        self.usuarioAtual = tuple()

        # CONFIGURAÇÕES ------------------------------
        super().__init__()
        self.setAcceptDrops(True)
        self.setObjectName("mainWindow")

        QtGui.QFontDatabase.addApplicationFont("src/view/assets/fonts/Poppins.ttf")
        self.setStyleSheet(open("src/view/assets/styles/mainWindow.css").read())
        self.setMinimumSize(relWidth(1300, 1920), relHeight(980, 1080))


        # WIDGET CENTRAL ----------------------------------------------------
        mainWindowSpace = verticalWidget(self, "mainWindowSpace")
        mainWindowSpace.layout().setContentsMargins(
            relWidth(25, 1920),
            relHeight(15, 1080),
            relWidth(25, 1920),
            relHeight(15, 1080),
        )
        self.setCentralWidget(mainWindowSpace)


        # STACKED WIDGET (contém as janelas) ---------------------------------
        self.paginas = QtWidgets.QStackedWidget(self)
        self.paginas.setObjectName("paginas")

        # Definindo efeito de DropShadow
        self.paginas.setGraphicsEffect(non_css_styles.BoxShadow(
            QtGui.QColor(0, 0, 0, 85),
            relWidth(4, 1920),
            relHeight(5, 1080), 4
            )
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
        biblioteca = TelaMinhaBiblioteca(self.paginas)
        biblioteca.setObjectName("biblioteca")
        self.paginas.addWidget(biblioteca)
        # Instância catalagoEMinhaBiblioteca (pagina)
        catalogo = TelaCatalogo(self.paginas)
        catalogo.setObjectName("catalago")
        self.paginas.addWidget(catalogo)


        mainWindowSpace.layout().addWidget(self.paginas)
        # self.paginas.setCurrentIndex(0)

    # (MÉTODOS) ---------------------------------------------

    def getUsuario(self):
        """
        Obtém dados do usuário atual que está logado\n
        **OBS: Utilizado em funções, classes ou métodos que precisam obter informações do usuário**
        """
        return self.usuarioAtual


    def setUsuario(self, tuplaUsuario: tuple):
        """
        Define o usuário atual que está logado
        :param tuplaUsuario:
        """
        self.usuarioAtual = tuplaUsuario
