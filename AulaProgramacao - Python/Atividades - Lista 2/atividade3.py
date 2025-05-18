numero1: float = float(input("Digite o primeiro número: "))
numero2: float = float(input("Digite o segundo número: "))
numero3: float = float(input("Digite o terceiro número: "))

if numero1 > numero2 and numero3:
    print("O primeiro número é o maior.")
elif numero2 > numero1 and numero3:
    print("O segundo número é o maior.")
elif numero3 > numero1 and numero2:
    print("O terceiro número é o maior.")
else:
    print("Todos os números são iguais.")