import sqlite3

# Definindo conexão com o banco de dados
conexao = sqlite3.connect("src/model/Pyndle.db")
# Definindo cursor para gerenciar o banco de dados
sgbd = conexao.cursor()


def dadosLivro(idLivro: int):
    """
    Função que retorna todos os dados do livro em um dicionário, a partir de seu ID
    :param int idLivro: Id do livro que deseja acessar os dados
    :return: Retorna um **dicionário** com os dados, caso o livro exista, senão retorna **None**
    """

    # Coleta todos os dados acerca de um livro com base em seu ID
    sgbd.execute("""
        SELECT * FROM livros 
        WHERE idLivro = ?
    """, (idLivro,))

    dados = sgbd.fetchone()

    # Verifica se o livro existe
    if dados:
        # Obtém os nomes das colunas da tabela
        colunas = [desc[0] for desc in sgbd.description]

        # Cria um dicionário com coluna: valor
        dados_dict = dict(zip(colunas, dados))

        return dados_dict
    else:
        return None


def pegarAvaliacao(id_livro, id_usuario):
    """
    Retorna a avaliação de um livro com base no usuário
    :param id_livro: ID do livro do qual deseja obter a avaliação
    :param id_usuario: ID do usuário que deseja obter a avalição
    """

    # Obtém a avaliação de um livro com base em seu ID e no ID do usuário
    sgbd.execute("""
        SELECT avaliacao FROM usuariosLivros 
        WHERE idLivro = ? AND idUsuario = ?
    """, (id_livro, id_usuario,))

    resultado = sgbd.fetchone()

    # Verifica se a avaliação existe
    if resultado:
        return resultado[0]
    else:
        return None


def setPagAtual(id_usuario, id_livro, pag_lida):
    """
    Salva a página atual do livro que o usuário está lendo em pyndle.bd
    :param id_usuario: ID do usuário que está lendo o livro
    :param id_livro: ID do livro que está sendo lido
    :param pag_lida: Última página lida pelo usuário
    """

    # Verificar se já existe uma linha com o mesmo idUsuario e idLivro
    sgbd.execute("""
        SELECT COUNT(*) FROM usuariosLivros 
        WHERE idUsuario = ? AND idLivro = ?
    """, (id_usuario, id_livro))

    resultado = sgbd.fetchone()

    # Se não existir, insira o novo registro
    if resultado[0] == 0:
        sgbd.execute("""
            INSERT INTO usuariosLivros (idUsuario, idLivro, pagAtual) 
            VALUES (?, ?, ?)
        """, (id_usuario, id_livro, pag_lida))

        conexao.commit()

    # Caso ela exista, atualize o valor de pagina lida
    else:
        sgbd.execute("""
            UPDATE usuariosLivros SET pagAtual = ? 
            WHERE idUsuario = ? AND idLivro = ?
        """, (pag_lida, id_usuario, id_livro))

        conexao.commit()


def getPagAtual(id_livro, id_usuario):
    """
    Obtém a última página de determinado livro que o usuário leu
    :param id_livro: ID do livro do qual deseja obter a última páginas lida
    :param id_usuario: ID do usuário que deseja saber a última página lida
    """

    # Coleta a última página lida pelo usuário em pyndle.db
    sgbd.execute("""
        SELECT pagAtual FROM usuariosLivros 
        WHERE idLivro = ? AND idUsuario = ?
    """, (id_livro, id_usuario,))

    pagina = sgbd.fetchone()

    # Verifica se a página atual está definida
    if pagina:
        return pagina[0]
    else:
        return 0


def pagTotal(id_livro, pag_totais):
    """
    Salva o número total de páginas de um determinado livro em pyndle.db
    :param id_livro:
    :param pag_totais:
    :return:
    """

    # Execute a instrução SQL para inserir na coluna pagAtual
    sgbd.execute("""
        INSERT INTO livros (idLivro, pagTotal) 
        VALUES (?, ?)
    """, (id_livro, pag_totais))

    # Commit para salvar a alteração no banco de dados
    conexao.commit()


def salvarReview(idUsuario: int, idLivro: int, review: str):
    """
    Salva o review de um usuário acerca de um livro que ele leu
    :param idUsuario: ID do usuário que deseja salvar o review
    :param idLivro: ID do livro que receberá a review
    :param review: review que será feita pelo usuário acerca do livro
    :return:
    """

    # Insere a review em pyndle.db
    sgbd.execute("""
        INSERT INTO usuarioLivros (idUsuario, idLivro, review)
        VALUES (?, ?, ?)
    """, (idUsuario, idLivro, review))

    # Salva o review
    conexao.commit()


def salvarAvaliacao(idUsuario, idLivro, avaliacao):
    """
    Salva a avaliação de um usuário acerca de determinado livro
    :param idUsuario: ID do usuário que deseja avaliar o livro
    :param idLivro: ID do livro que está sendo avaliado
    :param avaliacao: Avaliação recebida pelo livro
    """

    # Obtém a avaliação existente acerca daquele livro
    existente = pegarAvaliacao(idLivro, idUsuario)

    # Caso a avaliação exista, ela é atualizada
    if existente is not None:
        sgbd.execute("""
            UPDATE usuariosLivros SET avaliacao = ? 
            WHERE idUsuario = ? AND idLivro = ?
        """, (avaliacao, idUsuario, idLivro))

    # Caso a avaliação não exista, ela é inserida em pyndle.db
    else:
        sgbd.execute("""
            INSERT INTO usuariosLivros (idUsuario, idLivro, avaliacao)
            VALUES (?, ?, ?)
        """, (idUsuario, idLivro, avaliacao))

    # Avaliação salva
    conexao.commit()
