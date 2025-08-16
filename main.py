"""
Arquivo de teste para o módulo login.py.

Este script simula um pequeno banco de usuários e
executa o processo de autenticação utilizando o
mini framework de login.

Pode ser usado para validar o funcionamento
antes de integrar em um sistema real.
"""

import login  # Importa o módulo de autenticação

def sistema_principal():
    """
    Função que representa o sistema a ser executado
    após o login bem-sucedido.
    """
    print("\n--- SISTEMA PRINCIPAL ---")
    print("Você agora tem acesso às funcionalidades do sistema!")
    print("-------------------------\n")

if __name__ == "__main__":
    # Banco de usuários simulado para teste
    usuarios_teste = {
        "gabriel": {"senha": "1234"},
        "teste": {"senha": "abcd"}
    }

    print("=== TESTE DE LOGIN ===")
    sucesso = login.inicializar_sistema(usuarios_teste, sistema_principal)

    if sucesso:
        print("✅ Teste concluído: Login realizado com sucesso.")
    else:
        print("❌ Teste concluído: Falha na autenticação.")
