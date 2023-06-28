#-#-#-#-#-# EJERCICIO 1 #-#-#-#-#-#

#Dado un diccionario que contiene nombres y edades de personas, crea una lista que contenga los nombres de 
#personas que cumplen con las siguientes condiciones:

#Su edad es mayor de 20 años
#Su nombre comienza con la letra "M" o "L"
#Su edad es un número impar

people_data = {
    "Juan": 20,
    "María": 17,
    "Pedro": 25,
    "Ana": 16,
    "Luis": 22,
    "Marta": 27,
    "Lucía": 31,
    "Mario": 19,
    "Laura": 23,
    "Leandro": 29,
}

dif_list = []

for clave, valor in people_data.items():
    if valor > 20 and (clave.startswith("M") or clave.startswith("L")) and valor % 2 != 0:
        dif_list.append(f"{clave}:{valor}")

print(dif_list)


