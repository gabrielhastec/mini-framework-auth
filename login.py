"""
Mini framework de autenticação para sistemas Python.

Permite autenticar usuários com base em um banco de dados fornecido,
com verificação de existência do usuário e validação de senha com limite de tentativas.
Inclui funções para solicitar credenciais, executar o processo de login
e inicializar o sistema somente após autenticação bem-sucedida.
"""

def solicitar_usuario(banco_usuarios):
    """
    Solicita o nome de usuário até que um usuário válido seja informado.

    Args:
        banco_usuarios (dict): Dicionário com nomes de usuários como chaves.

    Returns:
        str: Nome do usuário válido encontrado no banco.

    Exemplo:
        >>> usuarios = {"gabriel": {"senha": "1234"}}
        >>> solicitar_usuario(usuarios)
        Usuário: gabriel
        'gabriel'
    """
    while True:
        usuario = input("Usuário: ")
        if usuario in banco_usuarios:
            return usuario
        print("Usuário não encontrado. Tente novamente.")


def solicitar_senha(usuario, banco_usuarios, max_tentativas=3):
    """
    Solicita a senha do usuário com limite de tentativas.

    Args:
        usuario (str): Nome do usuário a ser autenticado.
        banco_usuarios (dict): Dicionário no formato {usuario: {"senha": str}}.
        max_tentativas (int, opcional): Número máximo de tentativas permitidas.

    Returns:
        bool: True se a senha estiver correta, False caso contrário.

    Exemplo:
        >>> usuarios = {"gabriel": {"senha": "1234"}}
        >>> solicitar_senha("gabriel", usuarios)
        Senha: 1234
        Login efetuado. Seja Bem-vindo 'gabriel'.
        True
    """
    for tentativa in range(1, max_tentativas + 1):
        senha = input("Senha: ")
        if senha == banco_usuarios[usuario]["senha"]:
            print(f"Login efetuado. Seja bem-vindo '{usuario}'.")
            return True
        print(f"Senha incorreta! Tentativa {tentativa}/{max_tentativas}.")
    print("Número máximo de tentativas excedido.")
    return False


def autenticar(banco_usuarios):
    """
    Executa o processo completo de autenticação.

    Primeiro solicita o nome de usuário e, se válido, solicita a senha.
    Retorna o nome do usuário autenticado em caso de sucesso.

    Args:
        banco_usuarios (dict): Dicionário no formato {usuario: {"senha": str}}.

    Returns:
        str | None: Nome do usuário autenticado ou None se falhar.

    Exemplo:
        >>> usuarios = {"gabriel": {"senha": "1234"}}
        >>> autenticar(usuarios)
        Usuário: gabriel
        Senha: 1234
        'gabriel'
    """
    usuario = solicitar_usuario(banco_usuarios)
    if solicitar_senha(usuario, banco_usuarios):
        return usuario
    return None


def inicializar_sistema(banco_usuarios, funcao_sistema, *args, **kwargs):
    """
    Inicializa o sistema apenas após autenticação bem-sucedida.

    Args:
        banco_usuarios (dict): Dicionário no formato {usuario: {"senha": str}}.
        funcao_sistema (callable): Função principal do sistema a ser executada.
        *args: Argumentos posicionais para passar à função do sistema.
        **kwargs: Argumentos nomeados para passar à função do sistema.

    Returns:
        bool: True se o sistema foi inicializado, False caso contrário.

    Exemplo:
        >>> def sistema():
        ...     print("Sistema iniciado!")
        >>> usuarios = {"gabriel": {"senha": "1234"}}
        >>> inicializar_sistema(usuarios, sistema)
        Usuário: gabriel
        Senha: 1234
        Login efetuado. Seja bem-vindo 'gabriel'.
        Sistema iniciado!
        True
    """
    
    usuario = autenticar(banco_usuarios)
    if usuario:
        funcao_sistema(*args, **kwargs)
        return True
    else:
        print("Acesso negado.")
        return False
