# Recebe o número de horas trabalhadas e o valor por hora
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor por hora: R$ "))

# Calcula o salário com base nas horas extras
if horas_trabalhadas > 40:
    horas_normais = 40
    horas_extras = horas_trabalhadas - 40
    salario = (horas_normais * valor_por_hora) + (horas_extras * valor_por_hora * 1.5)
else:
    salario = horas_trabalhadas * valor_por_hora

print(f"Salário a pagar: R$ {salario:.2f}")
