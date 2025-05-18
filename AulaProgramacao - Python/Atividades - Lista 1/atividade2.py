print("Aqui calcularemos seu conceito na disciplina BCC201 - Introdução à Programação!")

conceito: str = input("Informe seu conceito: A, B, C, D, E ou F - ")

if conceito == "A":
    print("Excelente")
elif conceito == "B":
    print("Ótimo")
elif conceito == "C":
    print("Bom")
elif conceito == "D":
    print("Regular")
elif conceito == "E":
    print("Ruim")
else:
    print("Nos vemos de novo no ano que vem")