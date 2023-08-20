from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
from src.view.components.Menu import Menu
from src.view.components.dashboard.FundoDashboard import FundoDashboard


class Dashboard(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget):
        """
        Widget utilizado para modelar a dashboard presente na "MainWindow.py"\n
        Obs.: Utiliza o componente Menu.py

        :param parent: Define o parente do widget
        """

        super().__init__()
        self.setParent(parent)

        dashboardLayout = QtWidgets.QVBoxLayout()
        dashboardLayout.setSpacing(0)
        self.setLayout(dashboardLayout)

        # QFrame (menu) ------------------------------
        menu = Menu(self)
        menu.setObjectName("menu")
        dashboardLayout.addWidget(menu)

        # QFrame (fundo) -----------------------------
        fundo = FundoDashboard(self)
        fundo.setObjectName("fundo")
        dashboardLayout.addWidget(fundo)
