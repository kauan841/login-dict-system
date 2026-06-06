
import os
import sys
import json



sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from funcoes_system.cadastro import cadastro_usuario ,usuarios
from funcoes_system.login import login_usuario


caminho_arquivo = r"C:\\Users\\kaike\\Desktop\\login_system\\dados\\login.json"
   
try:
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        usuarios.update(json.load(arquivo))
except (FileNotFoundError, json.JSONDecodeError):
    pass
        


while True:
        print("\n=== Sistema de Login ===")
        print('seja bem-vindo! O que deseja fazer?')

        print("\n1. Cadastrar-se")
        print("2. Login")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastro_usuario()
            caminho_arquivo = r"C:\\Users\\kaike\\Desktop\\login_system\\dados\\login.json"
            with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
                json.dump(usuarios, arquivo, ensure_ascii=False, indent=4)

        elif escolha == '2':
            login_usuario()

        elif escolha == '3':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")