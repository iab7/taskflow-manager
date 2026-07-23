# 📋 TaskFlow Manager

Sistema de gerenciamento de tarefas desenvolvido em Python utilizando o conceito de CRUD (Create, Read, Update e Delete), persistência de dados em JSON, testes automatizados com PyTest e integração contínua utilizando GitHub Actions.

---

## 📖 Sobre o Projeto

O **TaskFlow Manager** é uma aplicação de linha de comando (CLI) que permite ao usuário organizar sua rotina por meio do cadastro e gerenciamento de tarefas.

O projeto foi desenvolvido como atividade acadêmica com foco na aplicação de conceitos de programação, versionamento com Git/GitHub e integração contínua.

---

## 🚀 Funcionalidades

- ✅ Criar tarefas
- ✅ Listar tarefas
- ✅ Editar tarefas
- ✅ Excluir tarefas
- ✅ Concluir tarefas
- ✅ Buscar tarefas
- ✅ Dashboard com estatísticas
- ✅ Persistência de dados em arquivo JSON
- ✅ Validação de dados
- ✅ Tratamento de erros
- ✅ Testes automatizados
- ✅ GitHub Actions

---

## 📂 Estrutura do Projeto

```
TaskFlow/
│
├── app.py
├── crud.py
├── dashboard.py
├── menu.py
├── models.py
├── storage.py
├── requirements.txt
│
├── data/
│   └── tarefas.json
│
├── tests/
│   ├── test_crud.py
│   ├── test_dashboard.py
│   └── test_storage.py
│
└── .github/
    └── workflows/
        └── python-tests.yml
```

---

## 🛠 Tecnologias Utilizadas

- Python 3
- JSON
- PyTest
- Git
- GitHub
- GitHub Actions

---

## ▶ Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/iab7/taskflow-manager.git
```

### 2. Entrar na pasta

```bash
cd taskflow-manager
```

### 3. Criar ambiente virtual

Windows

```bash
python -m venv .venv
```

Linux/Mac

```bash
python3 -m venv .venv
```

### 4. Ativar ambiente virtual

Windows

```bash
.venv\Scripts\activate
```

Linux/Mac

```bash
source .venv/bin/activate
```

### 5. Instalar dependências

```bash
pip install -r requirements.txt
```

### 6. Executar o sistema

```bash
python app.py
```

---

## 🧪 Executando os Testes

Para executar todos os testes automatizados:

```bash
python -m pytest
```

Saída esperada:

```
3 passed
```

---

## 🔄 Integração Contínua

O projeto utiliza **GitHub Actions** para executar automaticamente os testes sempre que um novo commit é enviado ao repositório.

Workflow:

- Instala o Python
- Instala as dependências
- Executa o PyTest
- Informa se os testes passaram ou falharam

---

## 📌 Funcionalidades Implementadas

- CRUD completo
- Persistência em JSON
- Busca de tarefas
- Dashboard
- Validação de entradas
- Tratamento de exceções
- Testes automatizados
- Integração Contínua

---

## 📚 Conceitos Aplicados

- Programação Orientada a Objetos
- Modularização
- Persistência de Dados
- CRUD
- Versionamento com Git
- GitHub
- GitHub Actions
- Testes Automatizados
- Boas práticas de programação

---
Diagrama de Casos de Uso:
          Usuário

             |

 ------------------------------------
| Criar tarefa                       |
| Listar tarefas                     |
| Editar tarefa                      |
| Excluir tarefa                     |
| Concluir tarefa                    |
| Buscar tarefa                      |
| Visualizar dashboard               |
 ------------------------------------
---
## 👨‍💻 Autor

Desenvolvido por **Isaque Abreu** como atividade acadêmica.

GitHub:
https://github.com/iab7

---

## 📄 Licença

Este projeto possui finalidade exclusivamente educacional.
