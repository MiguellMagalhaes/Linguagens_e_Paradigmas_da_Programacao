# TP_Apres_Inter_Miguel_Gabriel

## LusoWatch - Detetor de Português do Brasil

Este é o trabalho prático intermédio desenvolvido no âmbito da unidade curricular de Linguagens e Paradigmas da Programação. O projeto consiste numa aplicação que detecta e anota texto de português brasileiro, sugerindo equivalentes em português europeu.

## Descrição do Projeto

O **LusoWatch** é uma ferramenta de processamento de texto que:

- Detecta vocabulário brasileiro em documentos
- Anota o texto com sugestões em português europeu
- Suporta múltiplos formatos de ficheiro (TXT, PDF, DOCX)
- Foca especificamente na conversão BR → PT

## Estrutura do Projeto

```
LusoWatch/
├── data/
│   └── ptbr.csv                 # Base de dados de termos BR→PT
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

### 2. Substituição Direta (Opcional)
- Substitui automaticamente os termos detectados
- Gera versão convertida do documento

### 3. Suporte Multi-formato
- **TXT**: Ficheiros de texto simples
- **PDF**: Documentos PDF (requer PyPDF2)
- **DOCX**: Documentos Word (requer python-docx)

## Instalação

1. Clone ou descarregue o projeto
2. Navegue até à pasta do projeto:
   ```bash
   cd LusoWatch
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
1. Caminho para o CSV de termos BR→PT
2. Caminho do ficheiro de entrada
3. Caminho do ficheiro de saída

### Exemplo de Utilização

```bash
python main.py
```

```
=== DETETOR DE PORTUGUÊS DO BRASIL ===
Caminho para o CSV de termos (ex: data/termos_br_pt.csv): data/ptbr.csv
Caminho do ficheiro de entrada (txt/pdf/docx): documento.txt
Caminho do ficheiro de saída (será .txt): documento_anotado.txt
```

## Dependências

- `python-docx` - Para processamento de ficheiros DOCX
- `PyPDF2` - Para processamento de ficheiros PDF
- `lxml` - Para processamento XML (dependência do python-docx)

## Estrutura do Ficheiro CSV

O ficheiro `ptbr.csv` contém os termos a serem convertidos no formato:
```csv
termo_brasileiro,termo_portugues
```

Exemplo:
```csv
caminhão,camião
ônibus,autocarro
celular,telemóvel
```

## Testes

Execute os testes unitários:
```bash
cd tests
python -m pytest test_detector.py
python -m pytest test_file_handler.py
```

## Relatório

Consulte o ficheiro `Relatório/Relatório_LusoWatch.pdf` para informações detalhadas sobre:
- Arquitetura do sistema
- Metodologia de desenvolvimento
- Análise de resultados
- Conclusões

## Diferenças da Versão Final

Esta versão intermédia foca apenas na conversão de português brasileiro para português europeu, enquanto a versão final inclui suporte para múltiplos dialectos e idiomas.

## Autores

**Miguel Magalhães** - Nº 2021103166  
**Gabriel Fernando** - Nº 2021101890

ISPGAYA - Curso de Engenharia Informática

## Licença

© 2025 Miguel Magalhães & Gabriel Fernando. Todos os direitos reservados.  
Este código é parte de um projeto académico e não deve ser utilizado para fins comerciais.

---

*Trabalho realizado no âmbito da Unidade Curricular de Linguagens e Paradigmas da Programação*
