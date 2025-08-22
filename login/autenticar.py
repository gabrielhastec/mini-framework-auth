"""
Módulo principal de autenticação.

Funções:
- solicitar_usuario
- solicitar_senha
- autenticar
- inicializar_sistema
"""

def solicitar_usuario(banco_usuarios):
    """Solicita o nome de usuário até que um usuário válido seja informado."""
    while True:
        usuario = input("Usuário: ")
        if usuario in banco_usuarios:
            return usuario
        print("Usuário não encontrado. Tente novamente.")

def solicitar_senha(usuario, banco_usuarios, max_tentativas=3):
    """Solicita a senha do usuário com limite de tentativas."""
    for tentativa in range(1, max_tentativas + 1):
        senha = input("Senha: ")
        if senha == banco_usuarios[usuario]["senha"]:
            print(f"Login efetuado. Bem-vindo '{usuario}'.")
            return True
        print(f"Senha incorreta! Tentativa {tentativa}/{max_tentativas}")
    print("Número máximo de tentativas excedido.")
    return False

def autenticar(banco_usuarios):
    """
    Executa o processo completo de login.
    Retorna o nome do usuário autenticado ou None.
    """
    usuario = solicitar_usuario(banco_usuarios)
    if solicitar_senha(usuario, banco_usuarios):
        return usuario
    return None

def inicializar_sistema(banco_usuarios, funcao_principal):
    """
    Inicializa o sistema: solicita login e executa a função principal
    apenas se a autenticação for bem-sucedida.
    """
    usuario = autenticar(banco_usuarios)
    if usuario:
        funcao_principal()
        return True
    return False
