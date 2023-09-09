import sqlite3

conexao = sqlite3.connect("src/model/Pyndle.db")
sgbd = conexao.cursor()


def checar(nomeUsuario: str, senha: str):
    """
    Função para checar se o usuário existe no banco de dados
    :param str nomeUsuario: Login que deseja verificar
    :param str senha: Senha do usuário que deseja verificar
    :return bool: retorna False, caso não exista, ou True, caso exista
    """
    quantidadeUsuario = sgbd.execute(
        "SELECT login, senha FROM usuarios WHERE login = ?", (nomeUsuario,)
    )
    usuarioBD = quantidadeUsuario.fetchone()[0]
    if usuarioBD != None and nomeUsuario == usuarioBD:
        return True
    else:
        return False


def getTuplaUsuario(nomeUsuario: str):
    """
    Função que retorna uma tupla com todas as informações do usuário a partir de seu login
    :param str nomeUsuario: login do usuário sobre o qual deseja obter informações
    :return : Retorna uma **tupla** com as informações do usuário caso exista, senão retorna **None**
    """
    queryInfUsuario = sgbd.execute(
        "SELECT * FROM usuarios WHERE login = ?", (nomeUsuario,)
    )
    InfUsuario = queryInfUsuario.fetchone()
    if InfUsuario:
        return InfUsuario
    else:
        return None


def registrarUsuario(nomeUsuario: str, senha: str):
    """
    **Função para registrar o usuário**\n
    Primeiro checa se o usuário não existe para então registrar no banco de dados
    :param str nomeUsuario: nome do usuário que deseja registrar
    :param senha: senha do usuário que deseja registrar
    """
    if checar(nomeUsuario, senha) is False:
        sgbd.execute(
            """
        INSERT INTO usuarios(login, senha) VALUES (?, ?)
        """,
            (
                nomeUsuario.lower(),
                senha,
            ),
        )
        conexao.commit()  # Registrando no arquivo pyndle.db
        return True
    return False


def logarUsuario(nomeUsuario: str, senha: str):
    """
    **Função para logar usuário**
    Verifica se o usuário existe e, caso afirmativo, verificar se a senha corresponde ao usuário recebido
    :param str nomeUsuario: Login do usuário que deseja logar
    :param str senha: Senha do usuário que deseja logar
    :return bool: Retorna verdadeira, caso a senha correspondam, ou falso, caso o usuário não exista ou a senha não corresponda
    """
    if checar(nomeUsuario, senha):
        sgbd.execute(
            """
        SELECT senha FROM usuarios
        WHERE login = (?)
        """,
            (nomeUsuario,),
        )

        resultadoSenha = (
            sgbd.fetchone()
        )  # O fetchall retorna uma lista com tuplas dos registros

        if len(senha) != 0 and resultadoSenha[0] == senha:
            return True
        else:
            return False
    else:
        return False
