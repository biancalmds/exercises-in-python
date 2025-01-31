cpf = input("Insira seu CPF: ")
cpf = cpf.strip() #removendo espaços em branco
if "." or "-" in cpf:
    cpfModificado = cpf[:4].strip(".") + cpf[4:8].strip(".") + cpf[8:12].strip("-") + cpf[12:] #removendo "." e "-" com strip, devido a este método remover os caracteres indesejados apenas ao final, estou realizando o fatiamento do mesmo!

while True:
    if (len(cpfModificado) != 11) or (cpfModificado.isnumeric() == False):
        print("\nDigite seu CPF corretamente!!!")
        cpf = input("Insira seu CPF: ") 
        cpf = cpf.strip()
        if "." or "-" in cpf:
            cpfModificado = cpf[:4].strip(".") + cpf[4:8].strip(".") + cpf[8:12].strip("-") + cpf[12:]
    else:
        print(f"Você digitou seu CPF corretamente! Seu CPF é {cpfModificado}")
        break