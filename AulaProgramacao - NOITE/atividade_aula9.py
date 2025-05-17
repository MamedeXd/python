login: str = input("Digite o login de acesso: ")
senha: str = input("Digite a senha: ")

if login == "proz@25" and senha == "admin123":
    print("Logado com sucesso. Você pode acessar agora.")
else:
    print("Login ou senha inválido(s). Tente novamente.")