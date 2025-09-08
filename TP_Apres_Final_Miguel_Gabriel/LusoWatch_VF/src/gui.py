# Resumo: Interface gráfica em Tkinter que permite ao utilizador seleccionar um
# ficheiro CSV com termos BR‑PT, escolher um ficheiro de entrada (txt/pdf/docx),
# escolher um local de saída (.txt) e processar o texto: detecta vocabulário
# brasileiro e anota‑o com a sugestão em português europeu, gravando o resultado.

# Importações
import tkinter as tk  # Importa o módulo Tkinter (apelidado 'tk') para a GUI.
from tkinter import filedialog, messagebox  # Importa diálogos de ficheiro e caixas de mensagem.
from tkinter import ttk  # Importa ttk para Combobox.
import os  # Módulo do sistema de ficheiros para verificar caminhos.

# Imports dos teus módulos existentes
# (Ajusta o caminho se necessário, dependendo da tua organização)
from file_handler import (  # Importa funções utilitárias do módulo 'file_handler':
    ler_texto_txt,  # - leitura de ficheiros .txt
    ler_texto_pdf,  # - leitura de ficheiros .pdf
    ler_texto_docx,  # - leitura de ficheiros .docx
    escrever_texto_txt,  # - escrita de texto para .txt
)
from detector import detetar_e_anotar  # Importa a função que faz a deteção/anotação.
from substitutor import substituir_termos  # Importa a função que faz a substituição direta.
from utils import carregar_termos  # Importa função que lê o CSV e devolve dicionário BR→PT.
import re  # Para extrair sugestões do texto anotado


def criar_janela():  # Função que constrói e apresenta a interface gráfica.
    # Criação da janela principal
    janela = tk.Tk()  # Instancia o objecto root de Tkinter.
    janela.title("Detetor")  # Define o título da janela.

    # Variáveis para armazenar caminhos dos ficheiros
    csv_var = tk.StringVar()  # Guarda o caminho do CSV.
    entrada_var = tk.StringVar()  # Guarda o caminho do ficheiro de entrada.
    saida_var = tk.StringVar()  # Guarda o caminho do ficheiro de saída.

    # Variável para modo de processamento
    modo_var = tk.StringVar(value="substituir")  # Modo padrão: substituição

    # Caminho para os CSVs automáticos
    csvs_padrao = {
        "🇵🇹Português Europeu": "../data/csv/termos_ptpt.csv",
        "🇧🇷Português do Brasil": "../data/csv/termos_ptbr.csv",
        "🇺🇸Inglês (EUA)": "../data/csv/termos_enus.csv",
        "🇬🇧Inglês (Reino Unido)": "../data/csv/termos_enuk.csv",
    }

    csv_manual_override = [False]  # flag mutável para saber se o utilizador escolheu um CSV manualmente

    # Funções para os botões "Procurar Ficheiro"
    def selecionar_csv():  # Abre diálogo para escolher o CSV de termos.
        caminho = filedialog.askopenfilename(  # Diálogo de abertura de ficheiro.
            title="Selecione o CSV de termos",
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
        )
        if caminho:  # Se o utilizador escolheu um ficheiro:
            csv_var.set(caminho)  # Actualiza a variável correspondente.
            csv_manual_override[0] = True  # Marca que foi escolhido manualmente

    def selecionar_entrada():  # Abre diálogo para escolher o ficheiro de entrada.
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

    def selecionar_saida():  # Diálogo para indicar onde guardar o resultado.
        caminho = filedialog.asksaveasfilename(
            title="Selecione o ficheiro de saída (txt)",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if caminho:
            saida_var.set(caminho)

    def mostrar_janela_confirmacao(sugestoes, conteudo_original, termos, caminho_saida):
        """
        Mostra uma janela com as sugestões de substituição e permite ao utilizador
        confirmar ou cancelar a operação.

        :param sugestoes: Lista de tuplos (termo_original, sugestao)
        :param conteudo_original: Texto original a ser processado
        :param termos: Dicionário de termos para substituição
        :param caminho_saida: Caminho do ficheiro de saída
        """
        # Janela de confirmação
        janela_confirmacao = tk.Toplevel(janela)
        janela_confirmacao.title("Confirmar Substituições")
        janela_confirmacao.geometry("600x400")
        janela_confirmacao.grab_set()  # Torna a janela modal

        # Frame para título e descrição
        frame_topo = tk.Frame(janela_confirmacao)
        frame_topo.pack(fill=tk.X, padx=10, pady=10)

        # Título
        label_titulo = tk.Label(frame_topo, text="Substituições Encontradas", font=("Arial", 12, "bold"))
        label_titulo.pack(anchor=tk.W)

        # Descrição
        label_descricao = tk.Label(frame_topo,
                                   text=f"Foram encontradas {len(sugestoes)} sugestões de substituição.")
        label_descricao.pack(anchor=tk.W, pady=(5, 0))

        # Frame para a lista de substituições
        frame_lista = tk.Frame(janela_confirmacao)
        frame_lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Scrollbar
        scrollbar = tk.Scrollbar(frame_lista)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Listbox com as substituições no formato "termo_original → sugestão"
        listbox = tk.Listbox(frame_lista, width=80, height=15, font=("Monospace", 10))
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Configurar scrollbar
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

        # Adicionar itens à lista
        for original, sugestao in sugestoes:
            listbox.insert(tk.END, f"{original} → {sugestao}")

        # Frame para botões
        frame_botoes = tk.Frame(janela_confirmacao)
        frame_botoes.pack(fill=tk.X, padx=10, pady=10)

        # Função para substituir todos os termos e salvar
        def confirmar_substituicoes():
            resultado, num_alteracoes = substituir_termos(conteudo_original, termos)
            escrever_texto_txt(caminho_saida, resultado)
            janela_confirmacao.destroy()
            messagebox.showinfo("Sucesso",
                                f"Processo concluído. Ocorreram {num_alteracoes} substituições.\nFicheiro guardado em:\n{caminho_saida}")

        # Função para cancelar
        def cancelar_operacao():
            janela_confirmacao.destroy()
            messagebox.showinfo("Operação Cancelada", "Nenhuma alteração foi realizada.")

        # Botão para confirmar todas as substituições
        btn_confirmar = ttk.Button(frame_botoes, text="Confirmar Todas as Substituições",
                                   command=confirmar_substituicoes)
        btn_confirmar.pack(side=tk.LEFT, padx=5)

        # Botão para cancelar
        btn_cancelar = ttk.Button(frame_botoes, text="Cancelar",
                                  command=cancelar_operacao)
        btn_cancelar.pack(side=tk.RIGHT, padx=5)

        # Função para substituir todos os termos e salvar
        def confirmar_substituicoes():
            resultado, num_alteracoes = substituir_termos(conteudo_original, termos)
            escrever_texto_txt(caminho_saida, resultado)
            janela_confirmacao.destroy()
            messagebox.showinfo("Sucesso",
                                f"Processo concluído. Ocorreram {num_alteracoes} substituições.\nFicheiro guardado em:\n{caminho_saida}")

        # Função para cancelar
        def cancelar_operacao():
            janela_confirmacao.destroy()
            messagebox.showinfo("Operação Cancelada", "Nenhuma alteração foi realizada.")





    def extrair_sugestoes(texto_anotado):
        """
        Extrai as sugestões de um texto anotado pela função detetar_e_anotar.
        Retorna uma lista de tuplos (termo_original, sugestao).

        :param texto_anotado: O texto com anotações "[sug: termo]"
        :return: Lista de tuplos (termo_original, sugestao)
        """
        # Padrão regex para encontrar termos anotados: palavra + [sug: sugestão]
        padrao = r'(\b\w+\b) \[sug: (\w+)\]'
        matches = re.findall(padrao, texto_anotado)
        return matches

    def processar():
        """
        Carrega o CSV de termos, lê o ficheiro de entrada (txt/pdf/docx),
        detecta os termos a substituir, mostra janela de confirmação e,
        se confirmado, realiza a substituição e escreve o resultado.
        """
        caminho_csv = csv_var.get().strip()  # Obtém e limpa espaços do caminho CSV.
        caminho_entrada = entrada_var.get().strip()  # Obtém caminho de entrada.
        caminho_saida = saida_var.get().strip()  # Obtém caminho de saída.
        modo = modo_var.get()  # Obtém o modo de processamento

        if not caminho_csv or not caminho_entrada or not caminho_saida:  # Verifica se algum campo está vazio.
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        if not os.path.exists(caminho_csv):  # Confirma existência do CSV.
            messagebox.showerror("Erro", f"CSV não encontrado:\n{caminho_csv}")
            return

        if not os.path.exists(caminho_entrada):  # Confirma existência do ficheiro de entrada.
            messagebox.showerror("Erro", f"Ficheiro de entrada não encontrado:\n{caminho_entrada}")
            return

        # Carrega o dicionário de termos
        dicionario = carregar_termos(caminho_csv)  # Lê o CSV e obtém dicionário completo

        # Extrai apenas os termos (chave 'termos' do dicionário)
        termos = dicionario.get('termos', {})

        if not termos:
            messagebox.showwarning("Aviso", "Nenhum termo encontrado no CSV ou formato inválido.")
            return

        # Identifica extensão do ficheiro de entrada
        _, ext = os.path.splitext(caminho_entrada)  # Separa nome e extensão.
        ext = ext.lower()  # Normaliza para minúsculas.

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

            # Verifica o modo selecionado
            if modo == "anotar":
                # No modo anotar, realizar a anotação diretamente e salvar o resultado
                texto_anotado, num_anotacoes = detetar_e_anotar(conteudo, termos)

                if num_anotacoes == 0:
                    messagebox.showinfo("Informação", "Nenhum termo para anotar foi encontrado no texto.")
                    return

                # Salva diretamente o texto anotado sem mostrar confirmação
                escrever_texto_txt(caminho_saida, texto_anotado)
                messagebox.showinfo("Sucesso",
                                    f"Texto anotado com {num_anotacoes} sugestões.\nFicheiro guardado em:\n{caminho_saida}")

            else:  # modo == "substituir"
                # Primeiro faz a anotação para identificar os termos
                texto_anotado, num_anotacoes = detetar_e_anotar(conteudo, termos)

                # Se não encontrou termos para substituir
                if num_anotacoes == 0:
                    messagebox.showinfo("Informação", "Nenhum termo para substituir foi encontrado no texto.")
                    return

                # Extrai as sugestões do texto anotado
                sugestoes = extrair_sugestoes(texto_anotado)

                # Mostra janela de confirmação com as sugestões
                mostrar_janela_confirmacao(sugestoes, conteudo, termos, caminho_saida)

        except Exception as e:  # Captura qualquer excepção inesperada.
            messagebox.showerror("Erro", f"Ocorreu um erro:\n{e}")

    # Layout (Labels, Entries e Botões)
    # CSV
    label_csv = tk.Label(janela, text="CSV de termos:")
    label_csv.grid(row=1, column=0, padx=5, pady=5, sticky="e")  # Posiciona etiqueta.

    entry_csv = tk.Entry(janela, textvariable=csv_var, width=50)
    entry_csv.grid(row=1, column=1, padx=5, pady=5)
    btn_csv = tk.Button(janela, text="Procurar", command=selecionar_csv)
    btn_csv.grid(row=1, column=2, padx=5, pady=5)

    # Dropdown para seleção da língua
    lingua_var = tk.StringVar()
    label_lingua = tk.Label(janela, text="Língua para análise:")
    label_lingua.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    combo_lingua = ttk.Combobox(janela, textvariable=lingua_var, state="readonly")
    combo_lingua['values'] = list(csvs_padrao.keys())
    combo_lingua.current(0)  # Seleciona o primeiro por defeito
    combo_lingua.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    def atualizar_csv_padrao(event=None):
        if csv_manual_override[0]:  # Se foi definido manualmente, não atualiza
            return

        lingua = lingua_var.get()
        if lingua in csvs_padrao:
            caminho_padrao = csvs_padrao[lingua]
            if os.path.exists(caminho_padrao):
                csv_var.set(caminho_padrao)
            else:
                csv_var.set("")  # Limpa se o ficheiro não existir
                messagebox.showwarning("Aviso", f"CSV padrão não encontrado para:\n{lingua}\n({caminho_padrao})")

    combo_lingua.bind("<<ComboboxSelected>>", atualizar_csv_padrao)

    # Ficheiro de entrada
    label_entrada = tk.Label(janela, text="Ficheiro de entrada:")
    label_entrada.grid(row=2, column=0, padx=5, pady=5, sticky="e")

    entry_entrada = tk.Entry(janela, textvariable=entrada_var, width=50)
    entry_entrada.grid(row=2, column=1, padx=5, pady=5)
    btn_entrada = tk.Button(janela, text="Procurar", command=selecionar_entrada)
    btn_entrada.grid(row=2, column=2, padx=5, pady=5)

    # Ficheiro de saída
    label_saida = tk.Label(janela, text="Ficheiro de saída:")
    label_saida.grid(row=3, column=0, padx=5, pady=5, sticky="e")

    entry_saida = tk.Entry(janela, textvariable=saida_var, width=50)
    entry_saida.grid(row=3, column=1, padx=5, pady=5)
    btn_saida = tk.Button(janela, text="Procurar", command=selecionar_saida)
    btn_saida.grid(row=3, column=2, padx=5, pady=5)

    # Radio buttons para modo de processamento
    frame_modo = tk.Frame(janela)
    frame_modo.grid(row=4, column=0, columnspan=3, pady=5)

    label_modo = tk.Label(frame_modo, text="Modo de processamento:")
    label_modo.pack(side=tk.LEFT, padx=5)

    radio_substituir = tk.Radiobutton(frame_modo, text="Substituir", variable=modo_var, value="substituir")
    radio_substituir.pack(side=tk.LEFT, padx=10)

    radio_anotar = tk.Radiobutton(frame_modo, text="Anotar [sug: ]", variable=modo_var, value="anotar")
    radio_anotar.pack(side=tk.LEFT, padx=10)

    # Botão "Processar"
    btn_processar = tk.Button(janela, text="Processar", command=processar)
    btn_processar.grid(row=5, column=0, columnspan=3, padx=5, pady=15)

    # Inicializa o CSV automático na carga da janela
    atualizar_csv_padrao()

    # Inicia o loop da interface
    janela.mainloop()  # Entra no ciclo de eventos da GUI.


if __name__ == "__main__":  # Executa apenas se o ficheiro for o programa principal.
    criar_janela()  # Cria e mostra a janela.

# Este trabalho foi realizado no âmbito da Unidade Curricular de Linguagens e Paradigmas de Programação
# do Curso de Engenharia Informática, pelos alunos:
# -> Miguel Magalhães, Nº 2021103166;
# -> Gabriel Fernando, Nº 2021101890.

# © 2025 Miguel Magalhães & Gabriel Fernando. Todos os direitos reservados.
# Este código é parte de um projeto académico e não deve ser utilizado para fins comerciais.
# Se estes termos forem violados iram ter que resolver as coisas com o nosso advogado Saul Goodman >:D