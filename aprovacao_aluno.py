# Recebe a nota final e a frequência do aluno
nota = float(input("Digite a nota final: "))
frequencia = float(input("Digite a frequência (%): "))

# Verifica se o aluno foi aprovado
if nota >= 7 and frequencia >= 75:
    print("Aluno aprovado.")
else:
    print("Aluno reprovado.")
