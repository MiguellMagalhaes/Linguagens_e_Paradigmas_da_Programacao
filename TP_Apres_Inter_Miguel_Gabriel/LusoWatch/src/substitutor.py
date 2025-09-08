
# Resumo: Função que percorre um texto e substitui directamente cada expressão
# do português do Brasil (BR) pela respectiva equivalência em português europeu
# (PT), de acordo com o dicionário fornecido. Preserva a capitalização inicial
# do termo, quando necessário, utilizando expressões regulares com detecção
# insensível a maiúsculas/minúsculas.

# Importações necessárias
import re  # Importa o módulo 're', que disponibiliza operações com expressões regulares.

def substituir_termos(texto: str, termos_br_pt: dict) -> str:  # Define a função que recebe o texto original e o dicionário de termos BR→PT.
    """
    Substitui termos BR pelas sugestões PT directamente no texto (sem anotar).
    
    :param texto: Conteúdo a analisar
    :param termos_br_pt: Dicionário {br_expr -> pt_expr}
    :return: Texto com substituições realizadas
    """
    chaves_ordenadas = sorted(termos_br_pt.keys(), key=len, reverse=True)  # Ordena as chaves por tamanho decrescente para capturar expressões compostas primeiro.
    texto_substituido = texto                                               # Variável que armazenará o texto processado; começa igual ao original.

    for br_expr in chaves_ordenadas:                                        # Itera cada expressão brasileira na lista ordenada.
        pt_expr = termos_br_pt[br_expr]                                     # Obtém a expressão equivalente em português europeu.

        pattern = re.compile(rf"\b{re.escape(br_expr)}\b", re.IGNORECASE)   # Compila regex que corresponde exactamente ao termo (delimitado por \b) sem diferenciar maiúsculas.

        def substituidor(match):                                            # Função interna usada como callback do re.sub.
            original = match.group(0)                                       # Texto capturado no match (termo original no texto).
            if original[0].isupper():                                       # Se o termo começar por maiúscula...
                return pt_expr.capitalize()                                 # ...capitaliza a versão portuguesa para manter coerência.
            else:
                return pt_expr                                              # Caso contrário, devolve a versão portuguesa tal como está.

        texto_substituido = pattern.sub(substituidor, texto_substituido)    # Substitui todas as ocorrências pelo termo português.

    return texto_substituido                                                # Devolve o texto final com todas as substituições aplicadas.


# Este trabalho foi realizado no âmbito da Unidade Curricular de Linguagens e Paradigmas de Programação
# do Curso de Engenharia Informática, pelos alunos:
# -> Miguel Magalhães, Nº 2021103166;
# -> Gabriel Fernando, Nº 2021101890.

# © 2025 Miguel Magalhães & Gabriel Fernando. Todos os direitos reservados.
# Este código é parte de um projeto académico e não deve ser utilizado para fins comerciais.