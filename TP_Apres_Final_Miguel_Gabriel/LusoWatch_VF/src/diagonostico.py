# =======================================
# Resumo: Este script de diagnóstico percorre cada componente do sistema
# de deteção/substituição de variantes linguísticas. Importa os módulos-núcleo,
# verifica a existência dos ficheiros CSV e executa testes unitários rudimentares
# às funções de carregamento, deteção/anotação e substituição, produzindo
# mensagens de êxito ou falha. No final, cria um exemplo real e guarda os
# resultados em ficheiros de texto para inspeção posterior.
# =======================================

"""
Script de diagnóstico para verificar o funcionamento do detetor/substituidor de variantes linguísticas.
Este script testa cada componente do sistema para identificar possíveis falhas.
"""

# ------------------------------------------------------------------
# Importações
# ------------------------------------------------------------------
import os                 # Operações de sistema de ficheiros (existência de paths, etc.)
import sys                # Manipulação do caminho de pesquisa de módulos (sys.path).
from pathlib import Path   # Interface OO para caminhos (não utilizada mas importada por consistência).

# Adiciona o diretório atual ao caminho de importação
sys.path.append(os.getcwd())

# Tenta importar os módulos do programa
try:
    from detector import detetar_e_anotar              # Função de deteção + anotação
    from substitutor import substituir_termos          # Função de substituição direta
    from utils import carregar_termos                  # Utilitário de carregamento de CSV → dicionário
    from file_handler import ler_texto_txt, escrever_texto_txt  # IO de ficheiros de texto

    print("[✓] Módulos importados com sucesso.")
except ImportError as e:
    print(f"[✗] Erro ao importar módulos: {e}")
    sys.exit(1)


def verificar_arquivos_csv():
    """Verifica se os ficheiros CSV estão presentes e acessíveis."""
    csvs = [
        "csv/termos_ptpt.csv",
        "csv/termos_ptbr.csv",
        "csv/termos_enus.csv",
        "csv/termos_enuk.csv",
        "csv/termos_enox.csv"
    ]

    # Verifica também no directório data/csv
    csvs_data = [f"data/csv/{csv}" for csv in csvs]
    csvs_data_relativo = [f"../data/csv/{csv.split('/')[-1]}" for csv in csvs]

    todos_caminhos = csvs + csvs_data + csvs_data_relativo

    encontrados = []
    for csv_path in todos_caminhos:
        if os.path.exists(csv_path):
            encontrados.append(csv_path)
            print(f"[✓] CSV encontrado: {csv_path}")

    if not encontrados:
        print("[✗] Nenhum CSV encontrado. Verifique os caminhos.")
        return False

    return encontrados


def testar_carregamento_termos(caminhos_csv):
    """Testa o carregamento dos termos a partir dos CSVs."""
    for csv_path in caminhos_csv:
        print(f"\nTestando carregamento do CSV: {csv_path}")
        try:
            dicionario = carregar_termos(csv_path)

            # Verifica se o dicionário tem a estrutura esperada
            if 'termos' not in dicionario:
                print(f"[✗] Estrutura do dicionário incorreta para {csv_path}. Chaves: {dicionario.keys()}")
                continue

            # Verifica se há termos carregados
            num_termos = len(dicionario['termos'])
            if num_termos == 0:
                print(f"[✗] Nenhum termo carregado do CSV {csv_path}")
                continue

            print(f"[✓] {num_termos} termos carregados com sucesso do CSV {csv_path}")

            # Mostra alguns exemplos de termos carregados (até 5)
            print("Exemplos de termos carregados:")
            for i, (origem, alvo) in enumerate(list(dicionario['termos'].items())[:5]):
                print(f"    {origem} → {alvo}")

            return dicionario  # Retorna o primeiro dicionário carregado com sucesso

        except Exception as e:
            print(f"[✗] Erro ao carregar termos do CSV {csv_path}: {e}")

    return None


def testar_detecao_anotacao(dicionario):
    """Testa a função de deteção e anotação."""
    if not dicionario or 'termos' not in dicionario:
        print("[✗] Dicionário inválido para teste de deteção/anotação.")
        return False

    # Cria um texto de teste com alguns termos do dicionário
    termos_origem = list(dicionario['termos'].keys())
    if not termos_origem:
        print("[✗] Nenhum termo de origem para teste.")
        return False

    # Usa até 5 termos para o teste
    termos_teste = termos_origem[:5]
    texto_teste = f"Este é um texto de teste que contém os termos: {', '.join(termos_teste)}."
    print(f"\nTexto de teste para deteção: \"{texto_teste}\"")

    try:
        # Testa o detetor
        texto_anotado = detetar_e_anotar(texto_teste, dicionario['termos'])
        print(f"[✓] Texto anotado: \"{texto_anotado}\"")

        # Verifica se houve alterações no texto
        if texto_teste == texto_anotado:
            print("[✗] Nenhuma anotação foi adicionada ao texto.")
            return False

        return True
    except Exception as e:
        print(f"[✗] Erro ao testar deteção/anotação: {e}")
        return False


def testar_substituicao(dicionario):
    """Testa a função de substituição direta."""
    if not dicionario or 'termos' not in dicionario:
        print("[✗] Dicionário inválido para teste de substituição.")
        return False

    # Cria um texto de teste com alguns termos do dicionário
    termos_origem = list(dicionario['termos'].keys())
    if not termos_origem:
        print("[✗] Nenhum termo de origem para teste.")
        return False

    # Usa até 5 termos para o teste
    termos_teste = termos_origem[:5]
    texto_teste = f"Este é um texto de teste que contém os termos: {', '.join(termos_teste)}."
    print(f"\nTexto de teste para substituição: \"{texto_teste}\"")

    try:
        # Testa o substituidor
        texto_substituido = substituir_termos(texto_teste, dicionario['termos'])
        print(f"[✓] Texto substituído: \"{texto_substituido}\"")

        # Verifica se houve alterações no texto
        if texto_teste == texto_substituido:
            print("[✗] Nenhuma substituição foi realizada no texto.")
            return False

        return True
    except Exception as e:
        print(f"[✗] Erro ao testar substituição: {e}")
        return False


def criar_exemplo_real():
    """Cria um exemplo real usando um texto curto com termos conhecidos."""
    print("\n=== Teste com texto real ===")

    # Texto de exemplo com termos em PT-BR
    texto_exemplo = """
    Eu vou pegar o ônibus para a academia. Depois vou tomar um suco e comer um sanduíche.
    Mais tarde, preciso ir na rodoviária para encontrar meu amigo que está chegando de trem.
    Você pode me ajudar a encontrar meu celular? Acho que deixei no banheiro.
    """

    print(f"Texto de exemplo:\n{texto_exemplo}")

    # Carrega os termos PT-BR -> PT-PT
    csvs = verificar_arquivos_csv()
    if not csvs:
        print("[✗] Não foi possível encontrar os CSVs para o teste real.")
        return

    # Procura especificamente o CSV de termos_ptpt.csv
    csv_ptpt = None
    for csv in csvs:
        if "ptpt" in csv:
            csv_ptpt = csv
            break

    if not csv_ptpt:
        print("[✗] Não foi encontrado o CSV de termos PT-PT.")
        return

    print(f"Usando CSV: {csv_ptpt}")
    dicionario = carregar_termos(csv_ptpt)

    if 'termos' not in dicionario or not dicionario['termos']:
        print("[✗] Dicionário de termos vazio ou inválido.")
        return

    # Testa a substituição
    texto_substituido = substituir_termos(texto_exemplo, dicionario['termos'])
    print(f"\nTexto com substituições:\n{texto_substituido}")

    # Testa a anotação
    texto_anotado = detetar_e_anotar(texto_exemplo, dicionario['termos'])
    print(f"\nTexto com anotações:\n{texto_anotado}")

    # Guarda os resultados para inspeção
    try:
        escrever_texto_txt("diagnostico_substituido.txt", texto_substituido)
        escrever_texto_txt("diagnostico_anotado.txt", texto_anotado)
        print("[✓] Resultados guardados em 'diagnostico_substituido.txt' e 'diagnostico_anotado.txt'")
    except Exception as e:
        print(f"[✗] Erro ao guardar resultados: {e}")


def main():
    print("=== Diagnóstico do Detetor/Substituidor de Variantes Linguísticas ===")

    # Verifica a existência dos CSVs
    csvs = verificar_arquivos_csv()
    if not csvs:
        return

    # Testa o carregamento de termos
    dicionario = testar_carregamento_termos(csvs)
    if not dicionario:
        return

    # Testa a deteção/anotação
    testar_detecao_anotacao(dicionario)

    # Testa a substituição
    testar_substituicao(dicionario)

    # Cria um exemplo real
    criar_exemplo_real()


if __name__ == "__main__":
    main()

# ------------------------------------------------------------------
# Este trabalho foi realizado no âmbito da Unidade Curricular de
# Linguagens e Paradigmas de Programação, do Curso de Engenharia
# Informática, pelos alunos:
#   -> Miguel Magalhães, Nº 2021103166
#   -> Gabriel Fernando, Nº 2021101890
#
# © 2025 Miguel Magalhães & Gabriel Fernando. Todos os direitos reservados.
# Este código é parte de um projeto académico e não deve ser utilizado
# para fins comerciais.
# ------------------------------------------------------------------