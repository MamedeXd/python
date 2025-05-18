busca_menu: str = input("Digite uma letra para buscar a aba que deseja, entre: A, B, C, D ou X. Qual a opção desejada? ").upper()

match busca_menu:
    case "A":
        print("Você escolheu 'Ver saldo'. O seu saldo é: ... tadinho kkkkkkkk, melhor nem saber.")
    case "B":
        print("Você escolheu 'DEPOSITAR'. Para depositar, consulte o código de segurança do seu banco.")
    case "C":
        print("Você escolheu 'SACAR'. Lamentamos, mas você não tem saldo suficiente para o saque.")
    case "D":
        print("Você escolheu 'ENCERRAR CONTA'. Tem certeza que deseja fazer isso? Não recomendamos hein.")
    case "X":
        print("Você escolheu 'SAIR DO SISTEMA'. Você será redirecionado para a tela inicial, agradecemos pela confiança.")
    case _:
        print("Opção inválida, digite uma das opções acima por gentileza.")