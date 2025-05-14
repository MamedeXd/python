codigo: int = int(input("Digite o código de produto desejado (100, 101, 102, 103, 104): "))
quantidade_produto: int = int(input("Digite a quantidade de itens que deseja: "))

match codigo:
    case 100:
        valor_camisa: float = 120
        total: float = valor_camisa * quantidade_produto
        print("O produto escolhido é CAMISA, e sua compra deu um total de: R$", total)
    case 101:
        valor_saia: float = 220
        total: float = valor_saia * quantidade_produto
        print("O produto escolhido é SAIA, e sua compra deu um total de: R$", total)
    case 102:
        valor_calca: float = 180
        total: float = valor_calca * quantidade_produto
        print("O produto escolhido é CALÇA, e sua compra deu um total de: R$", total)
    case 103:
        valor_vestido: float = 350
        total: float = valor_vestido * quantidade_produto
        print("O produto escolhido é VESTIDO, e sua compra deu um total de: R$", total)
    case 104:
        valor_meia: float = 7.50
        total: float = valor_meia * quantidade_produto
        print("O produto escolhido é MEIA, e sua compra deu um total de: R$", total)
    case _:
        print("O código é inválido!")