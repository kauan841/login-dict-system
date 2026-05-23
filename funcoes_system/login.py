from .cadastro import usuarios


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
