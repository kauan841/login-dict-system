import json

def ler_usuarios():
    caminho_arquivo = r"C:\\Users\\kaike\\Desktop\\login_system\\dados\\login.json"
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

     