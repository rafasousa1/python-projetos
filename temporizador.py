import time

t = input("Digite o tempo (em segundos) ")

if t.isdigit():
    t = int(t)
else:
    print("Valor inválido digite apenas números")
    quit()
    
while t:
    minutos, segundos = divmod(t, 60)
    timer = "{:02d}:{:02d}".format(minutos, segundos)
    print(timer, end="\r")
    time.sleep(1) 
    t = t - 1
    
print("TEMPO ENCERRADO!!")