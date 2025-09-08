
# Resumo: Interface gráfica em Tkinter que permite ao utilizador seleccionar um
# ficheiro CSV com termos BR‑PT, escolher um ficheiro de entrada (txt/pdf/docx),
# escolher um local de saída (.txt) e processar o texto: detecta vocabulário
# brasileiro e anota‑o com a sugestão em português europeu, gravando o resultado.

# Importações
import tkinter as tk                                   # Importa o módulo Tkinter (apelidado 'tk') para a GUI.
from tkinter import filedialog, messagebox             # Importa diálogos de ficheiro e caixas de mensagem.
import os                                              # Módulo do sistema de ficheiros para verificar caminhos.

# Imports dos teus módulos existentes
# (Ajusta o caminho se necessário, dependendo da tua organização)
from file_handler import (                             # Importa funções utilitárias do módulo 'file_handler':
    ler_texto_txt,                                     #  - leitura de ficheiros .txt
    ler_texto_pdf,                                     #  - leitura de ficheiros .pdf
    ler_texto_docx,                                    #  - leitura de ficheiros .docx
    escrever_texto_txt,                                #  - escrita de texto para .txt
)
from detector import detetar_e_anotar                  # Importa a função que faz a detecção/anotação.
from utils import carregar_termos                      # Importa função que lê o CSV e devolve dicionário BR→PT.

def criar_janela():                                    # Função que constrói e apresenta a interface gráfica.
    # Criação da janela principal
    janela = tk.Tk()                                   # Instancia o objecto root de Tkinter.
    janela.title("Detetor de PT-BR → PT-PT")           # Define o título da janela.

    # Variáveis para armazenar caminhos dos ficheiros
    csv_var = tk.StringVar()                           # Guarda o caminho do CSV.
    entrada_var = tk.StringVar()                       # Guarda o caminho do ficheiro de entrada.
    saida_var = tk.StringVar()                         # Guarda o caminho do ficheiro de saída.

    # Funções para os botões "Procurar Ficheiro"
    def selecionar_csv():                              # Abre diálogo para escolher o CSV de termos.
        caminho = filedialog.askopenfilename(          # Diálogo de abertura de ficheiro.
            title="Selecione o CSV de termos",
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
        )
        if caminho:                                    # Se o utilizador escolheu um ficheiro:
            csv_var.set(caminho)                       # Actualiza a variável correspondente.

    def selecionar_entrada():                          # Abre diálogo para escolher o ficheiro de entrada.
        caminho = filedialog.askopenfilename(
            title="Selecione o ficheiro de entrada",
            filetypes=[
                ("Text Files", "*.txt"),
                ("PDF Files", "*.pdf"),
                ("Word docx", "*.docx"),
                ("All Files", "*.*")
            ]
        )
        if caminho:
            entrada_var.set(caminho)

    def selecionar_saida():                            # Diálogo para indicar onde guardar o resultado.
        caminho = filedialog.asksaveasfilename(
            title="Selecione o ficheiro de saída (txt)",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if caminho:
            saida_var.set(caminho)

    def processar():
        """
        Carrega o CSV de termos, lê o ficheiro de entrada (txt/pdf/docx),
        aplica a deteção/anotação, e escreve o resultado no ficheiro de saída.
        """
        caminho_csv = csv_var.get().strip()            # Obtém e limpa espaços do caminho CSV.
        caminho_entrada = entrada_var.get().strip()    # Obtém caminho de entrada.
        caminho_saida = saida_var.get().strip()        # Obtém caminho de saída.

        if not caminho_csv or not caminho_entrada or not caminho_saida:  # Verifica se algum campo está vazio.
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        if not os.path.exists(caminho_csv):            # Confirma existência do CSV.
            messagebox.showerror("Erro", f"CSV não encontrado:\n{caminho_csv}")
            return

        if not os.path.exists(caminho_entrada):        # Confirma existência do ficheiro de entrada.
            messagebox.showerror("Erro", f"Ficheiro de entrada não encontrado:\n{caminho_entrada}")
            return

        # Carrega o dicionário de termos
        termos_br_pt = carregar_termos(caminho_csv)    # Lê o CSV e obtém dict BR→PT.

        # Identifica extensão do ficheiro de entrada
        _, ext = os.path.splitext(caminho_entrada)     # Separa nome e extensão.
        ext = ext.lower()                              # Normaliza para minúsculas.

        try:
            # Lê o ficheiro consoante a extensão
            if ext == ".txt":
                conteudo = ler_texto_txt(caminho_entrada)
            elif ext == ".pdf":
                conteudo = ler_texto_pdf(caminho_entrada)
            elif ext == ".docx":
                conteudo = ler_texto_docx(caminho_entrada)
            else:
                messagebox.showerror("Erro", f"Extensão não suportada: {ext}")
                return

            # Anota termos (podes trocar para substituição total, se quiseres)
            resultado = detetar_e_anotar(conteudo, termos_br_pt)

            # Escreve saída
            escrever_texto_txt(caminho_saida, resultado)

            messagebox.showinfo("Sucesso", f"Processo concluído.\nFicheiro guardado em:\n{caminho_saida}")

        except Exception as e:                         # Captura qualquer excepção inesperada.
            messagebox.showerror("Erro", f"Ocorreu um erro:\n{e}")

    # Layout (Labels, Entries e Botões)
    # CSV
    label_csv = tk.Label(janela, text="CSV de termos:")
    label_csv.grid(row=0, column=0, padx=5, pady=5, sticky="e")  # Posiciona etiqueta.

    entry_csv = tk.Entry(janela, textvariable=csv_var, width=50)
    entry_csv.grid(row=0, column=1, padx=5, pady=5)
    btn_csv = tk.Button(janela, text="Procurar", command=selecionar_csv)
    btn_csv.grid(row=0, column=2, padx=5, pady=5)

    # Ficheiro de entrada
    label_entrada = tk.Label(janela, text="Ficheiro de entrada:")
    label_entrada.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    entry_entrada = tk.Entry(janela, textvariable=entrada_var, width=50)
    entry_entrada.grid(row=1, column=1, padx=5, pady=5)
    btn_entrada = tk.Button(janela, text="Procurar", command=selecionar_entrada)
    btn_entrada.grid(row=1, column=2, padx=5, pady=5)

    # Ficheiro de saída
    label_saida = tk.Label(janela, text="Ficheiro de saída:")
    label_saida.grid(row=2, column=0, padx=5, pady=5, sticky="e")

    entry_saida = tk.Entry(janela, textvariable=saida_var, width=50)
    entry_saida.grid(row=2, column=1, padx=5, pady=5)
    btn_saida = tk.Button(janela, text="Procurar", command=selecionar_saida)
    btn_saida.grid(row=2, column=2, padx=5, pady=5)

    # Botão "Processar"
    btn_processar = tk.Button(janela, text="Processar", command=processar)
    btn_processar.grid(row=3, column=0, columnspan=3, padx=5, pady=15)

    # Inicia o loop da interface
    janela.mainloop()                                  # Entra no ciclo de eventos da GUI.

if __name__ == "__main__":                             # Executa apenas se o ficheiro for o programa principal.
    criar_janela()                                     # Cria e mostra a janela.


# Este trabalho foi realizado no âmbito da Unidade Curricular de Linguagens e Paradigmas de Programação
# do Curso de Engenharia Informática, pelos alunos:
# -> Miguel Magalhães, Nº 2021103166;
# -> Gabriel Fernando, Nº 2021101890.

# © 2025 Miguel Magalhães & Gabriel Fernando. Todos os direitos reservados.
# Este código é parte de um projeto académico e não deve ser utilizado para fins comerciais.