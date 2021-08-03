oficinasMatutino = [["Criar e contar histórias", "A língua de sinais"],
["Criar e contar histórias", "Teatro: Luz, Câmera e Ação", "A língua de sinais"],
["Teatro: Luz, Câmera e Ação", "A língua de sinais", "Expressão Artística"],
["A língua de sinais", "Expressão Artística", "Soletrando"]]

oficinasVespertino = [["O mundo da imaginação", "Criando Emojis"],
["O corpo fala"], ["Leitura dramática"], ["Leitura dinâmica"]]


series = ("2ª serie", "3ª serie", "4ª serie", "5ª serie")
# Alunos
rmAlunos = []
serieAlunos = []
nomeAlunos = []

# Variável de controle
cadastro = True

def periodo(lista):
    periodo = input("Digite o período do aluno: ").strip()[0]
    while (periodo not in "MVT"):
        print("Período inválido... (Matutino ou Vespertino)")
        periodo = input("Digite o período do aluno: ").strip()[0]
        if (periodo == "M"):
            periodo = "Matutino"
            lista.append(periodo)
        elif (periodo == "V" or periodo == "T"):
            periodo = "Vespertino"
            lista.append(periodo)

def menu():
    print("Evento Literário -- Colégio Nova Esperança")
    print("Favor selecionar uma opção abaixo, digitando o número correspondente:")

    if (cadastro):
        print("""1 - Cadastrar
2 - Inscrição
3 - Listar
4 - Sair""")
        selecao = int(input("Digite a opção desejada: "))
        while(selecao < 1 or selecao > 4):
            print("Opção inválida...")
            selecao = int(input("Digite a opção desejada: "))
        return selecao
    else:
        print("""1 - Cadastrar (NÃO SELECIONÁVEL)
2 - Inscrição
3 - Listar
4 - Sair""")
        selecao = int(input("Digite a opção desejada: "))
        while(selecao < 2 or selecao > 4):
            print("Opção inválida...")
            selecao = int(input("Digite a opção desejada: "))
        return selecao

while True:
    selecao = menu()
    
    # Cadastro
    if (selecao == 1):
        while True:
            rm = input("Digite o rm do aluno: ").strip()
            while (rm in rmAlunos):
                print("rm já existe!")
                rm = input("Digite o rm do aluno: ").strip()
                if (rm == "0"):
                    cadastro = False
                    break 
            if (rm == "0"):
                cadastro = False
                break
            else:
                rmAlunos.append(rm)
                serie = int(input("Digite a serie do aluno: ").strip()[0])
                while (serie < 2 or serie > 5):
                    print("Série inválida!")
                    serie = int(input("Digite a serie do aluno: ").strip()[0])
                serieAlunos.append(series[serie-2])
                nome = input("Digite o nome do aluno: ").strip().capitalize()
                nomeAlunos.append(nome)
                
    # Inscrição
    elif (selecao == 2):
        rm = input("Insira o rm: ").strip()
        while (rm not in rmAlunos):
            print("Aluno não cadastrado... Favor procurar a coordenação do Fundamental I")
            rm = input("Insira o rm: ").strip()
        posRm = rmAlunos.index(rm)
        serieDoAluno = serieAlunos[posRm]
        posSerie = series.index(serieDoAluno)
        for c in oficinasMatutino:
            for l in oficinasMatutino[posSerie]:
                print(l)
            break
    # Listagem
    elif (selecao == 3):
        print(input("""Menu Listar inscrições
1 - Listar por aluno (ordem alfabética de nome)
2 - Listar por oficina (ordem alfabética)"""))
        ...
    else:
        print(rmAlunos)
        print(serieAlunos)
        print(nomeAlunos)
        print(periodoAlunos)
        break