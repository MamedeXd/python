print(" XD - VALIDADOR DE APOSENTADORIA INSS - XD")
idade: int = int(input("Informe a idade do contribuinte: "))
tempo_contribuicao: int = int(input("Informe o tempo de contribuição: "))

if idade >= 65 or tempo_contribuicao >= 35:
    print("O GERENTE ENLOUQUECEU!!! CLIQUE NO LINK PARA RECEBER SEU DEPÓSITO INSS!")
else:
    print("Aposentadoria Negada!! Continue na luta aí LOL.")

'''
    Para entrar em uma rede social é necessário informar um login e uma senha;
    Para testes foi criado um usuário padrão proz@25 e a senha é admin123.
    Crie um sistema de login que peça ao usuário um login e uma senha e exiba a mensagem : Logado com sucesso.
    Senão, escreva: Login ou senha inválidas.
'''