"""
Exercício 3
Escreva um programa para determinar a situação de um aluno (Aprovado, Exame ou
Reprovado) dada a sua assiduidade em percentagem e a nota do teste (0 a 20),
considerando a seguinte tabela de decisão:

  - Assiduidade inferior a 75 %                -> Reprovado
  - Assiduidade entre 75 % e 100 % e nota até 5 -> Reprovado
  - Assiduidade entre 75 % e 100 % e nota de 5 até 9,4 -> Exame
  - Assiduidade entre 75 % e 100 % e nota entre 9,5 e 20 -> Aprovado
"""

# Solicita ao utilizador a assiduidade em percentagem e converte para float
assiduidade = float(input("Introduz a assiduidade do aluno (0 a 100 %): "))

# Solicita ao utilizador a nota do teste e converte para float
nota = float(input("Introduz a nota do teste (0 a 20): "))

# Valida se a assiduidade está abaixo de 0 % ou acima de 100 %
if assiduidade < 0 or assiduidade > 100:
    # Informa o utilizador que o valor é inválido e termina o programa
    print("Erro: a assiduidade deve estar entre 0 % e 100 %.")
    exit()  # Encerra a execução porque os dados não são válidos

# Valida se a nota está fora do intervalo permitido 0–20
if nota < 0 or nota > 20:
    # Informa o utilizador que o valor é inválido e termina o programa
    print("Erro: a nota deve estar entre 0 e 20.")
    exit()  # Encerra a execução porque os dados não são válidos

# Verifica primeiro se a assiduidade é inferior a 75 %
if assiduidade < 75:
    situacao = "Reprovado"            # Define a situação directamente

# Se a assiduidade é igual ou superior a 75 %, avalia-se a nota
elif nota <= 5:
    situacao = "Reprovado"            # Nota muito baixa implica reprovação

elif nota < 9.5:                      # Aqui já sabemos que nota > 5
    situacao = "Exame"                # Nota intermédia implica exame

else:                                 # Nota igual ou superior a 9,5
    situacao = "Aprovado"             # Aluno cumpre critérios para aprovação

# Apresenta a situação final ao utilizador
print(f"Situação do aluno: {situacao}")

# -------------------------------------------------
# Trabalho realizado por: 
# 
# -> Miguel Magalhães
# Nº2021103166 
# ISPGAYA