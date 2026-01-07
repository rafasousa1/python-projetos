while True:
    print("\n Seu Gerenciador de Tarefas")
    print("1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Atualizar tarefa")
    print("4 - Completar tarefa")
    print("5 - Excluir tarefas completadas")
    print("6 - Sair")

    escolha = input('O que deseja realizar? ')

    if escolha == '6':
        print('Até Logo!')
        break