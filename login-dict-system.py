usuarios = []


def cadastro_usuario():
    nome = input("Digite o nome de usuário: ").strip()
    senha = input("Digite a senha: ").strip()

    if not nome or not senha:
        print("Preencha todos os campos.")
        return

    if nome in usuarios:
        print("Usuário já existe.")
    else:
        usuarios[nome] = senha
        print("Usuário registrado com sucesso!")


def login_usuario():
    nome = input("Digite o nome de usuário: ").strip()
    senha = input("Digite a senha: ").strip()

    if not nome or not senha:
        print("Preencha todos os campos.")
        return

    if nome in usuarios and usuarios[nome] == senha:
        print("Login realizado com sucesso!")
    else:
        print("Nome de usuário ou senha incorretos.")


def main():
    while True:
        print("\n1. Cadastrar-se")
        print("2. Login")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastro_usuario()
        elif escolha == '2':
            login_usuario()
        elif escolha == '3':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


main()