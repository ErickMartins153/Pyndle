from PyQt6 import QtWidgets
from src.view.components.Menu import Menu
from src.view.widgets.dashboard.subcomponents.FundoDashboard import FundoDashboard


class Dashboard(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget):
        """
        Widget utilizado para modelar a dashboard presente na "MainWindow.py"\n

        :param parent: Define o parente do widget
        """

        # CONFIGURAÇÕES --------------------------------
        super().__init__()
        self.setParent(parent)
        self.setStyleSheet(open("src/view/assets/styles/dashboard/dashboard.css").read())

        # LAYOUT ---------------------------------------
        dashboardLayout = QtWidgets.QVBoxLayout()
        dashboardLayout.setSpacing(0)
        self.setLayout(dashboardLayout)

        # MENU ------------------------------------
        menu = Menu(self)
        menu.setObjectName("menu")
        dashboardLayout.addWidget(menu)

        # FUNDO DASHBOARD -----------------------------
        fundoDashboard = FundoDashboard(self)
        fundoDashboard.setObjectName("fundoDashboard")
        dashboardLayout.addWidget(fundoDashboard)
