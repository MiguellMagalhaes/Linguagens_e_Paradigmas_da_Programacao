# Resumo: Função que percorre um texto e substitui directamente cada expressão
# do português do Brasil (BR) ou variantes (UK/US) pela respectiva equivalência
# em português europeu ou dialeto alvo, de acordo com o dicionário fornecido.
# Preserva a capitalização inicial do termo, utilizando expressões regulares
# com detecção insensível a maiúsculas/minúsculas.

import re  # Importa o módulo 're', que disponibiliza operações com expressões regulares.


def substituir_termos(texto: str, termos: dict) -> tuple:
    """
    Substitui termos conforme o dicionário { variante: termo_alvo } diretamente no texto.

    :param texto: Conteúdo a analisar
    :param termos: Dicionário { variante : termo_alvo }
    :return: Tupla (texto com substituições realizadas, número de substituições)
    """
    chaves_ordenadas = sorted(termos.keys(), key=len,
                              reverse=True)  # Ordena por tamanho decrescente para pegar expressões compostas primeiro.
    texto_substituido = texto
    total_substituicoes = 0  # Contador de substituições realizadas

    for termo_original in chaves_ordenadas:
        termo_alvo = termos[termo_original]

        pattern = re.compile(rf"\b{re.escape(termo_original)}\b", re.IGNORECASE)  # Palavra exata, case-insensitive

        # Conta ocorrências antes da substituição
        ocorrencias = len(pattern.findall(texto_substituido))
        total_substituicoes += ocorrencias

        def substituidor(match):
            original = match.group(0)
            # Preserva capitalização inicial
            if original[0].isupper():
                return termo_alvo.capitalize()
            else:
                return termo_alvo

        texto_substituido = pattern.sub(substituidor, texto_substituido)

    return texto_substituido, total_substituicoes

# Este trabalho foi realizado no âmbito da Unidade Curricular de Linguagens e Paradigmas de Programação
# do Curso de Engenharia Informática, pelos alunos:
# -> Miguel Magalhães, Nº 2021103166;
# -> Gabriel Fernando, Nº 2021101890.

# © 2025 Miguel Magalhães & Gabriel Fernando. Todos os direitos reservados.
# Este código é parte de um projeto académico e não deve ser utilizado para fins comerciais.