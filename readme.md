
# 🔐 Mini Framework de Autenticação (WIP)

> **Status:** Em desenvolvimento (Versão 0.1)
> **Autor:** Gabriel Rodrigues
> **Data de Início:** 15/08/2025
> **Licença:** MIT (a ser adicionada)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![Licença](https://img.shields.io/badge/Licença-MIT-green)
![Versão](https://img.shields.io/badge/Versão-0.1-orange)

---

## 📑 Sumário

* [Descrição](#-descrição)
* [Objetivos](#-objetivos)
* [Funcionalidades](#-funcionalidades)

  * [Implementadas](#-implementadas)
  * [Planejadas](#-planejadas)
* [Estrutura do Projeto](#️-estrutura-do-projeto)

  * [Estrutura de Dados](#-estrutura-de-dados)
  * [Funções Principais](#-funções-principais)
* [Como Executar](#-como-executar)
* [Como Usar](#-como-usar)
* [Limitações Atuais](#️-limitações-atuais)
* [Contribuição](#-contribuição)
* [Licença](#-licença)
* [Contato](#-contato)

---

## 📖 Descrição

O **Mini Framework de Autenticação** é um módulo Python criado para ser integrado em outros sistemas que necessitem de **validação de usuários**. Ele foi desenvolvido com foco em **simplicidade, reuso e boas práticas**, seguindo as recomendações da **PEP 8** e **PEP 257**.

Atualmente, ele funciona no console, mas possui roadmap para suportar persistência em arquivos e até interface gráfica.

🚧 **Aviso:** este repositório está em desenvolvimento. A estrutura e documentação serão refinadas em commits futuros.

---

## 🎯 Objetivos

* Criar uma base modular para sistemas que precisem de autenticação.
* Garantir separação entre **lógica de autenticação** e **lógica de negócio**.
* Permitir expansão para diferentes cenários (sistemas financeiros, jogos, cadastros etc.).
* Servir como projeto de aprendizado para boas práticas em Python.

---

## ✨ Funcionalidades

### ✅ Implementadas

* 🔐 **Login de Usuário** — valida se o usuário existe antes de solicitar senha.
* 🔄 **Limite de tentativas** — máximo configurável (padrão: 3).
* 📝 **Docstrings padronizadas** — documentação seguindo **PEP 257**.
* 🧩 **Integração modular** — pode ser chamado de qualquer outro script Python.

### 🔜 Planejadas

* 💾 **Persistência de dados** — suporte a arquivos JSON.
* 🔒 **Segurança avançada** — hashing de senhas.
* 👥 **Gestão de perfis** — diferentes níveis de acesso (admin, usuário).
* 🖼️ **Interface gráfica** — integração futura com Tkinter.
* 🧪 **Testes automatizados** — uso de `pytest`.

---

## 🗂️ Estrutura do Projeto

```
mini_auth/
│
├── login.py         # Módulo principal de autenticação
├── main.py          # Exemplo de uso (script executável)
└── README.md        # Documentação
```

### Estrutura de Dados

Usuários são armazenados em **dicionário Python**:

```python
usuarios = {
    "gabriel": {"senha": "1234"},
    "admin": {"senha": "admin"}
}
```

### Funções Principais

* **`solicitar_usuario(banco_usuarios)`** → valida se o usuário existe.
* **`solicitar_senha(usuario, banco_usuarios, max_tentativas=3)`** → gerencia tentativas de senha.
* **`autenticar(banco_usuarios)`** → executa o fluxo completo de login.

---

## 🚀 Como Executar

### Pré-requisitos

* Python **3.8+** instalado.
* Nenhuma dependência externa necessária.

### Passos

```bash
# 1. Clone o repositório
git clone https://github.com/gabrielhastec/mini-framework-auth.git

# 2. Entre no diretório
cd mini-framework-auth

# 3. Execute o exemplo
python main.py
```

---

## 📌 Como Usar

Exemplo básico:

```python
import login

def sistema_principal():
    print("Acesso liberado ao sistema principal!")

usuarios = {
    "gabriel": {"senha": "1234"},
    "teste": {"senha": "abcd"}
}

login.inicializar_sistema(usuarios, sistema_principal)
```

---

## ⚠️ Limitações Atuais

* Usuários em memória (sem banco de dados).
* Senhas não criptografadas.
* Apenas interface via console.
* Sem testes automatizados ainda.

---

## 🤝 Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature:

   ```bash
   git checkout -b feature/nova-funcionalidade
   ```
3. Faça commits pequenos e descritivos:

   ```bash
   git commit -m "Adiciona verificação de senha forte"
   ```
4. Envie sua branch:

   ```bash
   git push origin feature/nova-funcionalidade
   ```
5. Abra um Pull Request.

---

## 📜 Licença

Distribuído sob a licença **MIT**.
Arquivo `LICENSE` será adicionado futuramente.

---

## 📧 Contato

* **Autor:** Gabriel Rodrigues
* **E-mail:** [gabrielhastec.dev@gmail.com](mailto:gabrielhastec.dev@gmail.com)
* **GitHub:** [gabrielhastec](https://github.com/gabrielhastec)
* **Localização:** Recife-PE

⭐ Obrigado por conferir o **Mini Framework de Autenticação**!
