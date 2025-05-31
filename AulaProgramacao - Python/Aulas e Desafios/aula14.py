#Dicionários são estruturas do tipo coleção que armazenam dados do tipo Chave : Valor

dict_carro: dict = {
    "marca" : "FIAT",
    "modelo" : "Chronos",
    "ano" : 2023,
    "cor" : "Prata"
}

print("O modelo do carro é: ", dict_carro["modelo"]) #buscando pela chave

print("O ano do carro é: ", dict_carro.get("ano")) #buscando pela chave

print(dict_carro) #buscando a informação direta

dict_proprietario: dict = {}
nome: str = input("Informe o nome: ")
cpf: str = input("Informe o CPF: ")
tel: str = input("Informe o telefone: ")
dict_proprietario["nome_prop"] = nome #nome_prop é a chave que está sendo criada para o nome
dict_proprietario["cpf_prop"] = cpf #cpf_prop é a chave que está sendo criada para o CPF
dict_proprietario["tel_prop"] = tel #tel_prop é a chave que está sendo criada para o telefone

print(dict_proprietario)

#Retorna as chaves do dicionário
print(dict_carro.keys())

#Retorna os valores do dicionário
print(dict_carro.values())

for item in dict_carro.keys():
    print(dict_carro[item])

#ou:
# for item in dict_carro.keys():
# print(dict_carro.get(item))

#Apagar um elemento
dict_carro.pop("marca")
print(dict_carro)

del dict_carro["modelo"]
print(dict_carro)