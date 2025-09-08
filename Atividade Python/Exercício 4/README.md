# Exercício 4 - Comparação de Pessoas

## Descrição

Este exercício regista o nome, altura e peso de duas pessoas e identifica qual é a mais pesada e qual é a mais alta. Utiliza um ciclo `for` para recolher os dados de ambas as pessoas e mantém registo dos valores máximos.

## Ficheiro

- `mais_alta_e_pesada.py`

## Conceitos Utilizados

- Ciclos (`for` com `range()`)
- Variáveis para armazenar valores máximos
- Estruturas condicionais para comparações
- Entrada e conversão de dados (`float()`)
- Formatação de saída

## Como Executar

1. Navegue até à pasta do exercício:
   ```bash
   cd "Exercício 4"
   ```

2. Execute o programa:
   ```bash
   python mais_alta_e_pesada.py
   ```

3. Introduza os dados para cada pessoa:
   - Nome
   - Altura (em metros)
   - Peso (em kg)

## Exemplo de Execução

```
Introduz o nome da pessoa 1: Ana
Introduz a altura (em metros): 1.65
Introduz o peso (em kg): 58
Introduz o nome da pessoa 2: João
Introduz a altura (em metros): 1.80
Introduz o peso (em kg): 75
A pessoa mais pesada é: João
A pessoa mais alta é: João
```

## Lógica do Programa

1. Inicializa variáveis para armazenar:
   - Nome e peso da pessoa mais pesada
   - Nome e altura da pessoa mais alta
2. Executa um ciclo `for` duas vezes (uma para cada pessoa)
3. Para cada pessoa:
   - Solicita nome, altura e peso
   - Compara o peso com o peso máximo atual
   - Compara a altura com a altura máxima atual
   - Atualiza os valores máximos se necessário
4. Apresenta os resultados finais

## Estrutura de Dados

O programa utiliza variáveis simples para armazenar:
- `nome_mais_pesada` e `peso_mais_alto`
- `nome_mais_alta` e `altura_mais_alta`

## Casos de Teste

**Caso 1:**
- Pessoa 1: Ana, 1.65m, 58kg
- Pessoa 2: João, 1.80m, 75kg
- Resultado: João é mais pesado e mais alto

**Caso 2:**
- Pessoa 1: Maria, 1.70m, 65kg
- Pessoa 2: Pedro, 1.60m, 70kg
- Resultado: Pedro é mais pesado, Maria é mais alta

## Autor

**Miguel Magalhães**  
Nº 2021103166  
ISPGAYA
