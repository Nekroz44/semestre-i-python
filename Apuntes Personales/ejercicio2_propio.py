#-#-#-#-#-# Ejercicio 2 #-#-#-#-#-#

#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen 
#posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]

lista = []


for index in alphabet:
    if index % 3 != 0:
     lista.append(index)

print(lista)
     

