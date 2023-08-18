import sqlite3

connection = sqlite3.connect('pyndle.db')
db = connection.cursor()

# Create tables (if not exist)
db.execute("""
CREATE TABLE IF NOT EXISTS livro (
    idLivro INTEGER PRIMARY KEY,
    titulo TEXT DEFAULT 'Sem título',
    genero TEXT DEFAULT 'Não informado',
    autor TEXT DEFAULT 'Não informado',
    anoPublicacao TEXT DEFAULT 'Não informado',
    review TEXT,
    pagTotais INTEGER,
    pagAtual INTEGER DEFAULT 0,
    avaliacao INTEGER DEFAULT 0,
    capaLivro BLOB,
    arquivoPdf BLOB
)
""")

db.execute("""
CREATE TABLE IF NOT EXISTS usuario (
    idUsuario INTEGER PRIMARY KEY,
    login TEXT NOT NULL,
    senha TEXT NOT NULL,
    primeiroNome TEXT DEFAULT 'Fulano(a)',
    sobreNome TEXT DEFAULT 'Não informado',
    fotoPerfil BLOB
)
""")

db.execute("""
CREATE TABLE IF NOT EXISTS paginaAnotadas (
    numPagina INTEGER,
    idUsuario INTEGER,
    idLivro INTEGER,
    anotacao TEXT,
    FOREIGN KEY(idUsuario) REFERENCES usuario(idUsuario),
    FOREIGN KEY(idLivro) REFERENCES livro(idLivro)
)
""")

db.execute("""
CREATE TABLE IF NOT EXISTS usuarioLivro (
    idUsuario INTEGER,
    idLivro INTEGER,
    PRIMARY KEY(idUsuario, idLivro),
    FOREIGN KEY(idUsuario) REFERENCES usuario(idUsuario),
    FOREIGN KEY(idLivro) REFERENCES livro(idLivro)
)
""")

# Dados pra teste e pra exemplificar como usar os comandos sql com python
db.execute("INSERT INTO livro(titulo, pagTotais) VALUES ('O Homem que Calculava', 200)")
db.execute("INSERT INTO livro(titulo, pagTotais) VALUES ('Barbie Moda e Magia', 24)")
db.execute("INSERT INTO livro(titulo, pagTotais) VALUES ('O Alquimista', 150)")


db.execute("INSERT INTO usuario(login, senha, primeiroNome) VALUES ('user1', 'pass1', 'Luan')")
db.execute("INSERT INTO usuario(login, senha, primeiroNome) VALUES ('user2', 'barbie123', 'Rony')")
db.execute("INSERT INTO usuario(login, senha, primeiroNome) VALUES ('user3', 'pass3', 'Erick')")


db.execute("INSERT INTO paginaAnotadas(numPagina, idUsuario, idLivro, anotacao) VALUES (10, 1, 1, 'Anotação na página 10')")
db.execute("INSERT INTO paginaAnotadas(numPagina, idUsuario, idLivro, anotacao) VALUES (50, 2, 1, 'Anotação na página 50')")
db.execute("INSERT INTO paginaAnotadas(numPagina, idUsuario, idLivro, anotacao) VALUES (20, 3, 2, 'Anotação na página 20')")

db.execute("INSERT INTO usuarioLivro(idUsuario, idLivro) VALUES (1, 1)")
db.execute("INSERT INTO usuarioLivro(idUsuario, idLivro) VALUES (1, 3)")
db.execute("INSERT INTO usuarioLivro(idUsuario, idLivro) VALUES (2, 2)")

#testando como armazenar pdf/jpeg em string de bytes
pdf_path = r'C:\Users\micha\Desktop\Project\Pyndle\Pyndle.pdf'

with open(pdf_path, 'rb') as pdf_file:
    pdf_data = pdf_file.read()

#exemplo de como usar variáveis nos comandos SQL
db.execute('UPDATE livro SET arquivoPdf = (?) WHERE idLivro = 3', (pdf_data,))

jpeg_path = r'C:\Users\micha\Desktop\Project\Pyndle\test.jpg'

with open(jpeg_path, 'rb') as jpeg_file:
    jpeg_data = jpeg_file.read()

db.execute('UPDATE livro SET capaLivro = (?) WHERE idLivro = 3', (jpeg_data,))

db.execute('SELECT * FROM livro WHERE idLivro = 3')

#isso aqui basicamente vai nos permitir pegar input das tabelas em forma de lista e conseguir tratar no back e usar no front
#a = db.fetchall()
#print(a)

# Dando commit e fechando a conexão com o SQLite3
connection.commit()
connection.close()
