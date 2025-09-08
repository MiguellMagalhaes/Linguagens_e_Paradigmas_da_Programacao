"""
Exercício 2
Escreva um programa que receba a idade de um atleta e determine a sua categoria
segundo a tabela apresentada:
  - Infantil : 5 a 7 anos
  - Iniciado : 8 a 10 anos
  - Juvenil  : 11 a 13 anos
  - Junior   : 14 a 17 anos
  - Sénior   : 18 anos ou mais
"""

# Solicita ao utilizador a idade do atleta e converte a entrada para inteiro
idade = int(input("Introduz a idade do atleta (em anos completos): "))

# Verifica se a idade está no intervalo 5-7 anos
if 5 <= idade <= 7:
    categoria = "Infantil"               # Atribui a categoria correspondente

# Verifica se a idade está no intervalo 8-10 anos
elif 8 <= idade <= 10:
    categoria = "Iniciado"               # Atribui a categoria correspondente

# Verifica se a idade está no intervalo 11-13 anos
elif 11 <= idade <= 13:
    categoria = "Juvenil"                # Atribui a categoria correspondente

# Verifica se a idade está no intervalo 14-17 anos
elif 14 <= idade <= 17:
    categoria = "Junior"                 # Atribui a categoria correspondente

# Verifica se a idade é igual ou superior a 18 anos
elif idade >= 18:
    categoria = "Sénior"                 # Atribui a categoria correspondente

# Caso a idade seja inferior a 5 anos, não existe categoria definida
else:
    categoria = "Sem categoria definida" # Guarda informação de ausência de categoria

# Apresenta a categoria final ao utilizador
print(f"O atleta enquadra-se na categoria: {categoria}")

# -------------------------------------------------
# Trabalho realizado por: 
# 
# ->Miguel Magalhães
# Nº2021103166 
# ISPGAYA