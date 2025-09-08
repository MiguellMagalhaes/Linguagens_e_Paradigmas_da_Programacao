# Exercício 5 - Zodíaco Chinês

## Descrição

Este exercício determina o signo do zodíaco chinês baseado no ano de nascimento. O zodíaco chinês é composto por 12 animais que se repetem num ciclo de 12 anos. O programa utiliza a operação módulo (`%`) para determinar o signo correspondente.

## Ficheiro

- `Zodiaco_Chinês.py`

## Conceitos Utilizados

- Listas e indexação
- Operação módulo (`%`)
- Entrada e conversão de dados (`int()`)
- Formatação de saída

## Tabela do Zodíaco Chinês

| Resto da divisão por 12 | Signo    |
|-------------------------|----------|
| 0                       | Macaco   |
| 1                       | Galo     |
| 2                       | Cão      |
| 3                       | Porco    |
| 4                       | Rato     |
| 5                       | Boi      |
| 6                       | Tigre    |
| 7                       | Coelho   |
| 8                       | Dragão   |
| 9                       | Serpente |
| 10                      | Cavalo   |
| 11                      | Carneiro |

## Como Executar

1. Navegue até à pasta do exercício:
   ```bash
   cd "Exercício 5"
   ```

2. Execute o programa:
   ```bash
   python Zodiaco_Chinês.py
   ```

3. Introduza o ano de nascimento quando solicitado

## Exemplo de Execução

```
Introduz o teu ano de nascimento (ex.: 1998): 1998
O teu signo do Zodíaco chinês é: Tigre
```

## Lógica do Programa

1. Cria uma lista com os 12 signos na ordem correta
2. Solicita o ano de nascimento ao utilizador
3. Calcula o resto da divisão do ano por 12: `resto = ano % 12`
4. Utiliza o resto como índice para aceder ao signo correspondente na lista
5. Apresenta o signo ao utilizador

## Exemplos de Cálculo

- **1998**: 1998 % 12 = 6 → Tigre
- **2000**: 2000 % 12 = 8 → Dragão
- **1990**: 1990 % 12 = 10 → Cavalo
- **1985**: 1985 % 12 = 5 → Boi

## Estrutura da Lista

```python
signos = [
    "Macaco",   # índice 0  → resto 0
    "Galo",     # índice 1  → resto 1
    "Cão",      # índice 2  → resto 2
    "Porco",    # índice 3  → resto 3
    "Rato",     # índice 4  → resto 4
    "Boi",      # índice 5  → resto 5
    "Tigre",    # índice 6  → resto 6
    "Coelho",   # índice 7  → resto 7
    "Dragão",   # índice 8  → resto 8
    "Serpente", # índice 9  → resto 9
    "Cavalo",   # índice 10 → resto 10
    "Carneiro"  # índice 11 → resto 11
]
```

## Autor

**Miguel Magalhães**  
Nº 2021103166  
ISPGAYA
