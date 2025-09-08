
# Resumo: Teste unitário, usando PyTest, que verifica se a função
# detetar_e_anotar devolve exactamente o texto esperado quando lhe é
# fornecido um dicionário simples de termos BR→PT.

# Importações necessárias para o teste
import pytest                                  # Importa a framework PyTest para testes unitários.
from src.detector import detetar_e_anotar      # Importa a função a testar, localizada em src/detector.py.

def test_detetar_e_anotar_simples():           # Define um caso de teste.
    termos_br_pt = {                           # Dicionário de termos brasileiros e suas sugestões em PT‑PT.
        "você": "tu",
        "ônibus": "autocarro",
        "colocar": "pôr"
    }
    texto = "Você pode colocar seu bilhete no ônibus."    # Texto de entrada cujo vocabulário será detectado.
    esperado = (                                          # Resultado esperado após anotação.
        "Você [sug: Tu] pode colocar [sug: pôr] seu bilhete no ônibus [sug: autocarro]."
    )

    resultado = detetar_e_anotar(texto, termos_br_pt)     # Executa a função a testar.
    assert resultado == esperado                          # Verifica se o resultado coincide com o esperado.


# Este trabalho foi realizado no âmbito da Unidade Curricular de Linguagens e Paradigmas de Programação
# do Curso de Engenharia Informática, pelos alunos:
# -> Miguel Magalhães, Nº 2021103166;
# -> Gabriel Fernando, Nº 2021101890.

# © 2025 Miguel Magalhães & Gabriel Fernando. Todos os direitos reservados.
# Este código é parte de um projeto académico e não deve ser utilizado para fins comerciais.