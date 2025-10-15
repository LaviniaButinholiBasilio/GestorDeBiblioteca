# 📚 Sistema de Biblioteca (Python - Terminal)

![Feito com Python](https://img.shields.io/badge/feito%20com-Python-FFC0CB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-concluído-FFC0CB)
![Licença](https://img.shields.io/badge/licença-Livre-FFC0CB)
![Autoria](https://img.shields.io/badge/feito%20por-Lavínia%20Butinholi%20Basílio-FFC0CB)

---

## 📖 Descrição
Este projeto implementa um **Sistema de Biblioteca** em Python, totalmente jogável no terminal.  
O sistema permite:  
- Visualizar livros disponíveis  
- Visualizar empréstimos de um usuário logado  
- Consultar informações sobre o sistema  

O foco é a **gestão de empréstimos e livros** de forma simples, utilizando arquivos de texto (`usuarios.txt`, `livros.txt` e `emprestimos.txt`) para armazenar os dados.

---

## ⚙️ Funcionalidades
- 👤 Sistema de login de usuários (Clientes e Bibliotecários)  
- 📖 Listagem de livros disponíveis  
- 📅 Listagem de empréstimos de acordo com o usuário logado  
- ℹ️ Exibição de informações sobre o sistema  
- 💬 Interface simples via terminal  

---

## 🧠 Estrutura do Código
| Classe | Descrição |
|--------|------------|
| `Usuario` | Representa um usuário do sistema |
| `SistemaUsuarios` | Gerencia login e validação de usuários |
| `SistemaLivros` | Gerencia a listagem de livros disponíveis |
| `SistemaEmprestimos` | Gerencia a listagem de empréstimos por usuário |
| `SistemaBiblioteca` | Integra usuários, livros e empréstimos, e gerencia o menu principal |

---
--- Bem-vindo ao Sistema de Biblioteca ---
Informe o login: joao
Informe a senha: 12345
Bem-vindo, João!

--- Menu ---
1 - Visualizar Empréstimos
2 - Visualizar Livros
3 - Sobre
4 - Sair
Escolha uma opção: 2

--- Livros Disponíveis ---
Código: 1, Nome: Dom Quixote, Autor: Miguel de Cervantes
Código: 2, Nome: O Senhor dos Anéis, Autor: J.R.R. Tolkien
Código: 3, Nome: 1984, Autor: George Orwell


## 🪶 Licença

Este projeto é de **uso livre** para fins **educacionais e de aprendizado**.  

Sinta-se à vontade para estudar, modificar e aprimorar. 💡


## 👩‍💻 Autor

**Lavínia Butinholi Basílio**  

Desenvolvedora apaixonada por tecnologia e aprendizado, responsável por este projeto de estudo em **programação orientada a objetos** e **manipulação de arquivos em Python**.  
Este sistema foi criado com o objetivo de **facilitar o gerenciamento de bibliotecas** de forma prática e didática, servindo como um recurso educativo e um exemplo de boas práticas em código limpo.


## 🚀 Como Executar

### 1️⃣ Pré-requisitos
- Ter o **Python 3** instalado no sistema  
- Arquivos de dados:
  - `usuarios.txt`
  - `livros.txt`
  - `emprestimos.txt`

### 2️⃣ Clonar o repositório
```bash
git clone https://github.com/seuusuario/sistema-biblioteca.git
cd sistema-biblioteca
python biblioteca.py
