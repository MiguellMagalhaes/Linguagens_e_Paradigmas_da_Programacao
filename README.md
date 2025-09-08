# Linguagens e Paradigmas da Programação

Repositório completo de trabalhos, atividades e projetos desenvolvidos no âmbito da unidade curricular de Linguagens e Paradigmas da Programação do curso de Engenharia Informática. Este projeto documenta a evolução do conhecimento em programação, desde conceitos básicos até aplicações complexas de processamento de texto.

## 👨‍💻 Autores

**Miguel Magalhães** & **Gabriel Fernando**

ISPGAYA - Instituto Superior Politécnico Gaya

## 🎯 Objetivo Geral

Este repositório demonstra a progressão no domínio de diferentes linguagens de programação e paradigmas, desde exercícios fundamentais até projetos complexos de aplicação prática. O objetivo é mostrar a evolução das competências de programação através de implementações progressivamente mais sofisticadas.

## 📚 Estrutura Completa do Projeto

### 🐍 Atividade Python
**Localização**: `Atividade Python/`  
**Objetivo**: Aprender conceitos fundamentais de programação em Python através de exercícios práticos progressivos.

Esta secção contém 5 exercícios que demonstram a evolução do conhecimento em Python:

#### Exercício 1 - Conversão de Idade
- **Ficheiro**: `Exercício 1/Idade_anos_em_dias.py`
- **Conceitos**: Entrada de dados, operações matemáticas, formatação de saída
- **Como executar**:
  ```bash
  cd "Atividade Python/Exercício 1"
  python Idade_anos_em_dias.py
  ```
- **Descrição**: Converte idade expressa em anos, meses e dias para apenas dias (considerando 1 ano = 365 dias, 1 mês = 30 dias)

#### Exercício 2 - Categorização de Atletas
- **Ficheiro**: `Exercício 2/categoria_atleta.py`
- **Conceitos**: Estruturas condicionais (if/elif/else), operadores de comparação
- **Como executar**:
  ```bash
  cd "Atividade Python/Exercício 2"
  python categoria_atleta.py
  ```
- **Descrição**: Determina a categoria de um atleta baseada na idade (Infantil, Iniciado, Juvenil, Junior, Sénior)

#### Exercício 3 - Sistema de Aprovação
- **Ficheiro**: `Exercício 3/aprovação_do_aluno.py`
- **Conceitos**: Validação de dados, estruturas condicionais aninhadas, tratamento de erros
- **Como executar**:
  ```bash
  cd "Atividade Python/Exercício 3"
  python aprovação_do_aluno.py
  ```
- **Descrição**: Determina a situação de um aluno (Aprovado/Exame/Reprovado) baseada na assiduidade e nota

#### Exercício 4 - Comparação de Pessoas
- **Ficheiro**: `Exercício 4/mais_alta_e_pesada.py`
- **Conceitos**: Ciclos (for), estruturas de dados, comparações
- **Como executar**:
  ```bash
  cd "Atividade Python/Exercício 4"
  python mais_alta_e_pesada.py
  ```
- **Descrição**: Regista dados de duas pessoas e identifica a mais alta e a mais pesada

#### Exercício 5 - Zodíaco Chinês
- **Ficheiro**: `Exercício 5/Zodiaco_Chinês.py`
- **Conceitos**: Listas, operações matemáticas (módulo), indexação
- **Como executar**:
  ```bash
  cd "Atividade Python/Exercício 5"
  python Zodiaco_Chinês.py
  ```
- **Descrição**: Determina o signo do zodíaco chinês baseado no ano de nascimento

### 🔄 Atividades Comparativas
**Localização**: `Atividades/`  
**Objetivo**: Comparar implementações do mesmo algoritmo em diferentes linguagens de programação.

#### Atividade 1 - Python vs Java
- **Ficheiros**: 
  - `Atividade 1/Código/actcomentado.py` (Python)
  - `Atividade 1/Código/teste.java` (Java)
- **Relatório**: `Atividade 1/Relatório/Atividade Python vs Java_MiguelMagalhaes.pdf`
- **Como executar**:
  ```bash
  # Python
  cd "Atividades/Atividade 1/Código"
  python actcomentado.py
  
  # Java
  cd "Atividades/Atividade 1/Código"
  javac teste.java
  java teste
  ```
- **Descrição**: Implementação do mesmo algoritmo (gestão de notas de alunos) em Python e Java, com análise comparativa das diferenças entre as linguagens

### 📚 LPP Library
**Localização**: `LPP Library/`  
**Objetivo**: Biblioteca de códigos auxiliares e utilitários desenvolvidos durante o curso.

- **Estrutura**: `27.03/27.03.py`
- **Descrição**: Repositório de funções auxiliares, exemplos de implementação e códigos de demonstração
- **Como utilizar**: Importar funções necessárias nos projetos principais

### 🏆 Trabalho Prático Intermédio
**Localização**: `TP_Apres_Inter_Miguel_Gabriel/`  
**Projeto**: **LusoWatch** - Detetor de Português do Brasil  
**Objetivo**: Desenvolver uma aplicação de processamento de texto para detetar e converter vocabulário brasileiro.

#### Estrutura do Projeto
```
LusoWatch/
├── data/
│   └── ptbr.csv                 # Base de dados BR→PT
├── src/
│   ├── main.py                  # Script principal
│   ├── detector.py              # Módulo de deteção
│   ├── file_handler.py          # Manipulação de ficheiros
│   ├── gui.py                   # Interface gráfica
│   ├── substitutor.py           # Substituição de termos
│   └── utils.py                 # Funções utilitárias
├── tests/                       # Testes unitários
└── requirements.txt
```

#### Como Executar
```bash
cd "TP_Apres_Inter_Miguel_Gabriel/LusoWatch"
pip install -r requirements.txt
cd src
python main.py
```

#### Funcionalidades
- Deteção de vocabulário brasileiro em documentos
- Anotação com sugestões em português europeu
- Suporte para ficheiros TXT, PDF e DOCX
- Interface de linha de comandos

### 🎯 Trabalho Prático Final
**Localização**: `TP_Apres_Final_Miguel_Gabriel/`  
**Projeto**: **LusoWatch VF** - Detetor Multi-dialectos  
**Objetivo**: Evolução do projeto intermédio com suporte para múltiplos dialectos e idiomas.

#### Estrutura do Projeto
```
LusoWatch_VF/
├── data/
│   ├── csv/
│   │   ├── termos_enuk.csv      # Inglês UK
│   │   ├── termos_enus.csv      # Inglês US
│   │   ├── termos_ptbr.csv      # Português BR
│   │   └── termos_ptpt.csv      # Português PT
│   └── Exemplos/                # Ficheiros de exemplo
├── src/
│   ├── main.py                  # Script principal
│   ├── detector.py              # Módulo de deteção
│   ├── file_handler.py          # Manipulação de ficheiros
│   ├── gui.py                   # Interface gráfica
│   ├── substitutor.py           # Substituição de termos
│   └── utils.py                 # Funções utilitárias
├── tests/                       # Testes unitários
└── requirements.txt
```

#### Como Executar
```bash
cd "TP_Apres_Final_Miguel_Gabriel/LusoWatch_VF"
pip install -r requirements.txt
cd src
python main.py
```

#### Funcionalidades Avançadas
- **Multi-dialectos**: Português BR→PT e Inglês UK/US
- **Multi-formato**: TXT, PDF, DOCX
- **Deteção e Anotação**: Identifica termos e sugere alternativas
- **Substituição Direta**: Converte automaticamente o texto
- **Interface Intuitiva**: Linha de comandos com opções claras

#### Exemplo de Utilização
```bash
python main.py
# Escolha o idioma: 1 (Português) ou 2 (Inglês)
# Introduza o caminho do CSV de termos
# Introduza o ficheiro de entrada
# Introduza o ficheiro de saída
```

## 🛠️ Tecnologias e Dependências

### Linguagens de Programação
- **Python 3.x** - Linguagem principal para todos os projetos
- **Java** - Comparação de linguagens (Atividade 1)

### Bibliotecas Python
- `python-docx` - Processamento de documentos Word
- `PyPDF2` - Processamento de ficheiros PDF
- `lxml` - Processamento XML (dependência do python-docx)

### Instalação de Dependências
```bash
# Para os trabalhos práticos
pip install python-docx PyPDF2 lxml

# Ou instalar a partir do requirements.txt
pip install -r requirements.txt
```

## 📈 Evolução e Progressão

### Fase 1: Fundamentos (Atividade Python)
- Aprendizagem de conceitos básicos
- Estruturas de controlo
- Manipulação de dados
- Algoritmos simples

### Fase 2: Comparação (Atividades)
- Análise de diferentes linguagens
- Implementação do mesmo algoritmo em Python e Java
- Compreensão das diferenças entre paradigmas

### Fase 3: Aplicação Prática (Trabalhos Práticos)
- Desenvolvimento de aplicações complexas
- Processamento de ficheiros
- Arquitetura modular
- Testes unitários

### Fase 4: Refinamento (Versão Final)
- Melhoria de funcionalidades
- Suporte multi-dialectos
- Interface mais robusta
- Código mais limpo e organizado

## 🎓 Objetivos de Aprendizagem Alcançados

### Conceitos Fundamentais
- ✅ Estruturas de dados (listas, dicionários, arrays)
- ✅ Estruturas de controlo (if/else, for/while)
- ✅ Funções e modularização
- ✅ Tratamento de exceções
- ✅ Validação de dados

### Paradigmas de Programação
- ✅ Programação imperativa
- ✅ Programação orientada a objetos
- ✅ Comparação entre linguagens
- ✅ Escolha adequada de ferramentas

### Desenvolvimento de Software
- ✅ Arquitetura modular
- ✅ Separação de responsabilidades
- ✅ Testes unitários
- ✅ Documentação de código
- ✅ Gestão de dependências

### Aplicações Práticas
- ✅ Processamento de texto
- ✅ Manipulação de ficheiros
- ✅ Interfaces de utilizador
- ✅ Aplicações de linha de comandos

## 🚀 Como Começar

### Para Estudantes
1. **Comece pelos exercícios básicos**: Navegue até `Atividade Python/` e execute os exercícios por ordem
2. **Compare linguagens**: Explore `Atividades/` para ver diferenças entre Python e Java
3. **Analise projetos complexos**: Estude os trabalhos práticos para ver aplicações reais

### Para Desenvolvedores
1. **Clone o repositório**
2. **Instale as dependências**: `pip install -r requirements.txt`
3. **Execute os projetos**: Siga as instruções específicas de cada pasta
4. **Explore o código**: Cada ficheiro está bem comentado e documentado

## 📁 Navegação Rápida

| Pasta | Tipo | Dificuldade | Tempo Estimado |
|-------|------|-------------|----------------|
| `Atividade Python/` | Exercícios | Básico | 2-3 horas |
| `Atividades/` | Comparação | Intermédio | 1-2 horas |
| `LPP Library/` | Utilitários | Variável | Conforme necessidade |
| `TP_Apres_Inter_Miguel_Gabriel/` | Projeto | Avançado | 4-6 horas |
| `TP_Apres_Final_Miguel_Gabriel/` | Projeto | Avançado | 6-8 horas |

## 📄 Documentação

Cada pasta contém o seu próprio README.md com:
- Descrição detalhada do projeto/atividade
- Instruções de execução passo a passo
- Exemplos de utilização
- Estrutura de ficheiros
- Casos de teste

## 📊 Estatísticas do Projeto

- **Total de exercícios**: 5
- **Linguagens utilizadas**: 2 (Python, Java)
- **Projetos principais**: 2 (LusoWatch, LusoWatch VF)
- **Ficheiros de código**: 15+
- **Linhas de código**: 1000+
- **Formato de ficheiros suportados**: 3 (TXT, PDF, DOCX)

## 🤝 Contribuições

Este é um projeto académico desenvolvido no âmbito de uma unidade curricular. O código está disponível para fins educativos e de estudo.

## 📜 Licença

© 2025 Miguel Magalhães. Todos os direitos reservados.  
Este código é parte de um projeto académico e não deve ser utilizado para fins comerciais.

---

*Trabalhos realizados no âmbito da Unidade Curricular de Linguagens e Paradigmas da Programação*  
*ISPGAYA - Curso de Engenharia Informática*  
*Demonstração da evolução das competências de programação através de implementações progressivas*