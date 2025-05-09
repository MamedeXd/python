maça: float = 1.50
n1: int = 0
total: int = maça * n1

n1 = float(input("Digite a quantidade de maçãs: "))

if total > 20:
    print("Sua compra tem um desconto de 5 reais. O total é: ", total-5)
else:
    print("Sem desconto aplicável. O total é: ", total)