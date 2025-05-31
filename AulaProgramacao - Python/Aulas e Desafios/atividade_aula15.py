def quadrado():
    base: int = int(input("Digite uma medida: "))
    altura = base

    area = base * altura
    print(f"A área do quadrado é {area}cm².")

quadrado()

def triangulo():
    base: int = int(input("Digite a base: "))
    altura: int = int(input("Digite a altura: "))

    area = (base * altura) / 2
    print(f"A área do triângulo é {area}cm².")

triangulo()

def retangulo():
    base: int = int(input("Digite a base: "))
    altura: int = int(input("Digite a altura: "))

    area = base * altura
    print(f"A área do retângulo é {area}cm².")

retangulo()

def circulo():
    raio: int = int(input("Digite o raio do círculo: "))
    pi: float = 3.14
    
    area = pi * (raio**2)
    print(f"A área do círculo é {area}cm².")

circulo()