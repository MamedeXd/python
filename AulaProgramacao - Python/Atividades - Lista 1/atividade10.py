numero: float = float(input("Digite o número que deseja conferir: "))

if numero > 0:
    print("O número digitado é positivo!")
elif numero == 0:
    print("O número 0 não é nem positivo, nem negativo!")
else:
    print("O número digitado é negativo!")