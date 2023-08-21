import sqlite3

conexao = sqlite3.connect("src/model/Pyndle.db")
sgbd = conexao.cursor()

def livrosCatalogo(): #Função que dá todas as colunas dos nossos 5 livros do catalogo. Daí você só precisa verificar como o output sai e pegar os dados de lá, qnd descobrir como pegar o PDF do sql a gnt tb ajusta isso.
    sgbd.execute("SELECT * FROM livros WHERE idLivro IN (1, 2, 3, 4, 5)")

    resultado = sgbd.fetchall()
    print(resultado)

def livrosPessoais(idUsuario: int):
    sgbd.execute("""
                 SELECT livros.* FROM livros 
                 JOIN usuariosLivros ON livros.idLivro = usuariosLivros.idLivro
                 WHERE usuariosLivros.idUsuario = (?)""",(idUsuario,))
    resultado = sgbd.fetchall()
    print(resultado)

#codigo pra testar se funcionou
#livrosPessoais(1)
#print("\n")
#livrosCatalogo()