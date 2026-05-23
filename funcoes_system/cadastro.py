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