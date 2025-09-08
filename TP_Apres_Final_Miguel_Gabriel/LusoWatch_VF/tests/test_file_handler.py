
# Resumo: Teste unitário (pytest) que verifica se as funções de escrita e leitura
# de ficheiros .txt funcionam correctamente: grava uma string num ficheiro
# temporário e confirma que o conteúdo lido coincide com o original.

# Importações
# -> Módulos padrão: os (para manipulação de caminhos de ficheiros).
# -> pytest: framework para testes automatizados.
# -> src.file_handler: módulo que contém as funções a testar (escrever_texto_txt e ler_texto_txt).
import os                                                  # Módulo padrão para operações com caminhos de ficheiros.
import pytest                                              # Framework PyTest para executar testes automatizados.
from src.file_handler import (                             # Importa as funções a testar a partir de src/file_handler.py
    escrever_texto_txt,                                    #  - função que escreve uma string num ficheiro .txt
    ler_texto_txt                                          #  - função que lê o conteúdo de um ficheiro .txt
)

def test_escrever_e_ler_texto_tmp(tmp_path):               # Função de teste; pytest injecta 'tmp_path' (directório temporário).
    # Cria ficheiro temporário
    caminho_tmp = os.path.join(tmp_path, "teste.txt")      # Constrói o caminho completo para 'teste.txt' dentro da pasta temporária.
    conteudo_original = "Olá mundo!"                       # Texto que será escrito no ficheiro.

    escrever_texto_txt(caminho_tmp, conteudo_original)     # Escreve o conteúdo original no ficheiro temporário.
    conteudo_lido = ler_texto_txt(caminho_tmp)             # Lê de volta o conteúdo do mesmo ficheiro.

    assert conteudo_lido == conteudo_original              # Verifica se o que foi lido é igual ao que foi escrito.


# Este trabalho foi realizado no âmbito da Unidade Curricular de Linguagens e Paradigmas de Programação
# do Curso de Engenharia Informática, pelos alunos:
# -> Miguel Magalhães, Nº 2021103166;
# -> Gabriel Fernando, Nº 2021101890.

# © 2025 Miguel Magalhães & Gabriel Fernando. Todos os direitos reservados.
# Este código é parte de um projeto académico e não deve ser utilizado para fins comerciais.