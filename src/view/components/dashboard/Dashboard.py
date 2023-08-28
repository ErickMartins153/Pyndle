from PyQt6 import QtWidgets
from src.view.components.Menu import Menu
from src.view.components.dashboard.subcomponents.FundoDashboard import FundoDashboard


class Dashboard(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget):
        """
        Widget utilizado para modelar a dashboard presente na "MainWindow.py"\n
        Obs.: Utiliza o componente Menu.py

        :param parent: Define o parente do widget
        """
        # Configurações
        super().__init__()
        self.setParent(parent)

        # Definição do layout
        dashboardLayout = QtWidgets.QVBoxLayout()
        dashboardLayout.setSpacing(0)
        self.setLayout(dashboardLayout)

        # QFrame (menu) ------------------------------
        menu = Menu(self)
        menu.setObjectName("menu")
        dashboardLayout.addWidget(menu)

        # QFrame (fundo) -----------------------------
        fundoDashboard = FundoDashboard(self)
        fundoDashboard.setObjectName("fundoDashboard")
        dashboardLayout.addWidget(fundoDashboard)
