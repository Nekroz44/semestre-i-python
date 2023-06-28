####EJERCICIO 1####

#ITEM A

print ("\nITEM A\n")

a = [21,8,15,3,12]
b = [10,9,12,15,18]
c = [2,3,8,9,12]

list_full = a + b + c   

print (list_full)

#ITEM B

print("\nITEM B\n")

list_full.insert(-1,20)

print(list_full)

#ITEM C

print("\nITEM C\n")

list_full.sort(reverse = True)
print(list_full)

#ITEM D

print("\nITEM D\n")

listanueva = [4,5,6]
list_full.append(listanueva)
print(list_full)

#ITEM E

print("\nITEM E\n")

sum_sublist = listanueva[-1] + listanueva[-2] + listanueva[-3]
sum_list_full = list_full[0]+list_full[1]+list_full[2]+list_full[3]+list_full[4]+list_full[5]+list_full[6]+list_full[7]+list_full[8]+list_full[9]+list_full[10]+list_full[11]+list_full[12]+list_full[13]+list_full[14]+list_full[15]
final_list = sum_sublist + sum_list_full
print(final_list)

#ITEM F

print("\nITEM F\n")

promedio = (final_list) / 19
print (round(promedio, 2))