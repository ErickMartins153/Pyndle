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
        return None


def pegarAvaliacao(id_livro, id_usuario):
    sgbd.execute(
        "SELECT avaliacao FROM usuariosLivros WHERE idLivro = ? AND idUsuario = ?",
        (
            id_livro,
            id_usuario,
        ),
    )
    resultado = sgbd.fetchone()

    if resultado:
        return resultado[0]
    else:
        return None


def setPagAtual(id_usuario, id_livro, pag_lida):
    # Verificar se já existe uma linha com o mesmo idUsuario e idLivro
    sgbd.execute(
        "SELECT COUNT(*) FROM usuariosLivros WHERE idUsuario = ? AND idLivro = ?",
        (id_usuario, id_livro),
    )
    resultado = sgbd.fetchone()

    # Se não existir, insira o novo registro
    if resultado[0] == 0:
        sgbd.execute(
            "INSERT INTO usuariosLivros (idUsuario, idLivro, pagAtual) VALUES (?, ?, ?)",
            (id_usuario, id_livro, pag_lida),
        )
        conexao.commit()

    # Caso ela exista, atualize o valor de pagina lida
    sgbd.execute(
        "UPDATE usuariosLivros SET pagAtual = ? WHERE idUsuario = ? AND idLivro = ?",
        (pag_lida, id_usuario, id_livro),
    )
    conexao.commit()


def getPagAtual(id_livro, id_usuario):
    sgbd.execute(
        "SELECT pagAtual FROM usuariosLivros WHERE idLivro = ? AND idUsuario = ?",
        (
            id_livro,
            id_usuario,
        ),
    )
    pagina = sgbd.fetchone()

    if pagina:
        return pagina[0]
    else:
        return 0


def pagTotal(id_livro, pag_totais):
    # Execute a instrução SQL para inserir na coluna pagAtual
    sgbd.execute(
        "INSERT INTO livros (idLivro, pagTotal) VALUES (?, ?)", (id_livro, pag_totais)
    )

    # Commit para salvar a alteração no banco de dados
    conexao.commit()

def salvarReview(idUsuario, idLivro, review):
    sgbd.execute(
        """
    INSERT INTO usuarioLivros (idUsuario, idLivro, review)
    VALUES (?, ?, ?)""",
        (idUsuario, idLivro, review),
    )

    conexao.commit()


def salvarAvaliacao(idUsuario, idLivro, avaliacao):
    existente = pegarAvaliacao(idLivro, idUsuario)

    if existente is not None:
        sgbd.execute(
            "UPDATE usuariosLivros SET avaliacao = ? WHERE idUsuario = ? AND idLivro = ?",
            (avaliacao, idUsuario, idLivro),
        )
    else:
        sgbd.execute(
            """
        INSERT INTO usuariosLivros (idUsuario, idLivro, avaliacao)
        VALUES (?, ?, ?)""",
            (idUsuario, idLivro, avaliacao),
        )
    conexao.commit()
