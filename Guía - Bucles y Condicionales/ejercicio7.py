#######EJERCICIO 7#######

fact = 1
fact_list = []

while True:
    try:
        user_num = int(input('Ingresa un número entero: '))
        if user_num < 0:
            print('Ingresa un número entero positivo.')
            continue
        else:
            break
    except:
        print('Ingresa un número valido')

if user_num == 0:
    print('El factorial de 0 es: 1')
    print('\n0! = 1')

else:
    for i in range(1, user_num+1):
        fact = fact * i

    for j in range(user_num, 0, -1):
        j = str(j)
        fact_list.append(j)
    
    print('El factorial de', user_num, 'es:', fact)
    fact_list_str = ' * '.join(fact_list)
    print(f'\n{user_num}! = {fact_list_str} = {fact}')