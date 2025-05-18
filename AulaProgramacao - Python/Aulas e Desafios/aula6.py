numero_1: float = 0
numero_2: float = 0
total: float = 0

numero_1 = float(input("Informe o primeiro número: "))
numero_2 = float(input("Informe o segundo número: "))
operador_matematico: str = input("Informe a operação desejada: +, -, *, /")

if operador_matematico == "+":
    total = numero_1 + numero_2
elif operador_matematico == "-":
    total = numero_1 - numero_2
elif operador_matematico == "*":
    total = numero_1 * numero_2
elif operador_matematico == "/":
    total = numero_1 / numero_2
else:
    print("Opção inválida")

print("O resultado é: ", total)