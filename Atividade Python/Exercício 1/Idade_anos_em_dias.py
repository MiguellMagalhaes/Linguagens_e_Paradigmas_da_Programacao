"""
Exercício 1
Escreva um programa que, a partir da idade de uma pessoa expressa em anos,
meses e dias, apresente a idade apenas em dias (considerar o ano com 365 dias
e cada mês com 30 dias).
"""

# Solicita ao utilizador o número de anos e converte a string recebida em inteiro
anos = int(input("Quantos anos completos? "))

# Solicita ao utilizador o número de meses e converte para inteiro
meses = int(input("E quantos meses adicionais? "))

# Solicita ao utilizador o número de dias e converte para inteiro
dias = int(input("E finalmente quantos dias adicionais? "))

# Converte os anos em dias multiplicando pelo valor fixo de 365 dias por ano
dias_de_anos = anos * 365

# Converte os meses em dias multiplicando pelo valor fixo de 30 dias por mês
dias_de_meses = meses * 30

# Soma todas as parcelas para obter o total de dias
dias_totais = dias_de_anos + dias_de_meses + dias

# Mostra o resultado final ao utilizador de forma clara
print(f"A tua idade em dias é: {dias_totais} dia(s).")

# -------------------------------------------------
# Trabalho realizado por: 
# 
# -> Miguel Magalhães
# Nº2021103166 
# ISPGAYA