import sqlite3

connection = sqlite3.connect('pyndle.db')
db = connection.cursor()

# Create tables (if not exist)
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

# Commit the changes and close the connection
connection.commit()
connection.close()
