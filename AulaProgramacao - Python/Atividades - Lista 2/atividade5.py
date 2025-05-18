login: str = input("Digite o login de acesso: ")
senha: str = input("Digite a senha: ")

while senha != "admin123":
    print("Senha incorreta, tente novamente.")
    break
else:
    print("Senha correta, acesso liberado.")