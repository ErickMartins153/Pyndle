import os, io
from PIL import Image
from PIL.ImageQt import ImageQt

def getImages():
    diretorio = "myfiles/imagens"
    lista = []

    for nome_arquivo in os.listdir(diretorio):
        with open(os.path.join("myfiles/imagens", nome_arquivo), "rb") as imagem:
            lista.append((nome_arquivo, imagem.read()))
    return lista
