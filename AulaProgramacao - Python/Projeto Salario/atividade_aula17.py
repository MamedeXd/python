'''
    1- Uma empresa paga 45.90 por hora para um analista de sistemas pleno.
    Crie um programa que contém uma função que receba o número de horas
    trabalhadas no mês, através de um parâmetro e exibe o salário bruto.
    Calcular o INSS a ser pago.
    Calcular o FGTS.
    Calcular o Imposto de Renda.
    Encontrar o Salário Líquido.
'''

VALOR_HORA_BASE: float = 45.90

def calcula_salario_bruto(hora_trabalho: float):
    salario_bruto: float = hora_trabalho * VALOR_HORA_BASE
    print(f"O salário bruto é de R${salario_bruto}")
    return salario_bruto

def calcula_inss(salario_bruto: float):
    percentual: float = 0.0
    if salario_bruto <= 1518:
         percentual = 0.075  
    elif salario_bruto > 1518 and salario_bruto <= 2793.88:
         percentual = 0.09
    elif salario_bruto > 2793.88 and salario_bruto <= 4190.83:
         percentual = 0.12
    else:
         percentual = 0.14
    
    valor_inss: float = salario_bruto * percentual
    print(f"O valor do INSS é R${valor_inss}.")
    return valor_inss

def calcula_fgts(salario_bruto: float):
     fgts: float = salario_bruto * 0.08
     print(f"O FGTS é R${fgts}")
     return fgts

def calcula_imposto_renda(salario_bruto: float):
     aliquota: float = 0.0
     if salario_bruto > 2428.80 and salario_bruto < 2826.65:
          aliquota = 0.075
     elif salario_bruto > 2826.65 and salario_bruto < 3751.05:
          aliquota = 0.15
     elif salario_bruto > 3751.05 and salario_bruto < 4664.68:
          aliquota = 0.225
     elif salario_bruto > 4664.68:
          aliquota = 0.275
     
     imposto_renda: float = salario_bruto * aliquota
     print(f"O imposto de renda a ser pago é R${imposto_renda}.")
     return imposto_renda

def salario_liquido(salario_bruto: float, fgts: float, inss: float, imposto_renda: float):
     liquido: float = salario_bruto - (fgts + inss + imposto_renda)
     print(f"O salário líquido é R${liquido}")

trabalhado: float = float(input("Quantas horas trabalhou nesse mês?: "))
valor_salario: float = calcula_salario_bruto(trabalhado)
valor_inss: float = calcula_inss(valor_salario)
valor_fgts: float = calcula_fgts(valor_salario)
valor_ir: float = calcula_imposto_renda(valor_salario)
salario_liquido(valor_salario, valor_fgts, valor_inss, valor_ir)