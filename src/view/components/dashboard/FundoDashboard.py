import os, pathlib

from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
from src.view.components.Menu import Menu
import sys

class FundoDashboard(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()
        self.setParent(parent)
        #path = os.fspath(pathlib.Path(__file__).parent.parent.pare / 'fundo_dashboard.css')
        self.setStyleSheet(open('assets/styles/fundo_dashboard.css').read())

        fundoLayout = QtWidgets.QVBoxLayout()
        self.setLayout(fundoLayout)

        # Label (Bem vindo)
        saudacao = QtWidgets.QLabel(self)
        saudacao.setObjectName("saudacao")
        fundoLayout.addWidget(saudacao)

        saudacao.setText("Bem vindo, <nome do usuario>!")
        saudacao.setMaximumHeight(20)
        saudacao.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # QFrame (Grupo: Minha Biblioteca) ----------------------------
        groupMyBiblioteca = QtWidgets.QFrame(self)
        groupMyBiblioteca.setObjectName("groupMyBiblioteca")
        fundoLayout.addWidget(groupMyBiblioteca)

        myBibliotecaLayout = QtWidgets.QVBoxLayout()
        myBibliotecaLayout.setSpacing(14)
        groupMyBiblioteca.setLayout(myBibliotecaLayout)

        # Label (Minha Biblioteca)
        myBibliotecaLabel = QtWidgets.QLabel(groupMyBiblioteca)
        myBibliotecaLabel.setObjectName("indicadorListaLivros")
        myBibliotecaLabel.setMaximumHeight(25)
        myBibliotecaLabel.setText("Minha Biblioteca")
        myBibliotecaLayout.addWidget(myBibliotecaLabel)

        # QFrame (Meus Livros)
        meusLivros = QtWidgets.QFrame(groupMyBiblioteca)
        meusLivros.setObjectName("listaLivros")
        myBibliotecaLayout.addWidget(meusLivros)

        meusLivrosLayout = QtWidgets.QGridLayout()
        meusLivros.setLayout(meusLivrosLayout)

        #verMais = QtWidgets.QPushButton()
        #verMais.setObjectName('verMais')
        #meusLivrosLayout.addWidget(verMais, 0, 1)

        # QFrame (Grupo: Catálogo) ----------------------------
        groupCatalogo = QtWidgets.QFrame(self)
        groupCatalogo.setObjectName("groupMyBiblioteca")
        fundoLayout.addWidget(groupCatalogo)

        catalogoLayout = QtWidgets.QVBoxLayout()
        catalogoLayout.setSpacing(14)
        groupCatalogo.setLayout(catalogoLayout)

        # Label (Catálogo)
        catalogoLabel = QtWidgets.QLabel(groupCatalogo)
        catalogoLabel.setMaximumHeight(25)
        catalogoLabel.setObjectName("indicadorListaLivros")
        catalogoLabel.setText("Catálogo")
        catalogoLayout.addWidget(catalogoLabel)

        # QFrame (Meus Livros)
        catalogoLivros = QtWidgets.QFrame(groupCatalogo)
        catalogoLivros.setObjectName("listaLivros")
        catalogoLayout.addWidget(catalogoLivros)

        catalogoLivrosLayout = QtWidgets.QGridLayout()
        catalogoLivros.setLayout(catalogoLivrosLayout)
