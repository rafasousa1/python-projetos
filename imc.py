peso = float(input("Olá, digite seu peso (kg): "))
altura = float(input("Ok, agora digite sua altura (m): "))

imc = peso / (altura **2)

if imc < 18.5:
    print(f"O seu IMC é de {imc:.2f}, e você está abaixo do seu peso esperado")
elif imc >= 18.5 and imc < 24.9:
    print(f"O seu IMC é de {imc:.2f}, e você está com o peso normal")
elif imc >= 25 and imc < 29.9:
    print(f"O seu IMC é de {imc:.2f}, e você está com um peso maior que o ideal")
elif imc >= 30 and imc < 39.9:
    print(f"O seu IMC é de {imc:.2f}, e você está obeso")
else:
    print("Obesidade grave!")