def m_para_km(u1):
    return u1 / 1000

def km_para_m(u1):
    return u1 / 1000

def cm_para_m(u1):
    return u1 / 100

def mm_para_m(u1):
    return u1 / 1000

def m_para_mm(u1):
    return u1 * 1000

def m_para_cm(u1):
    return u1 * 100

def c_para_f(u1):
    return u1 * 9 / 5 + 32

def f_para_c(u1):
    return (u1 - 32) * 5 / 9

def conversor():
    print("Olá,selecione uma das opções!")
    print("Metros para Km (1)")
    print("Km para metros (2)")
    print("Cm para metros (3)")
    print("Milimetros para metros (4)")
    print("Metros para milimetros (5)")
    print("Metros para centímetros (6)")
    print("Celsius para Fahrenheit (7)")
    print("Fahrenheit para Celsius (8)")
    unidade = (input("> "))
        
    u1 = float(input("Digite o número que deseja converter: "))
        
    if unidade == "1":
            print(f"{u1} Convertendo para km fica {m_para_km(u1)}km")
    elif unidade == "2":
            print(f"{u1} Convertendo para metros fica {km_para_m(u1)}m")
    elif unidade == "3":
            print(f"{u1} Convertendo para metros fica{cm_para_m(u1)}m")
    elif unidade == "4":
            print(f"{u1} Convertendo para metros fica {mm_para_m(u1)}m")
    elif unidade == "5":
            print(f"{u1} Convertendo para mm fica {m_para_mm(u1)}mm")
    elif unidade == "6":
            print(f"{u1} Convertendo para cm fica {m_para_cm(u1)}cm")
    elif unidade == "7":
            print(f"{u1} Convertendo para Fahrenheit fica {c_para_f(u1)}F")
    elif unidade == "8":
            print(f"{u1} Convertendo para Celsius fica {f_para_c(u1)}C")
    else:
        print("Digite um valor válido!")
conversor()