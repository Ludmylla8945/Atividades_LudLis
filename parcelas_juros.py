# Recebe o valor da compra e a quantidade de parcelas
valor_compra = float(input("Digite o valor da compra: R$ "))
parcelas = int(input("Digite a quantidade de parcelas (1 a 24): "))

# Calcula o valor da parcela e o valor total a pagar
if parcelas > 12:
    juros = 0.015
    valor_total = valor_compra * (1 + juros)
    valor_parcela = (valor_total + (parcelas - 12) * 6) / parcelas
else:
    valor_total = valor_compra
    valor_parcela = valor_total / parcelas

print(f"Valor total a pagar: R$ {valor_total:.2f}")
print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")
