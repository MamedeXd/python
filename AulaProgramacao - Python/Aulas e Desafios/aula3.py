# Comando de entrada de dados via terminal input()
# Comando de saída de dados vis terminal print()
nome_recebido: str = ""
print("Informe um nome:")
nome_recebido = input()
print("O nome é",nome_recebido)

'''
    Operações  matemáticas:
        +soma
        -subtração
        *multiplicação
        /divisão
        **exponenciação
        %resto da divisão
'''

num1: int = 5  # primeiro valor de cálculo
num2: int = 10  # segundo valor de cálculo
total: float = 0  # receber o valor dos cálculos

total = num1 + num2  # resultado da soma
print("O resultado da soma é",total)

total = num2 - num1  # resultado da subtração
print("O resultado da subtração é",total)

total = num1 * num2  # resultado da multiplicação
print("O resultado da multiplicação é",total)

total = num2 / num1  # resultado da divisão
print("O resultado da divisão é",total)