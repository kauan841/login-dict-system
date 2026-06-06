from .cadastro import usuarios
from .arquivo import ler_usuarios
import getpass

def login_usuario():
    usuarios = ler_usuarios()

    tentativas = 3
    while tentativas > 0:
        nome = input("Digite o nome de usuário: ").strip()
        senha = getpass.getpass("Digite a senha: ").strip()

        if nome in usuarios and usuarios[nome] == senha:
            print(f"Login bem-sucedido! Bem-vindo, {nome}.")
            return
        else:
            tentativas -= 1
            print("Nome de usuário ou senha incorretos.")
            if tentativas > 0:
                print(f"Você tem {tentativas} tentativas restantes.")

    print("Acesso bloqueado após várias tentativas.")
