import random

escolha_user = input("Olá, escolha o que quer lançar pedra, papel ou tesoura: ").lower()
while escolha_user not in ['pedra', 'papel', 'tesoura']:
    escolha_user = input("Escolha inválida digite apenas pedra, papel ou tesoura: ").lower()

escolha_pc = random.choice(['pedra', 'papel', 'tesoura'])

while True:
    if escolha_user == escolha_pc:
        print("EMPATE")
    elif (escolha_user == 'pedra' and escolha_pc == 'tesoura') or (escolha_user == 'tesoura' and escolha_pc == 'papel') or (escolha_user == 'papel' and escolha_pc == 'pedra'):
        print("GANHOU PARABÉNS")
    else:
        print("VOCÊ PERDEU")
    
    continuar = input("Quer jogar denovo? (S/N): ").lower()
    
    if continuar != 's':
       break