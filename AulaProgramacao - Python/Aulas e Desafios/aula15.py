# Função é um bloco de código que pode ser chamado - Função simples e sem retorno

def somar():
    print("Somar foi chamada!")
    num1: int = int(input("Informe um número: "))
    num2: int = int(input("Informe outro número: "))
    
    total: int = num1 + num2
    print("O total é", total)

def subtrair():
    print("Subtrair foi chamada!")
    num1: int = int(input("Informe um número: "))
    num2: int = int(input("Informe outro número: "))
    
    total: int = num1 - num2
    print("O total é ", total)

somar() #Invocando a soma
subtrair() #Invocando a subtração


'''
    Crie uma aplicação para calcular a área de figuras geométricas:
        Quadrado;
        Triangulo;
        Retangulo;
        Círculo;
    Cada cálculo deve ser feito dentro de uma função específica.
    Desafio:
     Crie um sistema baseado em escolhas que de acordo com a opção
     selecionada pelo usuário a função determinada é chamada.
'''