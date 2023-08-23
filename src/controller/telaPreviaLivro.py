# Função que a partir do id do livro oferece todos os dados registrados dele
def dadosLivro(idLivro):
    db.execute("SELECT * FROM livros WHERE idLivro = ?", (idLivro,))
    resultado = db.fetchone()

    if resultado:
        idLivro, titulo, genero, autor, anoPublicacao, capaLivro, arquivoPdf, pagTotal = resultado
        print(f"ID: {idLivro}, Título: {titulo}, Gênero: {genero}, Autor: {autor}, Ano de Publicação: {anoPublicacao}, Capa do Livro: {capaLivro}, Arquivo PDF: {arquivoPdf}, Páginas Totais: {pagTotal}")
    else:
        print(f"O livro com ID {idLivro} não foi encontrado.")
