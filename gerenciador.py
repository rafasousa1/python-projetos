def adiconar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"A tarefa {nome_tarefa}, foi adicionada")
    return

def ver_tarefas(tarefas):
    print("\nLista de Tarefas")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{i}. [{status}] {nome_tarefa}")
    return

def atualiza_nome_tarefa(tarefas, indice_tarefa, tarefa_nova):
    ajuste_indice = int(indice_tarefa) - 1
    if ajuste_indice >= 0 and ajuste_indice < len(tarefas):
        tarefas[ajuste_indice]["tarefa"] = tarefa_nova
        print(f"Tarefa {indice_tarefa} atualizada para {tarefa_nova}")
    else:
        print("Indíce de tarefa inválido!")
    return

def completar_tarefa(tarefas, indice_tarefa):
    ajuste_indice = int(indice_tarefa) - 1
    tarefas[ajuste_indice]["completada"] = True
    print(f'Tarefa {indice_tarefa} marcada como completada!')
    return

def deletar_tarefas_completadas(tarefas):    
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)
    print('As tarefas completadas foram deletadas!')
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

    elif escolha == '2':
        ver_tarefas(tarefas)

    elif escolha == '3':
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o número da tarefa que quer atualizar: ")
        novo_nome = input("Digite o nome da nova tarefa: ")
        atualiza_nome_tarefa(tarefas, indice_tarefa, novo_nome)

    elif escolha == '4':
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o número da tarefa que quer atualizar: ")
        completar_tarefa(tarefas, indice_tarefa)
    
    elif escolha == '5':
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)

    elif escolha == '6':
        break

print("Até Logo!")