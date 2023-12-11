from manipulaAluno import alterar, buscar, cadastrar, excluir, exibir, listar
from utils import menu

turma = []


while True:
    menu()
    opcao = int(input("Informe a opção: "))

    if opcao == 1:
        cadastrar(turma)
    elif opcao == 2:
        listar(turma)
    elif opcao == 3:
        posicao = buscar(turma)
        exibir(turma, posicao)
    elif opcao == 4:
        posicao = buscar(turma)
        alterar(turma, posicao)
    elif opcao == 5:
        posicao = buscar(turma)
        excluir(turma, posicao)
    elif opcao == 9:
        break
    else:
        print("Opção inválida.")