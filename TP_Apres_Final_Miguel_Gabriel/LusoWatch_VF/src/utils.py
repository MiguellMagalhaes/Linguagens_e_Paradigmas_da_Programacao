# Resumo: Função utilitária que lê um ficheiro CSV contendo pares
# (palavra_br, sugestao_pt) ou tripletas (UK, US, alvo) e devolve um
# dicionário que mapeia variantes para o termo alvo, incluindo meta-infos.

# Importações necessárias
import os  # Módulo da biblioteca padrão para operações com o sistema de ficheiros.
import csv  # Módulo da biblioteca padrão para leitura e escrita de ficheiros CSV.


def carregar_termos(csv_path: str) -> dict:
    """
    Lê um ficheiro CSV que pode ter 2 ou 3 colunas:

    - 2 colunas: origem, alvo  (ex: BR, PT)
    - 3 colunas: variante1, variante2, alvo (ex: UK, US, Oxford)

    Devolve um dicionário com a estrutura:
    {
        'origem': ['origem1', 'origem2'],  # lista de variantes originais (ex: ['uk','us'])
        'alvo': 'nome_do_dialeto_alvo',    # string com nome do dialeto alvo (ex: 'oxford')
        'termos': { variante: termo_alvo, ... }  # dicionário com mapeamento
    }

    :param csv_path: Caminho para o ficheiro CSV.
    :return: Dicionário com meta-info e termos.
    """
    termos = {}
    meta_origem = []
    meta_alvo = ""

    if not os.path.exists(csv_path):
        print(f"[AVISO] Ficheiro {csv_path} não encontrado. A usar base de dados vazia.")
        return {'origem': [], 'alvo': '', 'termos': {}}

    with open(csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        linhas = list(reader)

        if not linhas:
            print(f"[AVISO] Ficheiro {csv_path} está vazio.")
            return {'origem': [], 'alvo': '', 'termos': {}}

        # Detectar o número de colunas
        n_colunas = len(linhas[0])

        if n_colunas == 2:
            # Simples: origem → alvo
            meta_origem = ['origem']
            meta_alvo = 'alvo'
            for linha in linhas:
                if len(linha) < 2:
                    continue
                origem, alvo = linha[0].strip().lower(), linha[1].strip()
                termos[origem] = alvo

        elif n_colunas == 3:
            # 3 colunas: variante1, variante2, termo_alvo
            # Considera que primeira e segunda são variantes origem,
            # terceira é o termo alvo (dialeto alvo)
            meta_origem = ['var1', 'var2']
            meta_alvo = 'alvo'
            for linha in linhas:
                if len(linha) < 3:
                    continue
                var1, var2, alvo = linha[0].strip().lower(), linha[1].strip().lower(), linha[2].strip()
                termos[var1] = alvo
                termos[var2] = alvo
        else:
            print(f"[AVISO] CSV com número inesperado de colunas: {n_colunas}. Deve ter 2 ou 3 colunas.")
            return {'origem': [], 'alvo': '', 'termos': {}}

    return {'origem': meta_origem, 'alvo': meta_alvo, 'termos': termos}

# Este trabalho foi realizado no âmbito da Unidade Curricular de Linguagens e Paradigmas de Programação
# do Curso de Engenharia Informática, pelos alunos:
# -> Miguel Magalhães, Nº 2021103166;
# -> Gabriel Fernando, Nº 2021101890.

# © 2025 Miguel Magalhães & Gabriel Fernando. Todos os direitos reservados.
# Este código é parte de um projeto académico e não deve ser utilizado para fins comerciais.
