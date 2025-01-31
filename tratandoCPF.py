cpf = input("Insira seu CPF: ")
cpf = cpf.strip() #removendo espaços em branco
cpf = cpf.replace(".", "") #removendo os pontos
cpf = cpf.replace("-", "") #removendo os traços

while True:
    if (len(cpf) != 11) or (cpf.isnumeric() == False):
        print("\nDigite seu CPF corretamente!!!")
        cpf = input("Insira seu CPF: ") 
        cpf = cpf.strip()
        cpf = cpf.replace(".", "") 
        cpf = cpf.replace("-", "") 
    else:
        print(f"Você digitou seu CPF corretamente! Seu CPF é {cpf}")
        break

