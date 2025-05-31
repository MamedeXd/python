import aula15

'''
Crie um programa que receba uma palavra e uma letra.
Conte quantas vezes a letra digitada aparece na palavra.
'''

palavra: str = input("informe a palavra: ")
letra_buscada: str = input("Informe a letra a ser buscada: ")
total: int = 0
for letra in palavra:
    print("A letra atual: ", letra)
    if letra == letra_buscada:
        total = total + 1
print(f"O total de '{letra_buscada}' na palavra {palavra} é {total}.")

aula15.somar()

'''
palavra: str = input("Digite uma palavra: ")
letra: str = input("Digite a letra a ser contada: ")
quantidade = palavra.count(letra)

print(f"A letra {letra} aparece {quantidade} vezes.")
'''