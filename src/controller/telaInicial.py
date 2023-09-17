import sqlite3

# Definindo conexão com o banco de dados
conexao = sqlite3.connect("src/model/Pyndle.db")
# Definindo cursor para gerenciar o banco de dados
sgbd = conexao.cursor()


def checar(nomeUsuario: str, senha: str = None):
    """
    Função para checar se o usuário existe no banco de dados\n
    Caso não seja passada uma senha, apenas verifica se existe um usuário com aquele nome
    :param str nomeUsuario: Login que deseja verificar
    :param str senha: Senha do usuário que deseja verificar
    :return bool: retorna False, caso não exista, ou True, caso exista
    """

    # Caso não seja informada a senha, apenas verifica se algum usuário com aquele login existe
    if senha is None:
        quantidadeUsuario = sgbd.execute("""
            SELECT login FROM usuarios 
            WHERE login = ?
        """, (nomeUsuario,))

        resultado = quantidadeUsuario.fetchone()

        if resultado:
            return True
        else:
            return False

    # Verifica se um usuário com aquele login e senha existe
    else:
        quantidadeUsuario = sgbd.execute("""
            SELECT login, senha FROM usuarios 
            WHERE login = ? AND senha = ?
        """, (nomeUsuario, senha))

        resultado = quantidadeUsuario.fetchone()

        if resultado:
            return True
        else:
            return False


def dadosUsuario(nomeUsuario: str) -> dict | None:
    """
    Função que retorna todos os dados do usuário em um dicionário, a partir do seu login
    :param nomeUsuario: Id do usuário que deseja acessar os dados
    :return: Retorna um **dicionário** com os dados, caso o usuário exista, senão retorna **None**
    """

    # Obtendo dados do pyndle.db
    sgbd.execute("""
        SELECT * FROM usuarios 
        WHERE login = ?
    """, (nomeUsuario,))

    dados = sgbd.fetchone()

    # Verifica se os dados existem
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
    :return: **True**: ao registrar || **False**: caso o usuário exista
    """

    # Define uma foto padrão caso o usuário não tenha definido
    if fotoPerfil == b'':
        with open('src/view/assets/icons/default_user.jpg', 'rb') as img_file:
            fotoPerfil = img_file.read()

    # Adiciona o usuário no banco de dados checando, caso não exista um com aquele login
    if checar(nomeUsuario) is False:
        sgbd.execute("""
            INSERT INTO usuarios(login, senha, fotoPerfil) 
            VALUES (?, ?, ?)
        """, (nomeUsuario, senha, fotoPerfil))

        conexao.commit()  # Registrando no arquivo pyndle.db

        return True
    return False


def logarUsuario(nomeUsuario: str, senha: str):
    """
    **Função para logar usuário**
    Verifica se o usuário existe e, caso afirmativo, verificar se a senha corresponde ao usuário recebido
    :param nomeUsuario: Login do usuário que deseja logar
    :param senha: Senha do usuário que deseja logar
    :return: **True**: caso a senha correspondam || **False**: caso o usuário não exista ou a senha não corresponda
    """

    # Coleta a senha daquele respectivo usuário no banco de dados
    if checar(nomeUsuario, senha):
        sgbd.execute("""
            SELECT senha FROM usuarios
            WHERE login = (?)
        """, (nomeUsuario,))

        resultadoSenha = (sgbd.fetchone())

        # Verifica se a senha inserida corresponde com a senha do usuário
        if len(senha) != 0 and resultadoSenha == senha:
            return True
        else:
            return False

    else:
        return False
