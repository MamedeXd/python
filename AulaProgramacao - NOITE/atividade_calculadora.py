pi: float = 3.14
area: float = 0.0

opcao: str = input("Digite uma das opções entre C, Q ou R: ")
match opcao:
    case "C":
        raio: float = float(input("Informe o raio: "))
        area = pi * (raio ** 2)
        print(f"A área do círculo é: {area}cm²")
    case "R":
        base: float = float(input("Informe a base do retângulo: "))
        altura: float = float(input("Informe a altura do retângulo: "))
        area = base * altura
        print(f"A área do retângulo é: {area}cm²")
    case "Q":
        lado: float = float(input("Informe a medida do lado: "))
        area = lado ** 2
        print(f"A área do quadrado é: {area}cm²")
    case _:
        print("A opção é inválida.")