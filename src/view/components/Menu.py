from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from src.view.components.FotoPerfil import FotoPerfil

class Menu(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget):
        """
        Widget utilizado para modelar o Menu/NavBar do aplicativo

        :param parent: Define o parente do widget
        """

        super().__init__()
        self.setParent(parent)
        self.setStyleSheet(open('src/view/assets/styles/menu.css').read())
        self.setMaximumHeight(70)

        menuLayout = QtWidgets.QHBoxLayout()
        menuLayout.setContentsMargins(20, 15, 20, 15)
        self.setLayout(menuLayout)

        # Logo -------------------------------
        fundoLogo = QtWidgets.QFrame(self)
        fundoLogo.setObjectName("fundoLogo")
        menuLayout.addWidget(fundoLogo)

        fundoLogoLayout = QtWidgets.QHBoxLayout()
        fundoLogoLayout.setContentsMargins(5, 0, 5, 0)
        fundoLogoLayout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        fundoLogo.setLayout(fundoLogoLayout)

        pyndleLogo = QtWidgets.QLabel(fundoLogo)
        pyndleLogo.setObjectName("pyndleLogo")
        pyndleLogo.setText("Pyndle")
        fundoLogoLayout.addWidget(pyndleLogo)

        # Distancia1 ----------------------------
        distancia1 = QtWidgets.QSpacerItem(40, 40)
        menuLayout.addSpacerItem(distancia1)

        # QLineEdit (Barra Pesquisa) ------------
        pesquisa = QtWidgets.QLineEdit()
        menuLayout.addWidget(pesquisa)

        pesquisa.setObjectName("pesquisa")
        pesquisa.setMinimumSize(300, 25)
        pesquisa.setMaximumHeight(25)
        pesquisa.setPlaceholderText("Pesquisar")

        # Distancia2 ----------------------------
        distancia2 = QtWidgets.QSpacerItem(300, 40)
        menuLayout.addSpacerItem(distancia2)

        # botão de logout simplificado
        botao = QtWidgets.QPushButton("Sair")
        menuLayout.addWidget(botao)
        botao.clicked.connect(self.deslogar)
        
        # optei por simplificar a função de logout, para termos algo eficiente e funcional 
    def deslogar(self):
        QtWidgets.QMainWindow.close(self)
