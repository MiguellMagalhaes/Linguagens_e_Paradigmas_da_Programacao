
# Resumo: Esta função percorre o texto recebido, deteta expressões do português do Brasil
# presentes no dicionário de correspondências e devolve o texto anotado com sugestões
# equivalentes em português de Portugal, preservando a capitalização. Utiliza expressões
# regulares para efectuar a detecção de forma insensível a maiúsculas e minúsculas.

# Importações
import re  # Importa o módulo 're', que oferece suporte a expressões regulares.

def detetar_e_anotar(texto: str, termos_br_pt: dict) -> str:  # Define a função que recebe um texto e um dicionário BR→PT, devolvendo o texto anotado.
    """
    Percorre 'texto', deteta expressões brasileiras que constem no dicionário 'termos_br_pt'
    e retorna uma versão do texto com as sugestões anotadas (ex: "você [sug: tu]").
    
    :param texto: Conteúdo de texto a analisar
    :param termos_br_pt: Dicionário mapeando expressões BR->PT
    :return: Texto anotado com sugestões
    """  # Docstring que descreve o propósito, parâmetros e valor de retorno da função.

    # Ordenamos as chaves por tamanho decrescente para apanhar primeiro as expressões compostas.
    chaves_ordenadas = sorted(termos_br_pt.keys(), key=len, reverse=True)  # Cria lista de chaves do dicionário, ordenada da mais longa para a mais curta.

    texto_anotado = texto  # Variável que guardará o texto já com anotações; começa igual ao texto original.

    for br_expr in chaves_ordenadas:  # Percorre cada expressão brasileira da lista ordenada.
        pt_expr = termos_br_pt[br_expr]  # Obtém a expressão correspondente em português europeu.

        # Cria expressão regex que ignora maiúsculas/minúsculas.
        # \b → limite de palavra (útil para termos simples; pode falhar em expressões compostas com pontuação).
        pattern = re.compile(rf"\b{re.escape(br_expr)}\b", re.IGNORECASE)  # Compila o padrão regex com \b e flag IGNORECASE.

        def substituidor(match):  # Função callback usada por re.sub para construir a anotação.
            original = match.group(0)  # Termo brasileiro encontrado no texto.
            # Se a primeira letra for maiúscula, capitalizamos a sugestão:
            if original[0].isupper():  # Verifica se o termo começa por maiúscula.
                pt_expr_capitalizada = pt_expr.capitalize()  # Capitaliza a sugestão portuguesa, mantendo coerência com o original.
                return f"{original} [sug: {pt_expr_capitalizada}]"  # Devolve termo original + sugestão capitalizada.
            else:
                return f"{original} [sug: {pt_expr}]"  # Devolve termo original + sugestão em minúsculas.

        texto_anotado = pattern.sub(substituidor, texto_anotado)  # Substitui cada ocorrência pelo termo anotado.

    return texto_anotado  # Devolve o texto final, contendo todas as anotações aplicadas.


# Este trabalho foi realizado no âmbito da Unidade Curricular de Linguagens e Paradigmas de Programação
# do Curso de Engenharia Informática, pelos alunos:
# -> Miguel Magalhães, Nº 2021103166;
# -> Gabriel Fernando, Nº 2021101890.


# © 2025 Miguel Magalhães & Gabriel Fernando. Todos os direitos reservados.
# Este código é parte de um projeto académico e não deve ser utilizado para fins comerciais.