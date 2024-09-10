# Recebe a idade do usuário
idade = int(input("Digite a sua idade: "))

# Classifica a idade
if idade < 12:
    print("Criança")
elif 12 <= idade < 18:
    print("Adolescente")
elif 18 <= idade <= 60:
    print("Adulto")
else:
    print("Idoso")
