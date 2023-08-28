def dadosLivro(idLivro: int):
    """
    Função que retorna todos os dados do livro em uma tupla, a partir de seu ID
    :param int idLivro: Id do livro que deseja acessar os dados
    :return: Retorna uma **tupla** com os dados, caso o livro exista, senão retorna **None**
    """
    db.execute("SELECT * FROM livros WHERE idLivro = ?", (idLivro,))
    dados = db.fetchone()

    if resultado:
        return dados
    else:
        print(f"O livro com ID {idLivro} não foi encontrado.")
        return None
