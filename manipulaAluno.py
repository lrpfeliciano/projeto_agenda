def cadastrar(turma):
    aluno = {}
    aluno['nome'] = input("Informe o nome: ")
    aluno['disciplina'] = input("Informe a disciplina: ")
    aluno['nota1'] = float(input("Informe a nota 1: "))
    aluno['nota2'] = float(input("Informe a nota 2: "))
    aluno['nota3'] = float(input("Informe a nota 3: "))
    aluno['nota4'] = float(input("Informe a nota 4: "))
    turma.append(aluno)

def listar(turma):
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

def buscar(turma):
    nomeBusca = input("Informe o nome para busca: ")

    posicao = -1
    i = 0
    for m in turma:
        if m['nome'].lower() == nomeBusca.lower():
            posicao = i
            break
        i = i + 1
    return posicao

def exibir(turma, posicao):
    if posicao > -1:        
        print(f"""{turma[posicao]['nome']} - {turma[posicao]['disciplina']} -
                {turma[posicao]['nota1']} - {turma[posicao]['nota2']} -
                {turma[posicao]['nota3']} - {turma[posicao]['nota4']} """)
    else:
        print("Não encontrado")

    
def alterar(turma, posicao):
    if posicao > -1:
        turma[posicao]['nome'] = input("Informe o nome: ")
        turma[posicao]['disciplina'] = input("Informe a disciplina: ")
        turma[posicao]['nota1'] = float(input("Informe a nota 1: "))
        turma[posicao]['nota2'] = float(input("Informe a nota 2: "))
        turma[posicao]['nota3'] = float(input("Informe a nota 3: "))
        turma[posicao]['nota4'] = float(input("Informe a nota 4: "))
    else:
        print("Não encontrado.")   

def excluir(turma, posicao):
    if posicao > -1:
        turma.pop(posicao)            
    else:
        print("Não encontrado")

def fazNada():
    print("Estou fazendo nada")