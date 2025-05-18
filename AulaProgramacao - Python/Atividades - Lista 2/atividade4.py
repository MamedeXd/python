numero1: float = float(input("Digite um número positivo: "))
numero2: float = float(input("Digite outro número positivo: "))

if numero1 and numero2 < 0:
    print("O número não pode ser negativo.")

while numero1 and numero2 >= 0:
    soma: float = numero1 + numero2
    print(f"A soma dos números {numero1} e {numero2} resulta em: ", soma)
    break

#else:
    print("O número não pode ser negativo.")