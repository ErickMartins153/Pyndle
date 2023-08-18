from PyQt6 import QtWidgets, QtGui, QtCore
import sys
from src.view.components.dashboard.Dashboard import Dashboard
from src.view.assets.styles import non_css_styles


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(open('assets/styles/style.css').read())
        self.resize(720, 512)

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
        self.paginas.setGraphicsEffect(non_css_styles.BoxShadow(QtGui.QColor(0, 0, 0, 85), 4, 5, 4))

        # Instância dashboard (pagina)
        dashboard = Dashboard(self.paginas)
        self.paginas.addWidget(dashboard)
        # Instância biblioteca (pagina)
        biblioteca = QtWidgets.QWidget(self.paginas)
        self.paginas.addWidget(biblioteca)
        # Instância catalogo (pagina)
        catalogo = QtWidgets.QWidget(self.paginas)
        self.paginas.addWidget(catalogo)


application = QtWidgets.QApplication(sys.argv)
janela = MainWindow()
janela.show()
sys.exit(application.exec())
