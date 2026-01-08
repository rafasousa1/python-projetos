def adiconar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"A tarefa {nome_tarefa}, foi adicionada")
    return
 
tarefas = []

while True:
    print("\n Seu Gerenciador de Tarefas")
    print("1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Atualizar tarefa")
    print("4 - Completar tarefa")
    print("5 - Excluir tarefas completadas")
    print("6 - Sair")

    escolha = input('O que deseja realizar? ')

    if escolha == '1':
        nome_tarefa = input("Digite o nome da tarefa que quer adicionar: ")
        adiconar_tarefa(tarefas,nome_tarefa)
    elif escolha == '6':
        break

print("Até Logo!")