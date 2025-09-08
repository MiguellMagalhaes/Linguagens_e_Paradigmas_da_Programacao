# Exercício 3 - Aprovação de Alunos

## Descrição

Este exercício determina a situação de um aluno (Aprovado, Exame ou Reprovado) baseada na sua assiduidade (em percentagem) e nota do teste (0 a 20), seguindo a seguinte tabela de decisão:

- **Assiduidade < 75%** → Reprovado
- **Assiduidade ≥ 75% e nota ≤ 5** → Reprovado
- **Assiduidade ≥ 75% e 5 < nota < 9,5** → Exame
- **Assiduidade ≥ 75% e nota ≥ 9,5** → Aprovado

## Ficheiro

- `aprovação_do_aluno.py`

## Conceitos Utilizados

- Validação de dados de entrada
- Estruturas condicionais aninhadas
- Tratamento de erros com `exit()`
- Operadores lógicos (`and`, `or`)
- Conversão de tipos (`float()`)

## Como Executar

1. Navegue até à pasta do exercício:
   ```bash
   cd "Exercício 3"
   ```

2. Execute o programa:
   ```bash
   python aprovação_do_aluno.py
   ```

3. Introduza os valores solicitados:
   - Assiduidade (0 a 100%)
   - Nota do teste (0 a 20)

## Exemplo de Execução

```
Introduz a assiduidade do aluno (0 a 100 %): 85
Introduz a nota do teste (0 a 20): 12
Situação do aluno: Aprovado
```

## Validação de Dados

O programa inclui validação para garantir que:
- A assiduidade está entre 0% e 100%
- A nota está entre 0 e 20

Se os valores estiverem fora destes intervalos, o programa termina com uma mensagem de erro.

## Lógica do Programa

1. Solicita assiduidade e nota do aluno
2. Valida se os valores estão nos intervalos permitidos
3. Aplica a lógica de decisão:
   - Primeiro verifica se assiduidade < 75% → Reprovado
   - Se assiduidade ≥ 75%, avalia a nota:
     - Nota ≤ 5 → Reprovado
     - 5 < nota < 9,5 → Exame
     - Nota ≥ 9,5 → Aprovado
4. Apresenta a situação final

## Casos de Teste

- Assiduidade 60%, Nota 15 → Reprovado (assiduidade baixa)
- Assiduidade 80%, Nota 3 → Reprovado (nota muito baixa)
- Assiduidade 90%, Nota 8 → Exame (nota intermédia)
- Assiduidade 95%, Nota 15 → Aprovado (critérios cumpridos)

## Autor

**Miguel Magalhães**  
Nº 2021103166  
ISPGAYA
