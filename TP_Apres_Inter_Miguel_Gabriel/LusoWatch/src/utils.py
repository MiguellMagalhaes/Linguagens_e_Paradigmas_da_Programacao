
# Resumo: Função utilitária que lê um ficheiro CSV contendo pares
# (palavra_br, sugestao_pt) e devolve um dicionário que mapeará cada termo
# brasileiro para a sua sugestão em português europeu. Caso o ficheiro não
# exista, avisa o utilizador e devolve um dicionário vazio.

# Importações necessárias
# Importa o módulo 'os' para operações com o sistema de ficheiros.
# Importa o módulo 'csv' para leitura e escrita de ficheiros CSV.
import os               # Módulo da biblioteca padrão para operações com o sistema de ficheiros.
import csv              # Módulo da biblioteca padrão para leitura e escrita de ficheiros CSV.

def carregar_termos(csv_path: str) -> dict:  # Define a função que recebe o caminho do CSV e devolve um dicionário BR→PT.
    """
    Lê um ficheiro CSV (palavra_br, sugestao_pt) e devolve um dicionário:
    { 'palavra_br': 'sugestao_pt', ... }.
    
    :param csv_path: Caminho para o ficheiro CSV.
    :return: Dicionário mapeando palavras BR -> sugestão PT.
    """
    termos_br_pt = {}                                             # Inicializa dicionário vazio para armazenar os pares.
    if not os.path.exists(csv_path):                              # Verifica se o ficheiro existe.
        print(f"[AVISO] Ficheiro {csv_path} não encontrado. A usar base de dados vazia.")
        return termos_br_pt                                       # Se não existir, devolve dicionário vazio.

    with open(csv_path, mode='r', encoding='utf-8') as f:         # Abre o CSV em modo leitura com codificação UTF‑8.
        reader = csv.DictReader(f, delimiter=',')                 # Utiliza DictReader para ler cada linha como dicionário.
        for row in reader:                                        # Percorre cada linha (row) do ficheiro.
            br = row['palavra_br'].strip().lower()                # Extrai a coluna 'palavra_br', retira espaços, converte para minúsculas.
            pt = row['sugestao_pt'].strip()                       # Extrai a coluna 'sugestao_pt' e retira espaços.
            termos_br_pt[br] = pt                                 # Adiciona o par BR→PT ao dicionário.
    return termos_br_pt                                           # Devolve o dicionário completo.

# Resumo: Função utilitária que lê um ficheiro CSV contendo pares
# Este trabalho foi realizado no âmbito da Unidade Curricular de Linguagens e Paradigmas de Programação
# do Curso de Engenharia Informática, pelos alunos:
# -> Miguel Magalhães, Nº 2021103166;
# -> Gabriel Fernando, Nº 2021101890.

# © 2025 Miguel Magalhães & Gabriel Fernando. Todos os direitos reservados.
# Este código é parte de um projeto académico e não deve ser utilizado para fins comerciais.