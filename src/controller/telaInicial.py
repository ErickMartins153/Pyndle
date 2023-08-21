import sqlite3

conexao = sqlite3.connect("src/model/Pyndle.db")
sgbd = conexao.cursor()

def checar(nomeUsuario, senha): #Essa função checa todas as restrições de nome de usuario que a gente decidir botar
    quantidadeUsuario = sgbd.execute("SELECT COUNT(login) FROM usuarios WHERE login = ?", (nomeUsuario,))
    count = quantidadeUsuario.fetchone()[0]
    if((quantidadeUsuario == 0) and (len(nomeUsuario > 0)) and (len(senha > 0))):
        return True
    else:
        return False

def registrarUsuario(nomeUsuario: str, senha: str):
    if checar(nomeUsuario, senha):
        sgbd.execute("""
            INSERT INTO usuarios(login, senha) VALUES (?, ?)
            """, (nomeUsuario, senha,))
        conexao.commit()  # Registrando no arquivo pyndle.db
        return True
    else:
        return False
    
def logarUsuario(nomeUsuario: str, senha: str):
    quantidadeUsuario = sgbd.execute("SELECT COUNT(login) FROM usuarios WHERE login = ?", (nomeUsuario,))
    count = quantidadeUsuario.fetchone()[0] #essa variavel tá basicamente perguntando se o nomeUsuario tá cadastrado no sistema, pq se não tiver, já avisa que o login foi digitado errado ou que você não foi cadastrado ainda

    if(count > 0):
        sgbd.execute("""
        SELECT senha FROM usuarios
        WHERE login = (?)
        """, (nomeUsuario,))

        resultado = sgbd.fetchall()  # O fetchall retorna uma lista com tuplas dos registros

        if (len(senha) != 0) and (resultado[0][0] == senha):
            return True
        else:
            return False
    else:
        return False

# Esse código foi pra testar se a função cadastrar tava funcionando
#nomeUsuario = input("Cadastre seu login: ")
#senha = input("Cadastre sua senha: ")
#if registrarUsuario(nomeUsuario, senha):
#    print("Usuário registrado com sucesso!")
#else:
#    print("Por favor, insira um login e senha válidos.")

#Código pra testar se a funcionalidade de login tá funcionando
#nomeUsuario = input("Login pra logar:")
#senha = input("Senha pra logar:")
#print(logarUsuario(nomeUsuario, senha))
