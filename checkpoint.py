oficinas = ("Criar e contar histórias", "Teatro: Luz, Câmera e Ação", "A língua de sinais", "Expressão artística", "Soletrando", "Leitura dramática", "O corpo fala", "O mundo da imaginação", "Leitura dinâmica", "Criando e recriando com emojis")
series = ("1ª serie", "2ª serie", "3ª serie", "4ª serie", "5ª serie")
# Alunos
rmAlunos = []
nomeAlunos = []
serieAlunos = []
cursoAlunos = []
# Variável de controle
cadastro = True

def menu():
    print("Evento Literário -- Colégio Nova Esperança")
    print("Favor selecionar uma opção abaixo, digitando o número correspondente:")

    if (cadastro):
        print("""1 - Cadastrar
2 - Inscrição
3 - Listar
4 - Sair""")
        selecao = int(input("Digite a opção desejada: "))
        while(selecao < 1 and selecao > 4):
            print("Opção inválida...")
            selecao = int(input("Digite a opção desejada: "))
        return selecao
    else:
        print("""1 - Cadastrar (NÃO SELECIONÁVEL)
2 - Inscrição
3 - Listar
4 - Sair""")
        selecao = int(input("Digite a opção desejada: "))
        while(selecao < 2 and selecao > 4):
            print("Opção inválida...")
            selecao = int(input("Digite a opção desejada: "))
        return selecao

while True:
    selecao = menu()
    
    # Cadastro
    if (selecao == 1):
        ...
    # Inscrição
    elif (selecao == 2):
        ...
    # Listagem
    elif (selecao == 3):
        ...
    else:
        break