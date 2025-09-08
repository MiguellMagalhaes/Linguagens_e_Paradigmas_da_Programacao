# Exercício 1 - Conversão de Idade

## Descrição

Este exercício converte a idade de uma pessoa expressa em anos, meses e dias para apenas dias. O programa solicita ao utilizador os valores de anos, meses e dias, e calcula o total de dias considerando:
- 1 ano = 365 dias
- 1 mês = 30 dias

## Ficheiro

- `Idade_anos_em_dias.py`

## Conceitos Utilizados

- Entrada de dados com `input()`
- Conversão de tipos (`int()`)
- Operações matemáticas básicas
- Formatação de saída com f-strings

## Como Executar

1. Navegue até à pasta do exercício:
   ```bash
   cd "Exercício 1"
   ```

2. Execute o programa:
   ```bash
   python Idade_anos_em_dias.py
   ```

3. Introduza os valores solicitados:
   - Número de anos completos
   - Número de meses adicionais
   - Número de dias adicionais

## Exemplo de Execução

```
Quantos anos completos? 25
E quantos meses adicionais? 6
E finalmente quantos dias adicionais? 15
A tua idade em dias é: 9405 dia(s).
```

## Lógica do Programa

1. Solicita ao utilizador os anos, meses e dias
2. Converte anos para dias: `anos × 365`
3. Converte meses para dias: `meses × 30`
4. Soma todos os valores: `dias_totais = dias_de_anos + dias_de_meses + dias`
5. Apresenta o resultado final

## Autor

**Miguel Magalhães**  
Nº 2021103166  
ISPGAYA
