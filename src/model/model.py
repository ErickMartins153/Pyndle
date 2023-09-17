import sqlite3

# Definindo conexão com o banco de dados
connection = sqlite3.connect('pyndle.db')
# Definindo cursor para gerenciar o banco de dados
db = connection.cursor()


# Cria as tabelas caso não exista em pyndle.db

# Criando tabela de livros
db.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        idLivro INTEGER PRIMARY KEY,
        titulo TEXT DEFAULT 'Sem título',
        genero TEXT DEFAULT 'Não informado',       
        autor TEXT DEFAULT 'Não informado',        
        anoPublicacao TEXT DEFAULT 'Não informado',
        capaLivro BLOB,
        arquivoPdf BLOB,
        pagTotal INTEGER
    )
""")

# Criando tabela de usuários
db.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        idUsuario INTEGER PRIMARY KEY,
        login TEXT NOT NULL,
        senha TEXT NOT NULL,
        primeiroNome TEXT DEFAULT 'Fulano(a)',
        sobreNome TEXT DEFAULT 'Não informado',
        fotoPerfil BLOB
    )
""")

# Criando tabela de anotação de páginas
db.execute("""
    CREATE TABLE IF NOT EXISTS paginasAnotadas (
        numPagina INTEGER,
        idUsuario INTEGER,
        idLivro INTEGER,
        anotacao TEXT,
        PRIMARY KEY(idUsuario, idLivro, numPagina),
        FOREIGN KEY(idUsuario) REFERENCES usuarios(idUsuario),
        FOREIGN KEY(idLivro) REFERENCES livros(idLivro)
    )
""")

# Criando tabela de relacionamento entre usuários e livros
db.execute("""
    CREATE TABLE IF NOT EXISTS usuariosLivros (
        idUsuario INTEGER,
        idLivro INTEGER,
        review TEXT,
        pagAtual INTEGER DEFAULT 0,
        percentual FLOAT DEFAULT 0,
        avaliacao INTEGER DEFAULT 0,
        PRIMARY KEY(idUsuario, idLivro),
        FOREIGN KEY(idUsuario) REFERENCES usuarios(idUsuario),
        FOREIGN KEY(idLivro) REFERENCES livros(idLivro)
    )
""")

# Salva as alterações feitas em pyndle.db
connection.commit()
connection.close()
