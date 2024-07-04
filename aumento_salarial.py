salario_colaborador = float(input("Digite o sálario: "))

if salario_colaborador == 280.00:
    aumento = salario_colaborador * 0.20
    salario_atual = salario_colaborador + aumento
    print(f"Ganhou um aumento de 20%, antes você ganahava R${salario_colaborador}, com o aumento você ganha mais R${aumento},agora recebe R${salario_atual:.2f}")
    
elif salario_colaborador > 280.00 and salario_colaborador <= 700.00:
    aumento = salario_colaborador * 0.15
    salario_atual = salario_colaborador + aumento
    print(f"Ganhou um aumento de 15%, antes você ganahava R${salario_colaborador}, com o aumento você ganha mais R${aumento},agora recebe R${salario_atual:.2f}")

elif salario_colaborador > 700.00 and salario_colaborador < 1500.00:
    aumento = salario_colaborador * 0.10
    salario_atual = salario_colaborador + aumento
    print(f"Ganhou um aumento de 10%, antes você ganahava R${salario_colaborador}, com o aumento você ganha mais R${aumento},agora recebe R${salario_atual:.2f}")

elif salario_colaborador > 1500.00:
    aumento = salario_colaborador * 0.05
    salario_atual = salario_colaborador + aumento
    print(f"Ganhou um aumento de 5%, antes você ganahava R${salario_colaborador}, com o aumento você ganha mais R${aumento},agora recebe R${salario_atual:.2f}")