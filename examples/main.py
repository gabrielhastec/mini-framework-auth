"""
Exemplo de execução do pacote mini_auth.
"""
from login import autenticar

# Funções simulando verificação em sistema externo
def verificar_usuario_externo(usuario):
    usuarios = ["gabriel", "admin", "teste"]
    return usuario in usuarios

def verificar_senha_externa(usuario, senha):
    banco_senhas = {"gabriel": "1234", "admin": "admin", "teste": "abcd"}
    return banco_senhas.get(usuario) == senha

# Função que representa o sistema principal
def sistema_principal(usuario):
    print(f"Acesso liberado ao sistema para {usuario}!")

# Inicializa autenticação
autenticar.inicializar_sistema(verificar_usuario_externo, verificar_senha_externa, sistema_principal)
