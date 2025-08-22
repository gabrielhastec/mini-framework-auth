import pytest
from login.autenticar import autenticar, inicializar_sistema
from login.exceptions import UsuarioNaoEncontrado, TentativasExcedidas

# Funções externas simuladas
def mock_verificar_usuario(usuario):
    return usuario in ["gabriel", "admin"]

def mock_verificar_senha(usuario, senha):
    senhas = {"gabriel": "1234", "admin": "admin"}
    return senhas.get(usuario) == senha

# Teste usuário existente
def test_usuario_existente(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "gabriel")
    usuario = autenticar(mock_verificar_usuario, lambda u, s: True)
    assert usuario == "gabriel"

# Teste usuário não existente
def test_usuario_nao_existente(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "invalido")
    with pytest.raises(UsuarioNaoEncontrado):
        autenticar(mock_verificar_usuario, mock_verificar_senha)

# Teste senha correta
def test_senha_correta(monkeypatch):
    inputs = iter(["gabriel", "1234"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    usuario = autenticar(mock_verificar_usuario, mock_verificar_senha)
    assert usuario == "gabriel"

# Teste senha incorreta
def test_senha_incorreta(monkeypatch):
    inputs = iter(["gabriel", "0000", "1111", "2222"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(TentativasExcedidas):
        autenticar(mock_verificar_usuario, mock_verificar_senha, max_tentativas=3)

# Teste inicializar sistema
def test_inicializar_sistema(monkeypatch):
    inputs = iter(["gabriel", "1234"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    chamado = {}

    def sistema(usuario):
        chamado["usuario"] = usuario

    inicializar_sistema(mock_verificar_usuario, mock_verificar_senha, sistema)
    assert chamado["usuario"] == "gabriel"
