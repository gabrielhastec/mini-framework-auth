"""
Funções auxiliares para o pacote mini_auth
"""

def mensagem_boas_vindas(usuario: str) -> None:
    """
    Mostra mensagem de boas-vindas após login bem-sucedido.

    Args:
        usuario (str): Nome do usuário autenticado.
    """
    print(f"Login efetuado. Seja bem-vindo(a), {usuario}!")
    