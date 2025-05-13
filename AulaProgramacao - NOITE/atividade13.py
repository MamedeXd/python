lucroA: float = 0.45
lucroB: float = 0.30

valor_produto: float = float(input("Informe o valor do produto: R$"))
valor_final: float = 0.0

if valor_produto < 20:
    percentual_real: float = (valor_produto * lucroA)
    valor_final = valor_produto + percentual_real
else:
    percentual_real: float = (valor_produto * lucroB)
    valor_final = valor_produto + percentual_real
print("O valor da venda foi de: R$", valor_final)