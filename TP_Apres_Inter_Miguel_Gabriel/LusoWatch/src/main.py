
# Resumo: Script de linha de comandos que solicita ao utilizador o caminho para
# um CSV de termos BR→PT, para um ficheiro de entrada (txt/pdf/docx) e para
# um ficheiro de saída (.txt). Lê o ficheiro indicado, detecta vocabulário
# brasileiro e anota‑o com sugestões em português europeu, gravando o resultado.

# Importações
import sys                                      # Módulo da bibliotec    padrão para saída forçada e argumentos de CLI.
import os                                       # Módulo para operações com sistema de ficheiros e caminhos.

from file_handler import (                      # Importa funções auxiliares para ler/escrever ficheiros.
    ler_texto_txt,                              #  - leitura de ficheiros .txt
    ler_texto_pdf,                              #  - leitura de ficheiros .pdf
    ler_texto_docx,                             #  - leitura de ficheiros .docx
    escrever_texto_txt,                         #  - escrita de texto em ficheiros .txt
)
from detector import detetar_e_anotar           # Função que detecta e anota termos brasileiros no texto.
# from substitutor import substituir_termos     # (Comentado) Função opcional para substituir termos por completo.
from utils import carregar_termos               # Função que lê o CSV de termos BR→PT e devolve um dicionário.

def main():                                     # Função principal que orquestra todo o fluxo.
    print("=== DETETOR DE PORTUGUÊS DO BRASIL ===")  # Mensagem de cabeçalho.

    # 1. Caminhos (podes substituir por argparse, etc.)
    caminho_csv = input("Caminho para o CSV de termos (ex: data/termos_br_pt.csv): ").strip()  # Pede caminho do CSV.
    caminho_entrada = input("Caminho do ficheiro de entrada (txt/pdf/docx): ").strip()         # Pede caminho de entrada.
    caminho_saida = input("Caminho do ficheiro de saída (será .txt): ").strip()                # Pede caminho de saída.

    # 2. Carrega termos BR->PT
    termos_br_pt = carregar_termos(caminho_csv)  # Lê o CSV e devolve dict BR→PT.
    if not termos_br_pt:                         # Se o dicionário estiver vazio ou não existir:
        print("[AVISO] Base de dados de termos está vazia ou não foi encontrada.")

    # 3. Identifica extensão do ficheiro de entrada
    _, ext = os.path.splitext(caminho_entrada)   # Divide nome e extensão do ficheiro.
    ext = ext.lower()                            # Converte extensão para minúsculas.

    # 4. Lê o ficheiro
    if ext == ".txt":                            # Escolhe função de leitura consoante a extensão.
        conteudo = ler_texto_txt(caminho_entrada)
    elif ext == ".pdf":
        conteudo = ler_texto_pdf(caminho_entrada)
    elif ext == ".docx":
        conteudo = ler_texto_docx(caminho_entrada)
    else:                                        # Extensão desconhecida → erro e termina o programa.
        print(f"[ERRO] Extensão de ficheiro não suportada: {ext}")
        sys.exit(1)

    # 5. Aplica deteção (neste caso, anotação)
    resultado = detetar_e_anotar(conteudo, termos_br_pt)  # Anota termos brasileiros detectados.
    # Se quisesses substituição total, faria:
    # resultado = substituir_termos(conteudo, termos_br_pt)

    # 6. Escreve resultado para um ficheiro .txt
    escrever_texto_txt(caminho_saida, resultado)          # Guarda o texto processado no caminho indicado.

    print(f"[INFO] Processamento concluído. Verifica o ficheiro '{caminho_saida}'.")  # Mensagem final.

if __name__ == "__main__":  # Garante que main() só é executado quando o script é corrido directamente.
    main()                  # Invoca a função principal.


# Este trabalho foi realizado no âmbito da Unidade Curricular de Linguagens e Paradigmas de Programação
# do Curso de Engenharia Informática, pelos alunos:
# -> Miguel Magalhães, Nº 2021103166;
# -> Gabriel Fernando, Nº 2021101890.

# © 2025 Miguel Magalhães & Gabriel Fernando. Todos os direitos reservados.
# Este código é parte de um projeto académico e não deve ser utilizado para fins comerciais.