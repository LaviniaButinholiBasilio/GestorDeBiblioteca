import os

class Usuario:
    def _init_(self, codigo, nome, tipo):
        self.codigo = codigo
        self.nome = nome
        self.tipo = tipo

class SistemaUsuarios:
    def _init_(self, usuarios_path="usuarios.txt"):
        self.usuarios_path = usuarios_path
        self.usuario_atual = None

    def validar_usuario(self, login, senha):
        try:
            with open(self.usuarios_path, "r") as file:
                for linha in file:
                    codigo, nome, tipo, login_arquivo, senha_arquivo = linha.strip().split(",")
                    if login.strip() == login_arquivo.strip() and senha.strip() == senha_arquivo.strip():
                        self.usuario_atual = Usuario(codigo, nome, tipo)
                        return True
            return False
        except FileNotFoundError:
            print("Arquivo de usuários não encontrado!")
            return False

class SistemaLivros:
    def _init_(self, livros_path="livros.txt"):
        self.livros_path = livros_path

    def listar_livros(self):
        try:
            with open(self.livros_path, "r") as file:
                print("\n--- Livros Disponíveis ---")
                for linha in file:
                    codigo, nome, autor = linha.strip().split(",")
                    print(f"Código: {codigo}, Nome: {nome}, Autor: {autor}")
        except FileNotFoundError:
            print("Arquivo de livros não encontrado!")

class SistemaEmprestimos:
    def _init_(self, emprestimos_path="emprestimos.txt"):
        self.emprestimos_path = emprestimos_path

    def listar_emprestimos(self, usuario):
        if not usuario:
            print("Nenhum usuário logado!")
            return
        try:
            with open(self.emprestimos_path, "r") as file:
                print(f"\n--- Empréstimos de {usuario.nome} ---")
                for linha in file:
                    codigo, cliente, livro, data = linha.strip().split(",")
                    if cliente == usuario.codigo:
                        print(f"Código: {codigo}, Livro: {livro}, Data: {data}")
        except FileNotFoundError:
            print("Arquivo de empréstimos não encontrado!")

class SistemaBiblioteca:
    def _init_(self):
        self.usuarios = SistemaUsuarios()
        self.livros = SistemaLivros()
        self.emprestimos = SistemaEmprestimos()

    def sobre(self):
        print("\n--- Sobre o Sistema ---")
        print("Empresa: TechBooks Solutions")
        print("Desenvolvedores: João, Maria, Ana")
        print("Programa: Sistema de Biblioteca")
        print("Descrição: Este sistema permite gerenciar empréstimos e visualizar livros de maneira prática.")

    def menu_usuario(self):
        while True:
            print("\n--- Menu ---")
            print("1 - Visualizar Empréstimos")
            print("2 - Visualizar Livros")
            print("3 - Sobre")
            print("4 - Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.emprestimos.listar_emprestimos(self.usuarios.usuario_atual)
            elif escolha == "2":
                self.livros.listar_livros()
            elif escolha == "3":
                self.sobre()
            elif escolha == "4":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida! Tente novamente.")

def main():
    sistema = SistemaBiblioteca()
    print("\n--- Bem-vindo ao Sistema de Biblioteca ---")
    login = input("Informe o login: ")
    senha = input("Informe a senha: ")

    if sistema.usuarios.validar_usuario(login, senha):
        print(f"Bem-vindo, {sistema.usuarios.usuario_atual.nome}!")
        sistema.menu_usuario()
    else:
        print("Login ou senha inválidos!")

if __name__ == "__main__":
    main()