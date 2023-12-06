turma = []

while True:
    print("Menu")
    print("1 - Cadastro")
    print("2 - Listar")
    print("3 - Pesquisar")
    print("4 - Alterar")
    print("5 - Excluir")
    print("9 - Sair")

    opcao = int(input("Informe a opção: "))

    if opcao == 1:
        aluno = {}
        aluno['nome'] = input("Informe o nome: ")
        aluno['disciplina'] = input("Informe a disciplina: ")
        aluno['nota1'] = float(input("Informe a nota 1: "))
        aluno['nota2'] = float(input("Informe a nota 2: "))
        aluno['nota3'] = float(input("Informe a nota 3: "))
        aluno['nota4'] = float(input("Informe a nota 4: "))
        turma.append(aluno)
    elif opcao == 2:
        for m in turma:
            media = (m['nota1'] + m['nota2'] + m['nota3'] + m['nota4']) / 4
            situacao =''
            if media >= 7: 
                situacao = 'Aprovado'
            else:
                situacao = 'Reprovado'

            print(f"""{m['nome']} - {m['disciplina']} - 
                  {m['nota1']} - {m['nota2']} - 
                  {m['nota3']} - {m['nota4']} - 
                   {media:.2f} - {situacao}""")
    elif opcao == 3:
        nomeBusca = input("Informe o nome para busca: ")

        posicao = -1
        i = 0
        for m in turma:
            if m['nome'].lower() == nomeBusca.lower():
                posicao = i
                break
            i = i + 1    

        if posicao > -1:        
            print(f"""{turma[posicao]['nome']} - {turma[posicao]['disciplina']} -
                {turma[posicao]['nota1']} - {turma[posicao]['nota2']} -
                {turma[posicao]['nota3']} - {turma[posicao]['nota4']} """)
        else:
            print("Não encontrado")
    elif opcao == 4:
        nomeBusca = input("Informe o nome para alterar: ")

        posicao = -1
        i = 0
        for m in turma:
            if m['nome'].lower() == nomeBusca.lower():
                posicao = i
                break
            i = i + 1

        if posicao > -1:
            turma[posicao]['nome'] = input("Informe o nome: ")
            turma[posicao]['disciplina'] = input("Informe a disciplina: ")
            turma[posicao]['nota1'] = float(input("Informe a nota 1: "))
            turma[posicao]['nota2'] = float(input("Informe a nota 2: "))
            turma[posicao]['nota3'] = float(input("Informe a nota 3: "))
            turma[posicao]['nota4'] = float(input("Informe a nota 4: "))
        else:
            print("Não encontrado.")   
    elif opcao == 5:
        nomeBusca = input("Informe o nome para excluir: ")

        posicao = -1
        i = 0
        for m in turma:
            if m['nome'].lower() == nomeBusca.lower():
                posicao = i
                break
            i = i + 1

        if posicao > -1:
            turma.pop(posicao)
            
        else:
            print("Não encontrado")

    elif opcao == 9:
        break
    else:
        print("Opção inválida.")