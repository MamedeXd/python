codigo: int = int(input("Digite o código de produto desejado (100, 101, 102, 103, 104): "))

match codigo:
    case 100:
        print("O produto escolhido é CAMISA, e seu valor é R$120")
    case 101:
        print("O produto escolhido é SAIA, e seu valor é R$220")
    case 102:
        print("O produto escolhido é CALÇA, e seu valor é R$180")
    case 103:
        print("O produto escolhido é VESTIDO, e seu valor é R$350")
    case 104:
        print("O produto escolhido é MEIA, e seu valor é R$7.50")
    case _:
        print("O código é inválido!")