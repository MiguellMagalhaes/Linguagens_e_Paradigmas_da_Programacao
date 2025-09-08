Instituto Superior Politécnico de GAYA
Licenciatura em Engenharia Informática – 2024/2025  
Unidade Curricular: Linguagens e Paradigmas de Programação  

Alunos:  
  • Miguel Magalhães (2021103166)  
  • Gabriel Fernando  (2021101890)  

Docente: Sr. Prof. José Arnaud  
Data: 21 de Abril de 2025  

========================================  
README.txt – Instruções de Instalação e Utilização  
========================================  

1. Descrição do Projeto  
   ---------------------  
   LusoWatch é uma ferramenta Python que:  
     • Deteta automaticamente termos do Português do Brasil num texto PT‑PT.  
     • Anota cada ocorrência com a forma europeia sugerida ([sug: …]).  
     • Permite, opcionalmente, substituição direta BR→PT.  
     • Suporta formatos de entrada: TXT, PDF e DOCX.  
     • Oferece duas interfaces:  
       – CLI (src/main.py)  
       – GUI Tkinter (src/gui.py)  

2. Pré‑requisitos  
   --------------  
   • Python 3.10 ou superior instalado.  
   • Sistema operativo: Windows, macOS ou Linux.  
   • Biblioteca Tkinter (no Ubuntu/Debian: `sudo apt install python3‑tk`).  
   • Ferramenta `pip` disponível.  

3. Configuração do Ambiente  
   ------------------------  
   1. Criar e ativar ambiente virtual (opcional, mas recomendado):  
      ```bash
      python3 -m venv venv
      source venv/bin/activate     # Linux/macOS
      .\venv\Scripts\Activate.ps1  # Windows PowerShell
      ```  
   2. Instalar dependências:  
      ```bash
      pip install -r requirements.txt
      ```  
      *O ficheiro requirements.txt inclui, no mínimo:*  
      ```
      PyPDF2>=3.0.0
      python-docx>=0.8.10
      pytest>=7.0.0
      ```  

4. Estrutura de Pastas  
   -------------------  
   ├── data/  
   │     └── ptbr.csv        # Base de dados léxica BR→PT  
   ├── src/                  # Código‑fonte  
   │   ├── detector.py       # Núcleo de deteção/anotação  
   │   ├── substitutor.py    # Substituição BR→PT  
   │   ├── file_handler.py   # Leitura TXT, PDF, DOCX; escrita TXT  
   │   ├── utils.py          # Carregamento do CSV  
   │   ├── gui.py            # Interface gráfica (Tkinter)  
   │   └── main.py           # Interface de linha de comandos  
   ├── tests/                # Testes PyTest  
   │   ├── test_detector.py  
   │   └── test_file_handler.py  
   ├── requirements.txt      # Lista de dependências  
   └── README.txt            # Este ficheiro  

5. Utilização – CLI  
   ----------------  
   1. Certificar‑se de que o ambiente virtual está ativo (veja ponto 3).  
   2. Executar:  
      ```bash
      python src/main.py
      ```  
   3. Seguir as instruções:  
      • Indicar caminho para o CSV de termos (data/ptbr.csv).  
      • Indicar caminho do ficheiro de entrada (.txt/.pdf/.docx).  
      • Indicar caminho do ficheiro de saída (.txt).  
   4. No final, receberá mensagem de sucesso ou erro.  

6. Utilização – GUI  
   ----------------  
   1. Certificar‑se de que o ambiente virtual está ativo.  
   2. Executar:  
      ```bash
      python src/gui.py
      ```  
   3. Na janela:  
      • “CSV de termos” → botão «Procurar» → selecionar data/ptbr.csv.  
      • “Ficheiro de entrada” → selecionar .txt/.pdf/.docx.  
      • “Ficheiro de saída” → definir nome e localização do .txt de saída.  
      • Clicar «Processar».  
   4. Surgirá um alerta de sucesso ou mensagem de erro.  

7. Testes Unitários  
   ----------------  
   1. Com o ambiente ativo, executar:  
      ```bash
      pytest --cov
      ```  
   2. Verificar que a cobertura é, no mínimo, 85 %.  
   3. Se algum teste falhar, o log indicará o módulo e a linha de erro.  

8. Boas Práticas e Cuidados  
   ------------------------  
   • Não renomear o ficheiro data/ptbr.csv nem alterar as colunas.  
   • Ao editar ptbr.csv, manter o formato CSV com cabeçalho: `palavra_br,sugestao_pt`.  
   • Em textos muito longos, o processamento de PDF pode demorar até 3 s.  
   • Para suporte a PDFs digitalizados em imagem, será necessário integrar OCR adicional.  
   • Garantir sempre UTF‑8 nos ficheiros de texto para evitar erros de codificação.  

9. Geração do requirements.txt  
   ---------------------------  
   Se adicionar novas dependências, atualizar com:  
   ```bash
   pip freeze > requirements.txt

10.	Contacto e Suporte

Para dúvidas ou relatórios de erro:

-> Miguel Magalhães: ispg2021103166@ispgaya.pt
-> Gabriel Fernando: ispg2021101890@ispgaya.pt

© 2025 Miguel Magalhães & Gabriel Fernando. Todos os direitos reservados.