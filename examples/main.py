"""
Exemplo de execução do pacote mini_auth.
"""
from login import inicializar_sistema

def sistema_principal():
    print("Acesso liberado ao sistema!")

usuarios_teste = {
    "gabriel": {"senha": "1234"},
    "teste": {"senha": "abcd"}
}

if __name__ == "__main__":
    inicializar_sistema(usuarios_teste, sistema_principal)
