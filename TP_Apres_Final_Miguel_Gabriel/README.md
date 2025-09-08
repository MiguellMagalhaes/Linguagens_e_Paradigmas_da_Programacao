# TP_Apres_Final_Miguel_Gabriel

## LusoWatch VF - Detetor de Português do Brasil e Outros Dialectos

Este é o trabalho prático final desenvolvido no âmbito da unidade curricular de Linguagens e Paradigmas da Programação. O projeto consiste numa aplicação que detecta e converte texto de português brasileiro para português europeu, com suporte adicional para outros dialectos.

## Descrição do Projeto

O **LusoWatch VF** é uma ferramenta de processamento de texto que:

- Detecta vocabulário brasileiro em documentos
- Anota o texto com sugestões em português europeu
- Suporta múltiplos formatos de ficheiro (TXT, PDF, DOCX)
- Inclui suporte para dialectos de inglês (UK/US/Oxford)
- Permite substituição direta de termos

## Estrutura do Projeto

```
LusoWatch_VF/
├── data/
│   ├── csv/
│   │   ├── termos_enuk.csv      # Termos inglês UK
│   │   ├── termos_enus.csv      # Termos inglês US
│   │   ├── termos_ptbr.csv      # Termos português BR
│   │   └── termos_ptpt.csv      # Termos português PT
│   └── Exemplos/
│       ├── diagnostico_anotado.txt
│       └── diagnostico_substituido.txt
├── src/
│   ├── main.py                  # Script principal
│   ├── detector.py              # Módulo de deteção
│   ├── file_handler.py          # Manipulação de ficheiros
│   ├── gui.py                   # Interface gráfica
│   ├── substitutor.py           # Substituição de termos
│   └── utils.py                 # Funções utilitárias
├── tests/
│   ├── test_detector.py
│   └── test_file_handler.py
├── requirements.txt
└── README.md
```

## Funcionalidades

### 1. Deteção e Anotação
- Identifica termos brasileiros no texto
- Anota com sugestões em português europeu
- Preserva o texto original com anotações

### 2. Substituição Direta
- Substitui automaticamente os termos detectados
- Gera versão convertida do documento

### 3. Suporte Multi-formato
- **TXT**: Ficheiros de texto simples
- **PDF**: Documentos PDF (requer PyPDF2)
- **DOCX**: Documentos Word (requer python-docx)

### 4. Multi-dialectos
- Português BR → PT
- Inglês UK/US → Dialecto alvo

## Instalação

1. Clone ou descarregue o projeto
2. Navegue até à pasta do projeto:
   ```bash
   cd LusoWatch_VF
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Como Executar

### Modo Linha de Comandos

```bash
cd src
python main.py
```

O programa irá solicitar:
1. Escolha do idioma (1 - Português, 2 - Inglês)
2. Caminho para o CSV de termos
3. Caminho do ficheiro de entrada
4. Caminho do ficheiro de saída

### Exemplo de Utilização

```bash
python main.py
```

```
=== DETETOR DE PORTUGUÊS DO BRASIL E OUTROS DIALECTOS ===
Idiomas disponíveis:
  1 - Português (BR → PT)
  2 - Inglês (UK/US → Dialecto alvo)
Escolha o idioma (1 ou 2): 1
Caminho para o CSV de termos (ex: data/termos.csv): data/csv/termos_ptbr.csv
Caminho do ficheiro de entrada (txt/pdf/docx): data/Exemplos/diagnostico.txt
Caminho do ficheiro de saída (será .txt): output/diagnostico_processado.txt
```

## Dependências

- `python-docx` - Para processamento de ficheiros DOCX
- `PyPDF2` - Para processamento de ficheiros PDF
- `lxml` - Para processamento XML (dependência do python-docx)

## Estrutura dos Ficheiros CSV

Os ficheiros CSV contêm os termos a serem convertidos no formato:
```csv
termo_origem,termo_destino
```

## Testes

Execute os testes unitários:
```bash
cd tests
python -m pytest test_detector.py
python -m pytest test_file_handler.py
```

## Relatório

Consulte o ficheiro `Relatório/Relatório_LusoWatch_VF.pdf` para informações detalhadas sobre:
- Arquitetura do sistema
- Metodologia de desenvolvimento
- Análise de resultados
- Conclusões

## Autores

**Miguel Magalhães** - Nº 2021103166  
**Gabriel Fernando** - Nº 2021101890

ISPGAYA - Curso de Engenharia Informática

## Licença

© 2025 Miguel Magalhães & Gabriel Fernando. Todos os direitos reservados.  
Este código é parte de um projeto académico e não deve ser utilizado para fins comerciais.

---

*Trabalho realizado no âmbito da Unidade Curricular de Linguagens e Paradigmas da Programação*
