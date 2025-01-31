import random
nove_digitos = ''

for i in range(9):
    nove_digitos += str(random.randint(0,9))

contagem_regressiva = 10
soma_digitos_1 = []
for i in range(9):
    soma_digitos_1.append(int(nove_digitos[i]) * contagem_regressiva)
    contagem_regressiva -= 1

soma_digitos_1 = sum(soma_digitos_1)
valida_digito_1 = (soma_digitos_1 * 10) % 11

if valida_digito_1 > 9:
    primeiro_digito = 0
else:
    primeiro_digito = valida_digito_1

dez_digitos = nove_digitos + str(primeiro_digito)
contagem_regressiva = 11
soma_digitos_2 = []

for i in range(10):
    soma_digitos_2.append(int(dez_digitos[i]) * contagem_regressiva)
    contagem_regressiva -= 1

soma_digitos_2 = sum(soma_digitos_2)
valida_digito_2 = (soma_digitos_2 * 10) % 11

if valida_digito_2 > 9:
    segundo_digito = 0
else:
    segundo_digito = valida_digito_2

cpf = dez_digitos + str(segundo_digito)

print(f"O CPF gerado foi: {cpf}")
