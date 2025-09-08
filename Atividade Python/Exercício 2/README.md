# Exercício 2 - Categorização de Atletas

## Descrição

Este exercício determina a categoria de um atleta baseada na sua idade, seguindo a seguinte tabela de categorias:

- **Infantil**: 5 a 7 anos
- **Iniciado**: 8 a 10 anos
- **Juvenil**: 11 a 13 anos
- **Junior**: 14 a 17 anos
- **Sénior**: 18 anos ou mais
- **Sem categoria definida**: Menos de 5 anos

## Ficheiro

- `categoria_atleta.py`

## Conceitos Utilizados

- Estruturas condicionais (`if`, `elif`, `else`)
- Operadores de comparação (`<=`, `>=`)
- Entrada e conversão de dados
- Formatação de saída

## Como Executar

1. Navegue até à pasta do exercício:
   ```bash
   cd "Exercício 2"
   ```

2. Execute o programa:
   ```bash
   python categoria_atleta.py
   ```

3. Introduza a idade do atleta quando solicitado

## Exemplo de Execução

```
Introduz a idade do atleta (em anos completos): 15
O atleta enquadra-se na categoria: Junior
```

## Lógica do Programa

1. Solicita a idade do atleta
2. Verifica a idade usando estruturas condicionais:
   - Se 5 ≤ idade ≤ 7 → Infantil
   - Se 8 ≤ idade ≤ 10 → Iniciado
   - Se 11 ≤ idade ≤ 13 → Juvenil
   - Se 14 ≤ idade ≤ 17 → Junior
   - Se idade ≥ 18 → Sénior
   - Caso contrário → Sem categoria definida
3. Apresenta a categoria correspondente

## Casos de Teste

- Idade 6 → Infantil
- Idade 9 → Iniciado
- Idade 12 → Juvenil
- Idade 16 → Junior
- Idade 20 → Sénior
- Idade 3 → Sem categoria definida

## Autor

**Miguel Magalhães**  
Nº 2021103166  
ISPGAYA
