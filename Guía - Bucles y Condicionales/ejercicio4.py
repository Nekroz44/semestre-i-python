####EJERCICIO 4####

while True:
    try:
        num_user = int(input("Ingrese un número entero: "))
        if num_user < 1: 
            print("Ingrese un valor mayor o igual a 1: ")
            continue
        else:
            break
    except ValueError:
        print("Ingrese un valor numérico válido: ")
print()

odd = 1

for i in range(num_user):
    odd_list = []
    odd_sum = 0
    j = 0
    
    while j <= i:
        odd_sum += odd
        odd_list.append(str(odd))
        odd += 2
        j += 1
        
    odd_str = " + ".join(odd_list)
    
    print(f'{i+1}**3 = {odd_sum} ➜  {odd_str} = {odd_sum}')