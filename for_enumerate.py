# Dada uma lista de tarefas, escreva um código que imprima cada tarefa numerada, começando do 1.
tarefas = ["Lavar a louça", "Estudar Python", "Fazer exercícios", "Ler um livro"]

for i, tarefa in enumerate(tarefas):
    print(f'{i+1}. {tarefa}')

# Dada uma lista de números, dobre apenas os números que estão em posições ímpares.
numeros = [10, 5, 8, 3, 12, 7]

for i, numero in enumerate(numeros):
    if i % 2 != 0:
        numeros[i] *= 2
print(numeros)

# Dada uma string, substitua todas as vogais por sua posição na palavra.
texto = "python"

for i, letra in enumerate(texto):
    if letra in "aeiou":
        novo_texto = texto.replace(letra, str(i))
print(novo_texto)

# Dada uma lista de números, crie uma nova lista contendo apenas os números em índices pares.
numeros = [3, 8, 2, 5, 7, 6, 1]
lista_i_pares = []

for i, numero in enumerate(numeros):
    if i % 2 == 0:
        lista_i_pares.append(numeros[i])
print(lista_i_pares)

# Dada uma lista de palavras, crie uma nova lista contendo tuplas, onde cada tupla tem a posição da palavra na lista original e a própria palavra.
palavras = ["maçã", "banana", "uva", "laranja"]
lista_externa = []

for i, fruta in enumerate(palavras):
    lista_interna = (i, fruta)
    lista_externa.append(lista_interna)

print(lista_externa)
