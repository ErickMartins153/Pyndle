import sqlite3
import fitz as PyMuPDF
import io
from PIL import Image

conexao = sqlite3.connect(r"src\model\Pyndle.db")
conexao.row_factory = sqlite3.Row
sgbd = conexao.cursor()


def adicionarlivrosPessoais(idUsuario: int, idLivro: int):
    # Criando relação entre usuário atual e livro adicionado
    sgbd.execute(
        """
        INSERT OR IGNORE INTO usuariosLivros(idUsuario, idLivro, pagAtual, avaliacao) 
        VALUES (?, ?, ?, ?)
        """,
        (idUsuario, idLivro, 0, 0),
    )
    conexao.commit()


def uploadLivro(arquivo, idUsuario: int):
    try:
        # Abre o arquivo PDF
        livro = PyMuPDF.open(arquivo)
        conteudoPdf = open(arquivo, "rb").read()
        # Recupera a primeira página do PDF
        primeira_pagina = livro[0]

        # Converte a primeira página em uma imagem
        imagem = primeira_pagina.get_pixmap()

        # Cria uma imagem PIL a partir do Pixmap
        imagem_pil = Image.frombytes(
            "RGB", [imagem.width, imagem.height], imagem.samples
        )

        # Salva a imagem em um buffer como formato JPEG
        capaLivro = io.BytesIO()
        imagem_pil.save(capaLivro, format="JPEG")

        # Recupera os metadados do PDF
        titulo = livro.metadata.get("title")
        if not titulo.strip():
            titulo = "Sem título"
        autor = livro.metadata.get("author")
        if not autor.strip():
            autor = "Sem autor"
        ano = livro.metadata.get("creationDate")[2:6]
        if not ano.strip():
            ano = "Sem data de criação"
        genero = "Indeterminado"
        paginas = livro.page_count

        # Adicionando livro no banco de dados
        sgbd.execute(
            """
        INSERT INTO livros(arquivoPdf, titulo, genero, autor, anoPublicacao, pagTotal, capaLivro) 
        VALUES (?,?,?,?,?,?, ?)
        """,
            (
                conteudoPdf,
                titulo,
                genero,
                autor,
                ano,
                paginas,
                capaLivro.getvalue(),
            ),
        )
        conexao.commit()

        ultimoLivroId = sgbd.lastrowid
        adicionarlivrosPessoais(idUsuario, ultimoLivroId)

        return ultimoLivroId

    except Exception as e:
        print(e)
        print(f"Ocorreu um erro ao processar o arquivo PDF: {e}")


def checarRelacaoUsuarioLivro(idUsuario: int, idLivro: int):
    """
    Verifica se a relação entre aquele usuário e o livro já existe na tabela UsuariosLivros
    """
    sgbd.execute(f"""
    SELECT * FROM usuariosLivros 
    WHERE idUsuario = ? AND idLivro = ?
    """, (idUsuario, idLivro))

    resultado = sgbd.fetchall()

    if resultado:
        return True
    else:
        return False


def apagarLivro(idLivro: int, idUsuario: int):
    """
    Deleta o livro caso o usuário cancele o registro antes de finalizá-lo
    :param idLivro: id do livro
    :param idUsuario: id do usuário
    """
    sgbd.execute("SELECT idLivro FROM livros WHERE idLivro = ?", (idLivro,))
    resultado = sgbd.fetchone()
    conexao.commit()

    if resultado[0] == idLivro:
        sgbd.execute(
            """
        DELETE FROM livros 
        WHERE idLivro = ?
        """,
            (idLivro,),
        )
        conexao.commit()

        sgbd.execute(
            """DELETE FROM usuariosLivros 
        WHERE idLivro = ? AND idUsuario = ?
        """,
            (idLivro, idUsuario),
        )
        conexao.commit()


def updateDados(dados: dict, idLivro: int):
    sgbd.execute(
        """
        UPDATE livros SET titulo = ?, genero = ?, autor = ?, anoPublicacao = ? WHERE idLivro = ?
        """,
        (dados["titulo"], dados["genero"], dados["autor"], dados["ano"], idLivro),
    )
    conexao.commit()


def buscarPalavraChave(arquivo, palavraChave: str):
    """
    Função para buscar por uma palavra específica no livro
    :param arquivo: arquivo PDF no qual você deseja buscar a palavra
    :param palavraChave: palavra que deseja encontrar
    :return:
    """
    documento = PyMuPDF.open(arquivo)
    paginasEncontradas = []

    for paginaNum, pagina in enumerate(documento, start=1):
        texto = pagina.get_text()
        if palavraChave.lower() in texto.lower():
            paginasEncontradas.append(paginaNum)

    documento.close()
    # Retorna o número de todas as páginas do livro em que a palavra foi encontrada
    return paginasEncontradas


def adicionarLivroCatalogo(titulo, genero, autor, anoPublicacao, arquivoPdf):
    """
    Função para inserir livros no catálogo
    """
    # Abre o arquivo PDF
    livro = PyMuPDF.open(arquivoPdf)
    pagTotal = livro.page_count
    arquivoPdfBytes = open(arquivoPdf, "rb").read()

    sgbd.execute(
        "INSERT INTO livros (titulo, genero, autor, anoPublicacao, arquivoPdf) VALUES (?, ?, ?, ?, ?)",
        (titulo, genero, autor, anoPublicacao, arquivoPdfBytes),
    )


def filtrarCatalogo(genero: str = None, ordemAlfabetica: bool = None):
    # Começa com uma consulta base que seleciona todos os campos de livros da minha biblioteca
    consulta = "SELECT * FROM livros WHERE idLivro <= 7"

    # Verifica se o gênero foi especificado e adiciona a cláusula correspondente
    if genero is not None:
        consulta += f" AND genero = ?"

    # Adiciona a cláusula ORDER BY para ordenação alfabética, se necessário
    if ordemAlfabetica is not None:
        if ordemAlfabetica:
            consulta += " ORDER BY titulo ASC"
        else:
            consulta += " ORDER BY titulo DESC"

    # Cria uma tupla de parâmetros para a consulta
    parametros = ()

    if genero is not None:
        parametros += (genero,)

    # Executa a consulta com os parâmetros apropriados
    sgbd.execute(consulta, parametros)

    # Recupera os resultados da consulta
    resultado = sgbd.fetchall()

    return resultado


def filtrarBiblioteca(
    idUsuario, genero: str = None, avaliacao: int = None, ordemAlfabetica: bool = None
):
    # Começa com uma consulta base que seleciona todos os campos de livros do catálogo
    consulta = "SELECT * FROM livros WHERE idLivro IN (SELECT idLivro FROM usuariosLivros WHERE idUsuario = ?)"

    # Verifica se o gênero foi especificado e adiciona a cláusula correspondente
    if genero is not None:
        consulta += f" AND genero = ?"

    # Verifica se a avaliação foi especificada e adiciona a cláusula correspondente
    if avaliacao is not None:
        consulta += """
            AND idLivro IN (
                SELECT idLivro FROM usuariosLivros WHERE idUsuario = ? AND avaliacao = ?
            )
        """

    # Adiciona a cláusula ORDER BY para ordenação alfabética, se necessário
    if ordemAlfabetica is not None:
        if ordemAlfabetica:
            consulta += " ORDER BY titulo ASC"
        else:
            consulta += " ORDER BY titulo DESC"

    # Cria uma tupla de parâmetros para a consulta
    parametros = (idUsuario,)

    if genero:
        parametros += (genero,)
    if avaliacao:
        parametros += (
            idUsuario,
            avaliacao,
        )

    # Executa a consulta com os parâmetros apropriados
    sgbd.execute(consulta, parametros)

    # Recupera os resultados da consulta
    resultado = sgbd.fetchall()

    return resultado


def getGeneros():
    return (
        "Terror",
        "Fantasia",
        "Aventura",
        "Romance",
        "Matemática",
        "Geografia",
        "Linguagens",
        "Literatura",
    )
