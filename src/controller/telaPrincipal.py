import sqlite3
import fitz as PyMuPDF

conexao = sqlite3.connect("src/model/Pyndle.db")
sgbd = conexao.cursor()

def livrosCatalogo():
    """
    Função que dá todas as colunas dos nossos 7 livros do catalogo
    """
    sgbd.execute("""
    SELECT * FROM livros
     WHERE idLivro IN (1, 2, 3, 4, 5, 6, 7)
     """)

    resultado = sgbd.fetchall()

    return resultado


def livrosPessoais(idUsuario: int):
    sgbd.execute("""
                 SELECT livros.* FROM livros 
                 JOIN usuariosLivros ON livros.idLivro = usuariosLivros.idLivro
                 WHERE usuariosLivros.idUsuario = (?)""", (idUsuario,))
    resultado = sgbd.fetchall()
    return resultado


def uploadLivro(arquivo, idUsuario):
    """
    Função para fazer o upload do arquivo PDF
    :param arquivo: arquivo PDF que deseja salvar
    :param idUsuario: id do usuário que está salvando o livro
    """
    # Abre o arquivo PDF
    livro = PyMuPDF.open(file)

    # Recupera o conteúdo do PDF como bytes
    pdf_content = open(file, 'rb').read()

    # Recupera os metadados do PDF
    titulo = livro.metadata.get('title', 'Sem título')
    autor = livro.metadata.get('author', 'Sem autor')
    ano = livro.metadata.get('creationDate', 'Sem data de criação')
    genero = input("Digite o gênero do livro: ")
    review = input("Digite a review do livro: ")
    paginas = livro.page_count

    # Insere os dados do livro, incluindo o conteúdo do PDF, na tabela do banco de dados
    sgbd.execute("""
    INSERT INTO livros(arquivoPdf, titulo, genero, autor, anoPublicacao, pagTotal) 
    VALUES (?,?,?,?,?,?)
    """, (sqlite3.Binary(pdf_content), titulo, genero, autor, ano, review, paginas))



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
    arquivoPdfBytes = open(arquivoPdf, 'rb').read()

    sgbd.execute("INSERT INTO livros (titulo, genero, autor, anoPublicacao, arquivoPdf) VALUES (?, ?, ?, ?, ?)",
                 (titulo, genero, autor, anoPublicacao, arquivoPdfBytes))
