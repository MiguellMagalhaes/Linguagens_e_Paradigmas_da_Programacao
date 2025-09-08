
# Resumo: Conjunto de utilitários para leitura de ficheiros de texto em vários
# formatos (.txt, .pdf, .docx) e para escrita de textos em ficheiro .txt.
# Cada função valida a existência do ficheiro de entrada, extrai o conteúdo
# apropriado e devolve‑o como string; a última função grava texto num caminho
# especifico.

# Importações
import os       # Módulo da biblioteca padrão que fornece funções para interagir com o sistema de ficheiros.
import PyPDF2   # Biblioteca externa usada para ler e extrair texto de ficheiros PDF.
import docx     # Biblioteca 'python-docx' (importada como docx) para manipular documentos .docx.

def ler_texto_txt(caminho_txt: str) -> str:  # Define função que recebe o caminho de um .txt e devolve o texto contido.
    """
    Lê o conteúdo integral de um ficheiro .txt e retorna como string.
    
    :param caminho_txt: Caminho para o ficheiro .txt
    :return: Conteúdo do ficheiro como string
    """  # Docstring a documentar finalidade, parâmetro e valor de retorno.
    if not os.path.exists(caminho_txt):  # Verifica se o ficheiro existe; caso contrário, lança erro explícito.
        raise FileNotFoundError(f"Ficheiro {caminho_txt} não encontrado.")

    with open(caminho_txt, 'r', encoding='utf-8') as fin:  # Abre o ficheiro em modo leitura de texto, com codificação UTF‑8.
        conteudo = fin.read()                              # Lê todo o conteúdo para memória.
    return conteudo                                        # Devolve a string lida.

def ler_texto_pdf(caminho_pdf: str) -> str:  # Função que extrai texto de um PDF completo.
    """
    Extrai o texto de um ficheiro PDF, página a página, e devolve como string.
    Utiliza a biblioteca PyPDF2.
    
    :param caminho_pdf: Caminho para o ficheiro PDF
    :return: Conteúdo textual do PDF
    """
    if not os.path.exists(caminho_pdf):  # Confirma se o PDF existe.
        raise FileNotFoundError(f"Ficheiro {caminho_pdf} não encontrado.")

    texto_completo = []                         # Lista que agregará o texto de todas as páginas.
    with open(caminho_pdf, 'rb') as f:          # Abre o ficheiro em modo binário de leitura.
        leitor_pdf = PyPDF2.PdfReader(f)        # Cria instância do leitor PyPDF2.
        num_paginas = len(leitor_pdf.pages)     # Obtém o número total de páginas.
        for i in range(num_paginas):            # Itera índice de cada página.
            pagina = leitor_pdf.pages[i]        # Seleciona a página actual.
            texto_pagina = pagina.extract_text()# Extrai o texto daquela página.
            if texto_pagina:                    # Se existir texto (pode haver páginas só com imagens):
                texto_completo.append(texto_pagina)  # Adiciona texto à lista.
    
    return "\n".join(texto_completo)            # Junta todo o texto separado por quebras de linha e devolve.

def ler_texto_docx(caminho_docx: str) -> str:  # Função que lê ficheiros Word (.docx).
    """
    Extrai o texto de um ficheiro .docx, parágrafo a parágrafo, e devolve como string.
    Utiliza a biblioteca python-docx.
    
    :param caminho_docx: Caminho para o ficheiro .docx
    :return: Conteúdo textual do DOCX
    """
    if not os.path.exists(caminho_docx):  # Verifica se o ficheiro existe.
        raise FileNotFoundError(f"Ficheiro {caminho_docx} não encontrado.")

    doc = docx.Document(caminho_docx)                 # Abre o documento Word.
    paragrafos = [p.text for p in doc.paragraphs]     # Compreensão de lista para obter texto de cada parágrafo.
    return "\n".join(paragrafos)                      # Devolve texto completo separado por quebras de linha.

def escrever_texto_txt(caminho_saida: str, conteudo: str):  # Função que grava string num ficheiro .txt.
    """
    Escreve o conteúdo no ficheiro de texto especificado.
    
    :param caminho_saida: Caminho do ficheiro .txt onde gravar o resultado
    :param conteudo: String com o texto a gravar
    """
    with open(caminho_saida, 'w', encoding='utf-8') as fout:  # Abre/Cria ficheiro em modo escrita, codificação UTF‑8.
        fout.write(conteudo)                                  # Escreve o conteúdo e fecha automaticamente.


# Este trabalho foi realizado no âmbito da Unidade Curricular de Linguagens e Paradigmas de Programação
# do Curso de Engenharia Informática, pelos alunos:
# -> Miguel Magalhães, Nº 2021103166;
# -> Gabriel Fernando, Nº 2021101890.

# © 2025 Miguel Magalhães & Gabriel Fernando. Todos os direitos reservados.
# Este código é parte de um projeto académico e não deve ser utilizado para fins comerciais.