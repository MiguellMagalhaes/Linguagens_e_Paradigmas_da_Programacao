Instituto Superior Politécnico de GAYA  
Licenciatura em Engenharia Informática – 2024/2025  
Unidade Curricular: Linguagens e Paradigmas de Programação  

Alunos:  
  • Miguel Magalhães (2021103166)  
  • Gabriel Fernando  (2021101890)  

Docente: Sr. Prof. José Arnaud  
Data: 25 de Maio de 2025  

========================================  
README.md – Instruções de Instalação e Utilização  
========================================  

## 1. Descrição do projeto  
LusoWatch 2.0 é uma ferramenta em Python que:  
* Detecta termos **PT-BR** em textos **PT-PT** e termos **EN-US** em textos **EN-UK/Oxford**.  
* Permite **anotar** ocorrências – `ônibus [sug: autocarro]` – ou **substituir** diretamente.  
* Suporta os formatos **TXT · PDF · DOCX** de entrada.  
* Disponibiliza duas interfaces:  
  – **CLI** interativa (`src/main.py`)  
  – **GUI** Tkinter (`src/gui.py`) com _dropdown_ de idioma e lista de confirmações.  
* Inclui script `src/diagnostico.py` para autoverificação e _benchmark_.  

## 2. Pré-requisitos  
* Python 3.10 ou superior.  
* Sistemas suportados: Windows · macOS · Linux.  
* Tkinter disponível (`sudo apt install python3-tk`, Debian/Ubuntu).  
* `pip` funcional.  

## 3. Configuração do ambiente  
1. **Criar e ativar** ambiente virtual (opcional, recomendado):  
   ```bash
   python -m venv venv
   # Linux / macOS
   source venv/bin/activate
   # Windows PowerShell
   .\venv\Scripts\Activate.ps1
   ```  
2. **Instalar** dependências:  
   ```bash
   pip install -r requirements.txt
   ```  
   > Requisitos mínimos: `PyPDF2 ≥ 3.0.0 · python-docx ≥ 0.8.10 · pytest ≥ 7.0.0`

## 4. Estrutura de pastas  
```
LusoWatch_VF/
├── data/
│   └── csv/
│       ├── termos_ptpt.csv   # PT-BR → PT-PT
│       ├── termos_enus.csv   # EN-US → EN-UK
│       └── termos_enuk.csv   # EN-UK → EN-US (debug)
├── src/
│   ├── detector.py           # Anotação
│   ├── substitutor.py        # Substituição
│   ├── file_handler.py       # I/O TXT|PDF|DOCX
│   ├── utils.py              # Loader CSV
│   ├── gui.py                # Interface gráfica
│   ├── main.py               # Interface CLI
│   └── diagnostico.py        # Auto-teste + benchmark
├── tests/
│   ├── test_detector.py
│   └── test_file_handler.py
├── requirements.txt
└── README.md
```

## 5. Utilização – CLI  
```bash
python src/main.py
```  
* Selecionar idioma (1=PT, 2=EN).  
* Indicar caminhos para CSV, ficheiro de entrada e de saída.  
* Escolher modo **Substituir** ou **Anotar** quando solicitado.  

## 6. Utilização – GUI  
```bash
python src/gui.py
```  
* Escolher a língua no _dropdown_.  
* Definir CSV, ficheiro de entrada e ficheiro de saída.  
* Selecionar **Substituir** ou **Anotar** e clicar **Processar**.  
* Confirmar as substituições apresentadas → ficheiro gravado.  

## 7. Script de diagnóstico  
Corre verificação completa e grava `diagnostico_substituido.txt` + `diagnostico_anotado.txt`.  
```bash
python src/diagnostico.py
```  

## 8. Testes unitários  
```bash
pytest --cov=src
```  
Cobertura esperada ≥ 85 %. O relatório HTML é gerado em `htmlcov/` se `pytest-html` estiver instalado.  

## 9. Boas práticas e cuidados  
* Editar apenas os CSV da pasta `data/csv/`, mantendo o número de colunas.  
* Garantir que todos os ficheiros de texto estão em **UTF-8**.  
* PDFs constituídos por imagens requerem integração futura de OCR.  
* Não incluir `venv/`, `__pycache__/` ou ficheiros temporários no .rar de entrega.  

## 10. Atualização do requirements.txt  
```bash
pip freeze > requirements.txt
```  

## 11. Empacotamento para entrega  
* Criar `TP_Apres_Final_Miguel_Gabriel.rar` com:  
  * **Relatório/Relatório_LusoWatch_VF.pdf**  
  * **LusoWatch_VF/** (estrutura apresentada no ponto 4).  

## 12. Contacto e suporte  
→ Miguel Magalhães · <ispg2021103166@ispgaya.pt>  
→ Gabriel Fernando  · <ispg2021101890@ispgaya.pt>  

© 2025 Miguel Magalhães & Gabriel Fernando — Todos os direitos reservados.  


