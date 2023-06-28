#####EJERCICIO 5#####

import random

rand_list = []

for i in range (0, 20):
    random_num = random.randint(40, 350)
    rand_list.append(random_num)
print(rand_list)

while True:
    try:
        num_user = int(input('Ingrese un numero entre 40 y 350: '))
        if (num_user < 40) or (num_user > 350):
            print('Ingrese un valor igual o mayor a 40.')
            continue
        else:
            break
    except ValueError:
        print('Ingrese un numero valido.')

if num_user not in rand_list:
    print('\nEl numero no se encuentra en la lista.')
else:
    ocurrencia = rand_list.count(num_user)
    print('\nEl número se encuentra en la lista.')
    print('El número aparece:', ocurrencia)






