import sqlite3

conexao = sqlite3.connect("../model/Pyndle.db")
sgbd = conexao.cursor()


def logar(nomeUsuario: str, senha: str):

    """
    Esse função é apenas um exemplo de como vocês podem montar as funções
    sem levar em consideração a interface

    Elas sempre retornarão um valor, dependendo da necessidade. No caso do
    login, eu coloquei para retornar True caso a senha corresponda a alguma
    do banco de dados, pensando que quem está no front irá usar ela para passar
    o usuário e senha e identificar se aquele usuário existe ou não.

    Outro exemplo de função que vocês poderiam fazer é uma que pegasse o
    usuario e senha passados no parâmetro e retornasse o ID do usuário
    para que esse ID fosse usado pelo pessoal do front para definir o ID
    atual do usuário que está usando o app no momento. Isso pode servir
    pra gente fazer outras funções com base no ID

    No caso, pensando que o usuário já está logado e o ID do usuário atual
    foi definido com a função que falei anteriormente, poderia ter uma função
    que recebesse o ID do usuário e acessasse o banco de dados naquele ID e
    retornasse uma lista com todos os livros da minha biblioteca, organizados
    em tuplas com (título, autor, arquivo do livro(binario)

    Enfim, essa é a minha ideia
    """

    sgbd.execute("""
    SELECT senha FROM usuarios
    WHERE login = ?
    """, (nomeUsuario,))

    resultado = sgbd.fetchall()  # O fetchall retorna uma lista com tuplas dos registros

    if len(resultado) != 0 and resultado[0][0] == senha:
        return True
    else:
        return False


'''
# Vocês podem testar as funções aqui no próprio código
# Aqui eu testei a função logar (só pra facilitar e testar se funciona ou não
# Depois apagar, é claro kkkkkkkkkkk

nome = "michael"
senha = "123"
existe = logar(nome, senha)
print(existe)
'''
