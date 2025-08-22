"""
Módulo principal de autenticação.

Funções:
- autenticar
- inicializar_sistema
"""

from login.exceptions import UsuarioNaoEncontrado, TentativasExcedidas
from login.utils import mensagem_boas_vindas


def autenticar(verificar_usuario, verificar_senha, max_tentativas=3):
    """
    Função principal de autenticação. Verifica se o usuário existe e se a senha está correta.
    
    Args:
        verificar_usuario (Callable[[str], bool]): Função que retorna True se o usuário existe.
        verificar_senha (Callable[[str, str], bool]): Função que retorna True se a senha está correta.
        max_tentativas (int, opcional): Número máximo de tentativas de senha. Padrão é 3.
    
    Returns:
        str: Nome do usuário autenticado.
    
    Raises:
        UsuarioNaoEncontrado: Quando o usuário não existe.
        TentativasExcedidas: Quando o usuário excede o número máximo de tentativas.
    """
    usuario = input("Usuário: ")
    if not verificar_usuario(usuario):
        raise UsuarioNaoEncontrado(f"Usuário '{usuario}' não encontrado.")

    for tentativa in range(1, max_tentativas + 1):
        senha = input("Senha: ")
        if verificar_senha(usuario, senha):
            mensagem_boas_vindas(usuario)
            return usuario
        print(f"Senha incorreta! Tentativa {tentativa}/{max_tentativas}.")
    
    raise TentativasExcedidas(f"Número máximo de tentativas ({max_tentativas}) excedido para '{usuario}'.")

def inicializar_sistema(verificar_usuario, verificar_senha, func_sistema_principal, max_tentativas=3):
    """
    Inicializa o sistema principal após login bem-sucedido.

    Args:
        verificar_usuario (Callable[[str], bool]): Função que retorna True se o usuário existe.
        verificar_senha (Callable[[str, str], bool]): Função que retorna True se a senha está correta.
        func_sistema_principal (Callable[[], None]): Função que representa o sistema principal a ser executado.
        max_tentativas (int, opcional): Número máximo de tentativas de senha.
    """
    try:
        usuario = autenticar(verificar_usuario, verificar_senha, max_tentativas)
        func_sistema_principal(usuario)
    except UsuarioNaoEncontrado as e:
        print(e)
    except TentativasExcedidas as e:
        print(e)