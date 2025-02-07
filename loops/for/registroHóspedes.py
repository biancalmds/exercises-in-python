# Estudo com foco no uso do for (sem tratamento de erros)
'''
Digamos que você está criando um sistema para registrar a chegada hóspedes em um hotel. 
No hotel os hóspedes podem ter quartos com 1, 2, 3 e 4 pessoas. Seu sistema deve conseguir:
    1. Identificar quantas pessoas o hóspede que acabou de chegar vai ter no quarto;
    2. De acordo com a quantidade de pessoas do hóspede, ele deve perguntar o cpf e o nome de cada pessoa, a fim de registrá-la no quarto (2 inputs para cada pessoa. 1 para o cpf e outro para o nome);
    3. O seu programa então deve gerar uma lista com todas as pessoas que ficarão no quarto em que cada item dessa lista é o nome da pessoa e o seu cpf.
'''
quarto = []
qnt_pessoas = int(input("Digite quantas pessoas vão se hospedar no quarto: "))

for i in range(qnt_pessoas):
    nome = input(f"Digite o nome do {i+1}° hóspede: ")
    cpf = int(input(f"Digite o cpf do {i+1}° hóspede: "))
    hospede = [nome, cpf]
    quarto.append(hospede)

for pessoas in quarto:
    print(pessoas)
