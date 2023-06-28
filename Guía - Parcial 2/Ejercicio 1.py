#-#-#-#-#-# EJERCICIO 1 #-#-#-#-#

def num_cant():
    while True:
        try:
            num = (int(input("Indique la cantidad de números a ingresar: ")))
            if num < 0:
                print ("Solamente se permiten números positivos")
                continue
            else:
                break
        except ValueError:
            print ("Ingrese solamente números")
            continue
    return num

def pedir(num):
    num_list = []
    for i in range(num):
        num = int(input("Ingrese un número: "))
        num_list.append(num)
    return num_list

def suma_par(num_list):
    suma_par = 0
    for i in num_list:
        if i % 2 == 0:
            suma_par = suma_par + i
    return suma_par

def suma_impar(num_list):
    suma_impar = 0
    for i in num_list:
        if i % 2 != 0:
            suma_impar = suma_impar + i
    return suma_impar

print('\n #=#=#=#=[ EJERCICIO 1 v]=#=#=#=#\n')    
        
num = num_cant()
num_list = pedir(num)


print ("El resultado de la suma par es:",suma_par(num_list))
print ("El resultado de la suma impar es:",suma_impar(num_list))
print ("El resultado de la suma total es:",sum(num_list))

print('\n #=#=#=#=[ FIN EJERCICIO 1 ]=#=#=#=#\n')
    