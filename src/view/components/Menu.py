import sys
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from src.view.components.FotoPerfil import FotoPerfil
from PyQt6.QtWidgets import QApplication, QMainWindow

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    menu = Menu(window)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

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
        pesquisa.setMinimumSize(200, 37)
        pesquisa.setMaximumHeight(37)
        pesquisa.setPlaceholderText("Pesquisar")


        botaoPesquisa = QtWidgets.QPushButton()
        botaoPesquisa.setText("🔍")
        botaoPesquisa.setObjectName("botaoPesquisa")
        menuLayout.addWidget(botaoPesquisa)

        # Distancia2 ----------------------------
        distancia2 = QtWidgets.QSpacerItem(300, 40)
        menuLayout.addSpacerItem(distancia2)

        # botão de logout simplificado
        botao = QtWidgets.QPushButton()
        botao.setText("Sair")
        botao.setObjectName("sair")
        menuLayout.addWidget(botao)
        botao.clicked.connect(self.deslogar)
        

    def deslogar(self):
        QtWidgets.QApplication.quit()
