"""
Exceções customizadas para o pacote mini_auth
"""

class UsuarioNaoEncontrado(Exception):
    """Exceção disparada quando o usuário não existe no banco de dados."""
    pass

class TentativasExcedidas(Exception):
    """Exceção disparada quando o usuário excede o número de tentativas de senha."""
    pass
