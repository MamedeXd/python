aux: int = 0
contador: int = 0

while contador < 3:
    num1: int = int (input("Informe um número: "))
    if num1 > aux:
        aux = num1
    contador = contador + 1

print("O maior número é: ", aux)