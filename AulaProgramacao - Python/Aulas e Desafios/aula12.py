carros: list = ["Lamborghini", "Pagani", "Koenigsegg", "Ferrari", "Mclaren", "Porsche", "Ford Ka"]
print(carros)

'''
for carros in carros:
    if "Maserati" == carros:
        print("Carro encontrado.")
    else:
        print("Carro não encontrado.")
'''
 
#Percorrendo uma lista(array)


#len exibe o tamanho(quantidade de elementos do array)
tamanho_lista: int = len(carros)

#Acessar um elemento pelo índice
print(carros[6])

for i in range(len(carros)):
    print(carros[i])