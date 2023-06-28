####EJERCICIO 9####

num = [4,3,8,12,6,10,14,3,6]

#ÍTEM A)

del num [-1]

print (num)

#ÍTEM B)

num.insert (0,2)

print (num)

#ÍTEM C)

num_no_repeat = []

for i in num:
    if i not in num_no_repeat:
        num_no_repeat.append (i)

print (num_no_repeat)

#ÍTEM D)

#MEDIA ARITMÉTICA

list_ordenados = sorted(num)

print (list_ordenados)

MA = sum(num) / len(num)
print (round(MA, 2))

#MEDIANA

if len(list_ordenados) % 2 == 0:
    mediana_pos_1 = (len(list_ordenados) / 2) -1
    mediana_pos_2 = mediana_pos_1 + 1

    mediana = (list_ordenados[mediana_pos_1] + list_ordenados[mediana_pos_2]) / 2
else:
    mediana_pos_1 = (len(list_ordenados) // 2)
    mediana = list_ordenados[mediana_pos_1]

print (mediana)




