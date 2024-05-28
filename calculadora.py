def soma(n1,n2):
    return n1 + n2

def subtrair(n1,n2):
    return n1 - n2

def multiplicar(n1,n2):
    return n1 * n2

def dividir(n1,n2):
    return n1 / n2

def calculadora():
    print("Selecione uma das opções!")
    print("SOMAR (1)")
    print("SUBTRAIR (2)")
    print("MULTIPLICAR (3)")
    print("DIVIDIR (4)")
    operacao = input("> ")
    
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    
    if operacao == "1":
        print(f" {n1} + {n2} = {soma(n1,n2)}")
    elif operacao == "2":
        print(f"{n1} - {n2} = {subtrair(n1,n2)}")
    elif operacao == "3":
        print(f"{n1} x {n2} = {multiplicar(n1,n2)}")
    elif operacao == "4":
        print(f"{n1} ÷ {n2} = {dividir(n1,n2)}")
    else:
        print("Escolha Inválida!")
calculadora()