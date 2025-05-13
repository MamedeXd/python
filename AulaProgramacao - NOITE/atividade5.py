maca: float = 1.50
desconto: float = 5.00

quantidade_maca: float = float(input("Informe a quantidade de maçãs: "))
valor: float = quantidade_maca * maca

if valor > 20:
    print("Sua compra obteve desconto, totalizando: R$", valor - desconto)
else:
    print("Sua compra não teve desconto, o total é: R$", valor)