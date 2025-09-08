"""
Exercício 4 (Ciclos)
Escreva um programa que permita registar o nome, a altura e o peso de duas
pessoas e apresente o nome da pessoa mais pesada e o nome da pessoa mais alta.
"""

# Guarda o nome da pessoa mais pesada (começa vazio)
nome_mais_pesada = ""

# Guarda o peso da pessoa mais pesada (começa a zero porque qualquer peso é maior)
peso_mais_alto = 0.0

# Guarda o nome da pessoa mais alta (começa vazio)
nome_mais_alta = ""

# Guarda a altura da pessoa mais alta (começa a zero porque qualquer altura é maior)
altura_mais_alta = 0.0

# Ciclo que se repete duas vezes, uma por cada pessoa a registar
for i in range(2):  # range(2) devolve 0 e 1
    # Lê o nome da pessoa actual
    nome = input(f"Introduz o nome da pessoa {i + 1}: ")

    # Lê a altura em metros (usa ponto como separador decimal) e converte para float
    altura = float(input("Introduz a altura (em metros): "))

    # Lê o peso em quilogramas e converte para float
    peso = float(input("Introduz o peso (em kg): "))

    # Se o peso introduzido for maior que o peso máximo guardado até agora
    if peso > peso_mais_alto:
        peso_mais_alto = peso        # Actualiza o maior peso
        nome_mais_pesada = nome      # Guarda o nome dessa pessoa

    # Se a altura introduzida for maior que a altura máxima guardada até agora
    if altura > altura_mais_alta:
        altura_mais_alta = altura    # Actualiza a maior altura
        nome_mais_alta = nome        # Guarda o nome dessa pessoa

# Depois do ciclo, apresenta o nome da pessoa mais pesada
print(f"A pessoa mais pesada é: {nome_mais_pesada}")

# Apresenta o nome da pessoa mais alta
print(f"A pessoa mais alta é: {nome_mais_alta}")

# -------------------------------------------------
# Trabalho realizado por: 
# 
# -> Miguel Magalhães
# Nº2021103166 
# ISPGAYA