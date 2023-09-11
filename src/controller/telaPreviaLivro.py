import sqlite3

conexao = sqlite3.connect("src/model/Pyndle.db")
sgbd = conexao.cursor()


def dadosLivro(idLivro: int):
    """
    Função que retorna todos os dados do livro em um dicionário, a partir de seu ID
    :param int idLivro: Id do livro que deseja acessar os dados
    :return: Retorna um **dicionário** com os dados, caso o livro exista, senão retorna **None**
    """
    sgbd.execute("SELECT * FROM livros WHERE idLivro = ?", (idLivro,))
    dados = sgbd.fetchone()

    if dados:
        # Obtém os nomes das colunas da tabela
        colunas = [desc[0] for desc in sgbd.description]

        # Cria um dicionário com coluna: valor
        dados_dict = dict(zip(colunas, dados))

        return dados_dict
    else:
        print(f"O livro com ID {idLivro} não foi encontrado.")
        return None


def pegarAvaliacao(id_livro, id_usuario):

    sgbd.execute("SELECT avaliacao FROM usuariosLivros WHERE idLivro = ? AND idUsuario = ?", (id_livro, id_usuario,))
    resultado = sgbd.fetchone()

    if resultado:
        return resultado[0]
    else:
        return "Livro não encontrado ou sem avaliação."

            

def salvarPag(id_usuario, id_livro, pag_lida):
  
    # Execute a instrução SQL para atualizar a coluna pagAtual
    sgbd.execute("UPDATE usuariosLivros SET pagAtual = ? WHERE idUsuario = ? AND idLivro = ?", (pag_lida, id_usuario, id_livro))
    
    # Commit para salvar a alteração no banco de dados
    connection.commit()
    print("Pagina atualizada com sucesso.")


def pagTotal(id_livro, pag_totais):
    
    # Execute a instrução SQL para inserir na coluna pagAtual
    sgbd.execute("INSERT INTO livros (idLivro, pagTotal) VALUES (?, ?)", (id_livro, pag_totais))

    # Commit para salvar a alteração no banco de dados
    connection.commit()
    print("Número de páginas inserido com sucesso")
