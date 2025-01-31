import os

while True:
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")

    if nome and email: #verifica se todos os campos foram preenchidos

        if "@" and ".com" in email: #verifica se existe "@" e ".com"
            indiceArroba = email.find("@")
            indicePonto = email.find(".")

            if indiceArroba < indicePonto: #verifica se o "@" está antes do ".com"
                print("Email válido")
                break
            else:
                os.system("cls")
                print("Email inválido") 
                continue     

        else:
            os.system("cls")
            print("Email inválido")
            continue

    else:
        os.system("cls")
        print("Preencha todos os campos")
        continue