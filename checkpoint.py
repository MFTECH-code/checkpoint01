from time import sleep

# Tupla de oficinals
# Criar e contar histórias -> index 0... Criando e recriando com emojis -> index 9
oficinas = ("Criar e contar histórias", "Teatro: Luz, Câmera e Ação", "A língua de sinais", "Expressão Artística", "Soletrando", "Leitura dramática", "O corpo fala", "O mundo da imaginação", "Leitura dinâmica", "Criando e recriando com emojis")
# Lista de contadores de alunos em oficinas
lotacaoOficinas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Matriz da grade das oficinas da manhã
oficinasMatutino = [(oficinas[0], oficinas[2]),
(oficinas[0], oficinas[1], oficinas[2]),
(oficinas[1], oficinas[2], oficinas[3]),
(oficinas[2], oficinas[3], oficinas[4])]
# Matriz da grade das oficinas da tarde
oficinasVespertino = [(oficinas[7], oficinas[9]),
(oficinas[6]), (oficinas[5]), (oficinas[8])]

# Tupla de series
series = ("2ª serie", "3ª serie", "4ª serie", "5ª serie")
# Alunos
oficinasAlunos = []
rmAlunos = []
serieAlunos = []
nomeAlunos = []

# Variável de controle
cadastro = True
totalAlunos = 0

# Listas filtradas
filtro_aluno = []
filtro_oficina = []


def imprimir_listagem(filtro):
    for i in range(0, len(filtro)):
        print(f"NOME: {filtro[i][0]}")
        print(f"RM: {filtro[i][1]}")
        print(f"SERIE: {filtro[i][2]}")
        if (len(filtro[i][3]) > 0):
            print("OFICINAS ADICIONADAS: ")
            for l in range(0, len(filtro[i][3])):
                print(f"{l+1} - {filtro[i][3][l]}")
            print("##########################################")
        else:
            print("NENHUMA OFICINA ADICIONADA")
            print("##########################################")

def filtrar_alunos(filtro):
    # Puxar os alunos de ordem alfabética
    lista_ordenada = sorted(nomeAlunos)
    
    # Primeiro encher as posições do filtro
    for i in range(0, len(filtro)):
        # Pegando posições raíz
        pos_aluno = nomeAlunos.index(lista_ordenada[i])

        # Colocando nomes
        filtro[i].insert(0, lista_ordenada[i])
        # Colocando RMs
        filtro[i].insert(1, rmAlunos[pos_aluno])
        # Colocando serie 
        filtro[i].insert(2, serieAlunos[pos_aluno])
        # Colocando Oficinas
        filtro[i].insert(3, oficinasAlunos[pos_aluno])
    return filtro

def sem_filtro(filtro):
    for i in range(0, len(filtro)):
        # Colocando nomes
        filtro[i].insert(0, nomeAlunos[i])
        # Colocando RMs
        filtro[i].insert(1, rmAlunos[i])
        # Colocando serie 
        filtro[i].insert(2, serieAlunos[i])
        # Colocando Oficinas
        filtro[i].insert(3, oficinasAlunos[i])
    return filtro

# Função para adicionar lista dentro de vetor
def lotar_lista(lista):
    lista.append([])

def filtro():
    print("""Listagem de oficina e alunos
1 - Listar por aluno (Ordem Alfabética de nome)
2 - Listar sem filtro""")
    filtro = int(input("Digite o tipo de filtragem desejada: "))
    while (filtro < 1 or filtro > 2):
        print("Selecione uma das opções mostradas acima...")
        filtro = int(input("Digite o tipo de filtragem desejada: "))
    return filtro

def menu():
    print("COLÉGIO NOVA ESPERANÇA - EVENTO LITERÁRIO")
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
        print("##########################################")
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
        print("##########################################")
        return selecao
print("##########################################")
while True:
    selecao = menu()
    sleep(1)
    
    # Cadastro
    if (selecao == 1):

        print("CADASTRO DE ALUNOS")
        while True:
            rm = input("Digite o rm do aluno: ").strip()
            while (rm in rmAlunos):
                print("rm já existe!")
                rm = input("Digite o rm do aluno: ").strip()
                if (rm == "0"):
                    cadastro = False
                    sleep(1)
                    break 
            if (rm == "0"):
                cadastro = False
                sleep(1)
                break
            else:
                rmAlunos.append(rm)
                nome = input("Digite o nome do aluno: ").strip().capitalize()
                nomeAlunos.append(nome)
                serie = int(input("Digite a serie do aluno: ").strip()[0])
                while (serie < 2 or serie > 5):
                    print("Série inválida!")
                    serie = int(input("Digite a serie do aluno: ").strip()[0])
                serieAlunos.append(series[serie-2])
                oficinasAlunos.append([])
                lotar_lista(filtro_aluno)
                totalAlunos += 1
                print("Aluno cadastrado!")
                sleep(1)
                print("##########################################")
                
    # Inscrição
    elif (selecao == 2):
        print("INSCRIÇÃO DE ALUNOS EM OFICINAS")
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
                    sleep(1)
                    break
            elif (periodo == "V" or periodo == "T"):
                print("Oficinas do perído vespertino")
                for c in oficinasVespertino:
                    cont = 1
                    if (posSerie == 0):
                        for l in oficinasVespertino[posSerie]:
                            print(f"{cont} - {l}")
                            cont += 1
                        sleep(1)
                        break
                    else:
                        for l in oficinasVespertino[posSerie]:
                            if (c == oficinasVespertino[posSerie]):
                                print(f"1 - {c}")
                            sleep(1)
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
                            print("OFICINA ADICIONADA COM SUCESSO!")
                            sleep(1)
                        else:
                            print("OFICINA LOTADA (QTD MÁX 10 ALUNOS)")
                            sleep(1)

                    else:
                        print("ALUNO ATINGIU A QUANTIDADE MÁXIMA DE OFICINAS QUE PODE SE CADASTRAR (LIMITE 3 OFICINAS)")
                        sleep(1)
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
                                print("OFICINA ADICIONADA COM SUCESSO!")
                                sleep(1)
                            else:
                                print("OFICINA LOTADA (QTD MÁX 10 ALUNOS)")
                                sleep(1)
                            
                            #-----
                        else:
                            
                            if (oficinasVespertino[posSerie] in oficinasAlunos[posRm]):
                                print("ALUNO ATINGIU A QUANTIDADE MÁXIMA DE OFICINAS QUE PODE SE CADASTRAR (LIMITE 3 OFICINAS)")
                                sleep(1)
                                break
                            #-----
                            # Contador da oficina escolhida
                            oficinaEscolhida = oficinasVespertino[posSerie]
                            oficinaPos = oficinas.index(oficinaEscolhida)

                            if (lotacaoOficinas[oficinaPos] < 10):
                                lotacaoOficinas[oficinaPos] += 1
                                oficinasAlunos[posRm].insert(posRm, oficinasVespertino[posSerie])
                                print("OFICINA ADICIONADA COM SUCESSO!")
                                sleep(1)
                            else:
                                print("OFICINA LOTADA (QTD MÁX 10 ALUNOS)")
                                sleep(1)
                            #-----
                            
                    else:
                        print("ALUNO ATINGIU A QUANTIDADE MÁXIMA DE OFICINAS QUE PODE SE CADASTRAR (LIMITE 3 OFICINAS)")
                        sleep(1)
                break
            
    # Listagem
    elif (selecao == 3):
        # Menu de seleção de listagem
        filtro_listagem = filtro()
        # Criar uma matriz filtrada comforme a seleção
        if (filtro_listagem == 1):
            print("LISTAGEM DE ALUNOS EM ORDEM ALFABÉTICA")
            # Construindo matriz com dados dos alunos em ordem alfabética
            filtro_aluno = filtrar_alunos(filtro_aluno)
            # Imprimir o resultado
            imprimir_listagem(filtro_aluno)
            sleep(2)
        else:
            print("LISTAGEM SEM FILTRO")
            filtro_aluno = sem_filtro(filtro_aluno)
            imprimir_listagem(filtro_aluno)
            sleep(2)
    else:
        break