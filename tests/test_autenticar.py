import pytest
from login.autenticar import autenticar, solicitar_usuario, solicitar_senha

# Como o input() é usado, podemos simular entradas com monkeypatch do pytest
def test_usuario_existente(monkeypatch):
    banco = {"gabriel": {"senha": "1234"}}
    monkeypatch.setattr('builtins.input', lambda _: "gabriel")
    usuario = solicitar_usuario(banco)
    assert usuario == "gabriel"

def test_senha_correta(monkeypatch):
    banco = {"gabriel": {"senha": "1234"}}
    monkeypatch.setattr('builtins.input', lambda _: "1234")
    assert solicitar_senha("gabriel", banco) is True
