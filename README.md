# 🔐 LoginCore

Sistema de autenticação de usuários desenvolvido em Python com cadastro, login, persistência de dados em JSON e estrutura modular.

---

## 🚀 Sobre o Projeto

O LoginCore é um projeto criado para praticar conceitos fundamentais de desenvolvimento em Python, simulando um sistema real de autenticação de usuários através do terminal.

O sistema permite cadastrar usuários, realizar login, validar credenciais e armazenar dados de forma persistente utilizando arquivos JSON.

---

## ✨ Funcionalidades

* ➕ Cadastro de usuários
* 🔑 Login com validação de credenciais
* 💾 Armazenamento de dados em JSON
* ❌ Impede usuários duplicados
* 🔒 Limite de 3 tentativas de login
* ⚠️ Validação de campos obrigatórios
* 📂 Organização modular do código
* 🖥️ Interface via terminal

---

## 📁 Estrutura do Projeto

```text
login_system/
│
├── main/
│   └── sistema_login.py
│
├── funcoes_system/
│   ├── __init__.py
│   ├── cadastro.py
│   ├── login.py
│   └── arquivo.py
│
├── dados/
│   └── login.json
│
└── README.md
```

---

## 🧠 Tecnologias Utilizadas

* Python 3
* JSON
* Dicionários (`dict`)
* Modularização
* Manipulação de arquivos
* Tratamento de exceções

---

## 📌 Fluxo do Sistema

```text
=== Sistema de Login ===

1. Cadastrar-se
2. Login
3. Sair
```

### Cadastro

* O usuário informa nome e senha.
* O sistema verifica se o nome já existe.
* Os dados são armazenados em arquivo JSON.

### Login

* O usuário informa nome e senha.
* O sistema valida as credenciais.
* São permitidas até 3 tentativas.

---

## ⚙️ Regras de Negócio

* O nome de usuário deve ser único.
* Nome e senha não podem ser vazios.
* O login possui limite de 3 tentativas.
* Os dados são persistidos em arquivo JSON.

---

## 🎯 Objetivos de Aprendizagem

Este projeto foi desenvolvido para praticar:

* Organização de projetos Python
* Estruturas de dados
* Modularização
* Manipulação de arquivos JSON
* Tratamento de exceções
* Lógica de autenticação
* Boas práticas de programação

---

## 📈 Próximas Melhorias

* 🔐 Criptografia de senhas com hashlib
* 🔄 Alteração de senha
* 🗑️ Exclusão de usuários
* 📊 Registro de tentativas de login
* 🌐 API com Flask
* 🗄️ Integração com banco de dados SQLite

---

## 👨‍💻 Autor

Desenvolvido por **Kauan Moraes** 🚀

Projeto criado com fins educacionais e para evolução das habilidades em Python.
