'''
    Para ser aprovado em um curso, o aluno deve possuir nota maior que 6. Se for, então seu status é aprovado.
    Se for menor que 4, seu status é reprovado, e se tiver entre 4 e 6, ele está de recuperação.
    
    Crie um programa que receba uma nota e diz qual é o status do aluno.
'''

nome: str = input("Informe seu nome: ")
nota: float = float(input("Informe sua nota: "))

if nota >= 6.0:
    print("Você está aprovado,", nome, ".")
elif nota <= 4.0:
    print("Você foi reprovado.,", nome, ".")
else:
    print("Você está de recuperação,", nome, ".")