# Criar e contar histórias -> index 0... Criando e recriando com emojis -> index 9
oficinas = ("Criar e contar histórias", "Teatro: Luz, Câmera e Ação", "A língua de sinais", "Expressão Artística", "Soletrando", "Leitura dramática", "O corpo fala", "O mundo da imaginação", "Leitura dinâmica", "Criando e recriando com emojis")
lotacaoOficinas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


oficinasMatutino = [(oficinas[0], oficinas[2]),
(oficinas[0], oficinas[1], oficinas[2]),
(oficinas[1], oficinas[2], oficinas[3]),
(oficinas[2], oficinas[3], oficinas[4])]

oficinasVespertino = [(oficinas[7], oficinas[9]),
(oficinas[6]), (oficinas[5]), (oficinas[8])]


series = ("2ª serie", "3ª serie", "4ª serie", "5ª serie")
# Alunos
oficinasAlunos = []
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


def filtro():
    print("""Listagem de oficina e alunos
1 - Listar por aluno (Ordem Alfabética de nome)
2 - Listar por oficina (Ordem Alfabética)""")
    filtro = int(input("Digite o tipo de filtragem desejada: "))
    while (filtro < 1 or filtro > 2):
        print("Selecione uma das opções mostradas acima...")
        filtro = int(input("Digite o tipo de filtragem desejada: "))
    return filtro

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
                oficinasAlunos.append([])
                
    # Inscrição
    elif (selecao == 2):
        rm = input("Insira o rm: ").strip()
        while (rm not in rmAlunos):
            print("Aluno não cadastrado... Favor procurar a coordenação do Fundamental I")
            rm = input("Insira o rm: ").strip()
        posRm = rmAlunos.index(rm)
        serieDoAluno = serieAlunos[posRm]
        posSerie = series.index(serieDoAluno)

        # Selecionar período da oficina que quer ver
        while True:
            periodo = input("Digite o período que deseja vizualizar: ").strip()[0].capitalize()
            while (periodo not in "MVT"):
                print("Período inválido... (Matutino ou Vespertino)")
                periodo = input("Digite o período do aluno: ").strip()[0].capitalize()
            if (periodo == "M"):
                print("Oficinas do perído matutino")
                for c in oficinasMatutino:
                    cont = 1
                    for l in oficinasMatutino[posSerie]:
                        print(f"{cont} - {l}")
                        cont += 1
                    break
            elif (periodo == "V" or periodo == "T"):
                print("Oficinas do perído vespertino")
                for c in oficinasVespertino:
                    cont = 1
                    if (posSerie == 0):
                        for l in oficinasVespertino[posSerie]:
                            print(f"{cont} - {l}")
                            cont += 1
                        break
                    else:
                        for l in oficinasVespertino[posSerie]:
                            if (c == oficinasVespertino[posSerie]):
                                print(f"1 - {c}")
                            break

            check = input("Você deseja vizualizar outro período?[S/N]: ").strip()[0].capitalize()
            while (check not in "SN"):
                print("Resposta inválida... (Sim ou Não)")
                check = input("Você deseja vizualizar outro período?[S/N]: ").strip()[0].capitalize()
            if (check == "N"):
                opt = int(input("Selecione o número da diciplina escolhida: "))
                if (periodo == "M"):
                    if (len(oficinasAlunos[posRm]) < 3):
                        while(oficinasMatutino[posSerie][opt-1] in oficinasAlunos[posRm]):
                            print("Aluno já está cadastrado nessa oficina... Favor selecionar outra")
                            opt = int(input("Selecione o número da diciplina escolhida: "))
                        # Contador da oficina escolhida
                        oficinaEscolhida = oficinasMatutino[posSerie][opt-1]
                        oficinaPos = oficinas.index(oficinaEscolhida)

                        if (lotacaoOficinas[oficinaPos] < 10):
                            lotacaoOficinas[oficinaPos] += 1
                            oficinasAlunos[posRm].insert(posRm, oficinasMatutino[posSerie][opt-1])
                            print("Sucesso")
                            print("Oficina adicionada")
                        else:
                            print("Oficina já está lotada! MÁXIMO 10 ALUNOS")

                    else:
                        print("Cada aluno pode se inscrever no máximo em 3 oficinas")
                else:
                    if (len(oficinasAlunos[posRm]) < 3):
                        while(oficinasVespertino[posSerie][opt-1] in oficinasAlunos[posRm]):
                            print("Aluno já está cadastrado nessa oficina... Favor selecionar outra")
                            opt = int(input("Selecione o número da diciplina escolhida: "))
                        if (type(oficinasVespertino[posSerie]) != type("string")):
                            #-----
                            # Contador da oficina escolhida
                            oficinaEscolhida = oficinasVespertino[posSerie][opt-1]
                            oficinaPos = oficinas.index(oficinaEscolhida)

                            if (lotacaoOficinas[oficinaPos] < 10):
                                lotacaoOficinas[oficinaPos] += 1
                                oficinasAlunos[posRm].insert(posRm, oficinasVespertino[posSerie][opt-1])
                                print("Sucesso")
                                print("Oficina adicionada")
                            else:
                                print("Oficina já está lotada! MÁXIMO 10 ALUNOS")
                            
                            #-----
                        else:
                            
                            if (oficinasVespertino[posSerie] in oficinasAlunos[posRm]):
                                print("Aluno já está cadastrado nessa oficina...")
                                break
                            #-----
                            # Contador da oficina escolhida
                            oficinaEscolhida = oficinasVespertino[posSerie]
                            oficinaPos = oficinas.index(oficinaEscolhida)

                            if (lotacaoOficinas[oficinaPos] < 10):
                                lotacaoOficinas[oficinaPos] += 1
                                oficinasAlunos[posRm].insert(posRm, oficinasVespertino[posSerie])
                                print("Sucesso")
                                print("Oficina adicionada")
                            else:
                                print("Oficina já está lotada! MÁXIMO 10 ALUNOS")
                            #-----
                            
                    else:
                        print("Cada aluno pode se inscrever no máximo em 3 oficinas")
                break
            
    # Listagem
    elif (selecao == 3):
        # Menu de seleção de listagem
        filtro = filtro()
        # Criar uma matriz filtrada comforme a seleção
        # Imprimir o resultado
    else:
        break