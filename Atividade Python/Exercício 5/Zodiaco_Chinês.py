"""
Exercício 5 – Listas / Zodíaco Chinês
O Zodíaco chinês é composto por animais com ciclo de 12 anos. Uma maneira
simplificada de identificar o signo é verificar apenas o ano de nascimento,
aplicando a operação ano % 12 segundo a tabela:

  resto 0  -> Macaco
  resto 1  -> Galo
  resto 2  -> Cão
  resto 3  -> Porco
  resto 4  -> Rato
  resto 5  -> Boi
  resto 6  -> Tigre
  resto 7  -> Coelho
  resto 8  -> Dragão
  resto 9  -> Serpente
  resto 10 -> Cavalo
  resto 11 -> Carneiro
"""

# Cria uma lista com os 12 signos pela ordem do resto da divisão por 12
signos = [
    "Macaco",   # índice 0  → resto 0
    "Galo",     # índice 1  → resto 1
    "Cão",      # índice 2  → resto 2
    "Porco",    # índice 3  → resto 3
    "Rato",     # índice 4  → resto 4
    "Boi",      # índice 5  → resto 5
    "Tigre",    # índice 6  → resto 6
    "Coelho",   # índice 7  → resto 7
    "Dragão",   # índice 8  → resto 8
    "Serpente", # índice 9  → resto 9
    "Cavalo",   # índice 10 → resto 10
    "Carneiro"  # índice 11 → resto 11
]

# Pede ao utilizador o ano de nascimento e converte a resposta para inteiro
ano = int(input("Introduz o teu ano de nascimento (ex.: 1998): "))

# Calcula o resto da divisão do ano por 12 para descobrir a posição na lista
resto = ano % 12

# Selecciona o signo correspondente usando o resto como índice
signo = signos[resto]

# Mostra o signo ao utilizador numa frase completa
print(f"O teu signo do Zodíaco chinês é: {signo}")

# -------------------------------------------------
# Trabalho realizado por: 
# 
# -> Miguel Magalhães
# Nº2021103166
# ISPGAYA