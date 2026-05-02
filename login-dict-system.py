usuarios = {}


def cadastro_usuario():
    
    nome = input("Digite um nome de usuário: ").strip()
    if nome in usuarios:
        print("Nome de usuário já existe. Tente outro.")
        return
    if not nome:
        print("Nome de usuário não pode ser vazio.")
        return
    
    senha = input("Digite uma senha: ").strip()
    usuarios[nome] = senha
    print("Usuário cadastrado com sucesso!")
    
    if not senha:
        print("Senha não pode ser vazia.")
        return
  


def login_usuario():

    tentativas = 3
    while tentativas > 0:
        nome = input("Digite o nome de usuário: ").strip()
        senha = input("Digite a senha: ").strip()

        if nome in usuarios and usuarios[nome] == senha:
            print(f"Login bem-sucedido! Bem-vindo, {nome}.")
            return
        else:
            tentativas -= 1
            print("Nome de usuário ou senha incorretos.")
            if tentativas > 0:
                print(f"Você tem {tentativas} tentativas restantes.")

    print("Acesso bloqueado após várias tentativas.")


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