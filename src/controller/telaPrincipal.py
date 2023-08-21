import sqlite3
import fitz as PyMuPDF

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

file = 'livro_teste.pdf'  # Substitua pelo nome do arquivo que deseja inserir

id_usuario = 5 # Substitua pelo ID real do livro que você deseja inserir

# Função para fazer o upload do arquivo PDF
def uploadLivro(arquivo, idUsuario):
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
        sgbd.execute("INSERT INTO livro(arquivoPdf, titulo, genero, autor, anoPublicacao, review, pagTotais) VALUES (?,?,?,?,?,?,?)",
                    (sqlite3.Binary(pdf_content), titulo, genero, autor, ano, review, paginas))
