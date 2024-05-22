from random import randint

nome = input("Olá, qual o seu nome? ")
print(f"Ok {nome}, estou tentando advinhar um número de 1 até 10, consegue me ajudar?")

numero_advinhado = randint(0,10)
tentativas = 3

for i in range(1, tentativas + 1):
    numero_escolhido = int(input("Digite um número: "))
    if numero_escolhido == numero_advinhado:
        print(f"Parabéns você acertou em {i} tentativas")
        break
    elif numero_escolhido > numero_advinhado:
        print("Digite um número menor")
    else:
        print("Digite um número maior")