import sqlite3

conexao = sqlite3.connect("src/model/Pyndle.db")
sgbd = conexao.cursor()


def checar(nomeUsuario: str, senha: str = None):
    """
    Função para checar se o usuário existe no banco de dados\n
    Caso não seja passada uma senha, apenas verifica se existe um usuário com aquele nome
    :param str nomeUsuario: Login que deseja verificar
    :param str senha: Senha do usuário que deseja verificar
    :return bool: retorna False, caso não exista, ou True, caso exista
    """
    if senha is None:
        quantidadeUsuario = sgbd.execute(
            """
        SELECT login FROM usuarios 
        WHERE login = ?
        """,
            (nomeUsuario,),
        )

        resultado = quantidadeUsuario.fetchone()

        if resultado:
            return True
        else:
            return False

    else:
        quantidadeUsuario = sgbd.execute(
            """
        SELECT login, senha FROM usuarios 
        WHERE login = ? AND senha = ?
        """,
            (nomeUsuario, senha),
        )

        resultado = quantidadeUsuario.fetchone()

        if resultado:
            return True
        else:
            return False


def dadosUsuario(nomeUsuario: str):
    """
    Função que retorna todos os dados do usuário em um dicionário, a partir de seu ID
    :param nomeUsuario: Id do usuário que deseja acessar os dados
    :return: Retorna um **dicionário** com os dados, caso o usuário exista, senão retorna **None**
    """
    sgbd.execute("SELECT * FROM usuarios WHERE login = ?", (nomeUsuario,))
    dados = sgbd.fetchone()

    if dados:
        # Obtém os nomes das colunas da tabela
        colunas = [desc[0] for desc in sgbd.description]

        # Cria um dicionário com coluna: valor
        dados_dict = dict(zip(colunas, dados))

        return dados_dict
    else:
        return None


def registrarUsuario(nomeUsuario: str, senha: str, fotoPerfil: bytes):
    """
    **Função para registrar o usuário**\n
    Primeiro checa se o usuário não existe para então registrar no banco de dados
    :param str nomeUsuario: nome do usuário que deseja registrar
    :param senha: senha do usuário que deseja registrar
    :param fotoPerfil: foto de perfil do usuário em bytes
    """
    if checar(nomeUsuario) is False:
        sgbd.execute(
            """
        INSERT INTO usuarios(login, senha, fotoPerfil) 
        VALUES (?, ?, ?)
        """,
            (
                nomeUsuario,
                senha,
                fotoPerfil,
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
