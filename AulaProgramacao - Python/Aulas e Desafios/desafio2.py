codigo: int = int(input("Digite o código de produto desejado (100, 101, 102, 103, 104): "))
quantidade_produto: int = int(input("Digite a quantidade de itens que deseja: "))
produto: str = ""
total: float = 0.0

match codigo:
    case 100:
        total: float = 120 * quantidade_produto
        produto = "Camisa"
    case 101:
        total: float = 220 * quantidade_produto
        produto = "Saia"
    case 102:
        total: float = 180 * quantidade_produto
        produto = "Calça"
    case 103:
        total: float = 350 * quantidade_produto
        produto = "Vestido"
    case 104:
        total: float = 7.50 * quantidade_produto
        produto = "Meia"
    case _:
        print("O código é inválido!")

if total >= 500:
    desconto: float = total * 0.10
    print(f"Sua compra de {produto} teve desconto de 10%, e o valor final foi: R$", total - desconto)
else:
    print(f"O valor do/da(s) {produto} é R${total}")
