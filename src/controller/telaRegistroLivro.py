# Essa função recebe como parâmetros a capa, o autor e o arquivo pdf do livro e os insere no banco de dados
def registroLivro(capaLivro, autor, arquivoPdf):
    # Abre o arquivo PDF
    livro = PyMuPDF.open(arquivoPdf)
    arquivoPdfBytes = open(arquivoPdf, 'rb').read()

    sgbd.execute("INSERT INTO livros (capaLivro, autor, arquivoPdf) VALUES (?, ?, ?)",
                 (capaLivro, autor, arquivoPdfBytes))

    sgbd.commit()
