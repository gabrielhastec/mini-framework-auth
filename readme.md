
# 🔐 Mini Framework de Autenticação (WIP)

> **Status:** Em desenvolvimento (Versão 0.1)
> **Autor:** Gabriel Rodrigues
> **Data de Início:** 15/08/2025
> **Licença:** MIT (a ser adicionada)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![Versão](https://img.shields.io/badge/Versão-0.1-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📑 Sumário

* [Descrição](#-descrição)
* [Objetivos](#-objetivos)
* [Funcionalidades](#-funcionalidades)

  * [Implementadas](#-implementadas)
  * [Planejadas](#-planejadas)
* [Roadmap de Versões](#-roadmap-de-versões)
* [Estrutura do Projeto](#️-estrutura-do-projeto)

  * [Estrutura de Dados](#-estrutura-de-dados)
  * [Funções Principais](#-funções-principais)
* [Como Executar](#-como-executar)
* [Como Usar](#-como-usar)
* [Pré-requisitos](#-pré-requisitos)
* [Limitações Atuais](#️-limitações-atuais)
* [Contribuição](#-contribuição)
* [Licença](#-licença)
* [Contato](#-contato)

---

## 📖 Descrição

O **Mini Framework de Autenticação** é um pacote Python modular que permite integrar **autenticação de usuários** em outros sistemas com facilidade.

O pacote prioriza:

* **Modularidade** — cada funcionalidade em arquivos separados (`autenticar.py`, `exceptions.py`, `utils.py`).
* **Boas práticas** — PEP 8, PEP 257 e docstrings detalhadas.
* **Reuso e escalabilidade** — fácil integração em projetos pequenos ou grandes.

🚧 **Aviso:** O projeto está em desenvolvimento; novas versões trarão funcionalidades adicionais.

---

## 🎯 Objetivos

* Criar uma base sólida para autenticação modular em Python.
* Separar **lógica de autenticação** da **lógica do sistema principal**.
* Permitir futuras integrações com banco de dados, interface gráfica e segurança avançada.
* Servir como projeto educacional e de referência para boas práticas em Python.

---

## ✨ Funcionalidades

### ✅ Implementadas

* Login de usuário com verificação prévia da existência.
* Limite de tentativas configurável (padrão: 3).
* Exceções customizadas (`UsuarioNaoEncontrado`, `TentativasExcedidas`).
* Funções auxiliares em `utils.py`.
* Docstrings e documentação seguindo PEP 257.

### 🔜 Planejadas

* Persistência de dados em arquivos JSON.
* Criptografia de senhas e validação de força.
* Gestão de perfis e níveis de acesso (admin, usuário).
* Interface gráfica com Tkinter ou similar.
* Testes automatizados com `pytest`.
* Pacote instalável via PyPI.

---

## 🗺️ Roadmap de Versões

| Versão | Status             | Novidades                                                         |
| ------ | ------------------ | ----------------------------------------------------------------- |
| 0.1    | Em desenvolvimento | Estrutura inicial, login básico, docstrings, utils e exceptions   |
| 0.2    | Planejado          | Adição de persistência JSON, testes unitários, hashing de senhas  |
| 0.3    | Planejado          | Gestão de perfis, interface gráfica simples, logging de eventos   |
| 1.0    | Futuro             | Primeira versão estável, pronta para integração em sistemas reais |

---

## 🗂️ Estrutura do Projeto

```
mini_auth/
│
├── login/
│   ├── __init__.py        # Pacote do módulo
│   ├── autenticar.py      # Funções principais de login
│   ├── exceptions.py      # Exceções customizadas
│   └── utils.py           # Funções auxiliares
│
├── examples/
│   └── main.py            # Exemplo executável
├── tests/
│   └── test_autenticar.py # Testes unitários com pytest
├── setup.py               # Configuração para instalação do pacote
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação
```

### Estrutura de Dados

```python
usuarios = {
    "gabriel": {"senha": "1234"},
    "teste": {"senha": "abcd"}
}
```

### Funções Principais

* `solicitar_usuario(banco_usuarios)` → valida usuário.
* `solicitar_senha(usuario, banco_usuarios, max_tentativas=3)` → gerencia tentativas de senha.
* `autenticar(banco_usuarios)` → fluxo completo de login.
* `inicializar_sistema(banco_usuarios, funcao_principal)` → executa função principal após login.
* `utils.mensagem_boas_vindas(usuario)` → exibe mensagem de boas-vindas.
* Exceções customizadas em `exceptions.py`.

---

## 🚀 Como Executar

```bash
# Clone o repositório
git clone https://github.com/gabrielhastec/mini-framework-auth.git
cd mini-framework-auth

# Execute exemplo
python examples/main.py
```

---

## 📌 Como Usar

```python
from login import inicializar_sistema

def sistema_principal():
    print("Acesso liberado!")

usuarios = {
    "gabriel": {"senha": "1234"},
    "teste": {"senha": "abcd"}
}

inicializar_sistema(usuarios, sistema_principal)
```

---

## 📋 Pré-requisitos

* Python 3.8+
* Dependências futuras listadas no `requirements.txt`

---

## ⚠️ Limitações Atuais

* Usuários em memória (sem banco de dados).
* Senhas não criptografadas.
* Apenas interface via console.
* Testes limitados.

---

## 🤝 Contribuição

1. Faça um **fork**.
2. Crie uma branch:

```bash
git checkout -b feature/nova-funcionalidade
```

3. Faça commits pequenos e descritivos.
4. Envie sua branch e abra um Pull Request.

---

## 📜 Licença

Projeto educacional. Licença MIT planejada.
Código pode ser estudado e adaptado, mas não usar em produção sem autorização.

---

## 📧 Contato

* **Autor:** Gabriel Rodrigues
* **E-mail:** [gabrielhastec.dev@gmail.com](mailto:gabrielhastec.dev@gmail.com)
* **GitHub:** [gabrielhastec](https://github.com/gabrielhastec)
* **Localização:** Recife-PE

⭐ Obrigado por conferir o **Mini Framework de Autenticação**!
