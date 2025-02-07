# Definindo as variáveis básicas
palavraSecreta = "perfume"
palavraFormatada = ["*"] * len(palavraSecreta)
contTentativas = 0

# Inicializando o loop infinito até você ganhar
while True:
    tentativa = input("Digite uma letra: ")
    contTentativas += 1

    while len(tentativa) > 1: #loop para verificar se foi digitado uma letra
        print("Só é permitido uma letra por vez!!")
        tentativa = input("Digite uma letra: ")
        contTentativas += 1

    for i in range(len(palavraSecreta)): #percorrendo a palavra secreta para ver se a letra digitada está nela e em qual posição para preencher
        if tentativa == palavraSecreta[i]:
            palavraFormatada[i] = tentativa

    wordComplete = "".join(palavraFormatada)
    print(f"Palavra Formatada: {wordComplete}")
    
    if wordComplete == palavraSecreta:
        print("VOCÊ GANHOU!!!")
        print(f"A palavra secreta era: {palavraSecreta}")
        print(f"Você usou {contTentativas} tentativas")
        break
