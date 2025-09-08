def verificar_dados_alunos():
    """
    Solicita o nome de um aluno e as suas notas, verificando se as notas são válidas (entre 0 e 20).
    Armazena os dados num dicionário e exibe as informações verificadas.
    """
    nome_aluno = input("Digite o nome do aluno: ")  # Pede ao utilizador o nome do aluno
    notas = []  # Cria uma lista para armazenar as notas

    while True:  # Inicia um ciclo infinito para inserir várias notas
        try:
            nota_str = input("Digite uma nota do aluno (ou 'fim' para terminar): ")  # Pede ao utilizador uma nota
            if nota_str.lower() == 'fim':  # Se o utilizador escrever 'fim', termina o ciclo
                break
            nota = float(nota_str)  # Tenta converter a nota para float
            if 0 <= nota <= 20:  # Verifica se a nota está no intervalo permitido
                notas.append(nota)  # Adiciona a nota à lista
            else:
                print("Erro: A nota deve estar entre 0 e 20.")  # Mensagem de erro se a nota for inválida
        except ValueError:
            print("Erro: Por favor, digite um número válido para a nota.")  # Mensagem de erro se não for possível converter para número

    dados_aluno = {
        'nome': nome_aluno,  # Guarda o nome do aluno
        'notas': notas       # Guarda a lista de notas
    }

    print("\nDados do aluno verificados:")
    print(f"Nome: {dados_aluno['nome']}")  # Mostra o nome do aluno
    if dados_aluno['notas']:  # Se existirem notas inseridas
        print(f"Notas: {', '.join(map(str, dados_aluno['notas']))}")  # Mostra a lista de notas
        media = sum(dados_aluno['notas']) / len(dados_aluno['notas'])  # Calcula a média das notas
        print(f"Média: {media:.2f}")  # Mostra a média com duas casas decimais
    else:
        print("Nenhuma nota foi inserida para este aluno.")  # Mensagem caso não tenham sido inseridas notas

# Executar o algoritmo
verificar_dados_alunos()