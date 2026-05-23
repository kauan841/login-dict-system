
import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from funcoes_system.cadastro import cadastro_usuario
from funcoes_system.login import login_usuario


while True:
        print("\n=== Sistema de Login ===")
        print('seja bem-vindo! O que deseja fazer?')

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