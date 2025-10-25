# Gerenciador de Tarefas com Python, SQL e Pandas (CRUD)

Uma aplicação de terminal completa para gerenciamento de tarefas pessoais, demonstrando a implementação de um sistema CRUD (Create, Read, Update, Delete) com persistência de dados em um banco SQLite.

Este projeto nasceu do meu foco em aprender os fundamentos do desenvolvimento Back-End e bancos de dados, colocando em prática os conceitos da minha graduação em Análise e Desenvolvimento de Sistemas (ADS).

O objetivo principal foi construir uma aplicação robusta do zero, indo além de um script simples. O desafio foi projetar e implementar a interação completa com um banco de dados SQL, gerenciar a "lógica de negócios" de forma limpa e garantir que a aplicação fosse segura contra entradas inválidas (Programação Defensiva).

O projeto evoluiu de um único menu monolítico para uma aplicação Orientada a Objetos, onde cada funcionalidade (adicionar, editar, etc.) foi refatorada em seu próprio método, seguindo o Princípio da Responsabilidade Única (SRP).

## Tecnologias e Conceitos Aplicados

* **Python 3**
* **SQL (SQLite):**
  * **DDL (Data Definition Language) :** `CREATE TABLE`, `PRIMARY KEY AUTOINCREMENT`, `NOT NULL`, `DEFAULT 0`.
  * **DML (Data Manipulation Language):** Implementação do ciclo CRUD completo (`INSERT`, `SELECT`, `UPDATE`, `DELETE`) com placeholders (`?`).
* **Pandas:** Utilizado para carregar (`read_sql_query`) e exibir os dados do `SELECT` de forma limpa e formatada no terminal.
* **Programação Orientada a Objetos (POO):** Toda a lógica de negócios e interação com o banco foi encapsulada na classe `Lista`.
* **Clean Code (SRP):** O código foi refatorado para que cada método tenha uma responsabilidade única (ex: `adicionar_tarefas()`, `apagar_tarefas()`).
* **Programação Defensiva:** Validação robusta de entrada do usuário com `try/except ValueError` e verificação de existência de ID (`SELECT`/`fetchone`) antes de operações de escrita.
* **Estrutura de Projeto Profissional:** O projeto utiliza um layout `src/`, ambiente virtual (`.venv`) e `.gitignore` para separar o código-fonte de dados sensíveis (`.env`) e do banco (`.db`).

## Como Rodar o Projeto

1. **Clone o repositório:**
   ```
   git clone [https://github.com/Silea-Dev/gerenciador_tarefas.git](https://github.com/Silea-Dev/gerenciador_tarefas.git)
   cd gerenciador_tarefas
   ```
2. **Crie e ative seu ambiente virtual:**
   ```
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # macOS / Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Instale as dependências:**
   (Este projeto requer `pandas` e `flask`, listados no `requirements.txt`)
   ```
   pip install -r requirements.txt
   ```
4. **Execute a aplicação de terminal:**
   O `main.py` é o ponto de entrada que iniciará o login e o menu.
   ```
   python main.py
   ```

## Referências

Acessar SQL: conceitos básicos, vocabulário e sintaxe. Disponível em [https://support.microsoft.com/pt-br/topic/acessar-sql-conceitos-b%C3%A1sicos-vocabul%C3%A1rio-e-sintaxe-444d0303-cde1-424e-9a74-e8dc3e460671](https://support.microsoft.com/pt-br/topic/acessar-sql-conceitos-b%C3%A1sicos-vocabul%C3%A1rio-e-sintaxe-444d0303-cde1-424e-9a74-e8dc3e460671). Acessado em 20/10/2025.
