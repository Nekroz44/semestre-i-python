#LAS LISTAS...

lista1 = [1,4,9,15,23]
print (lista1)

lista2 = [4,"Diego",True]
print (lista2)

print (lista2[1])

#Las listas son más ordenas, ya que se puede pedir posición de uno de sus elementos
#Son editables, ya que se puede cambiar los elementos dentro de ella (Eliminar o añadir)
#Son dinámicas ya que se pueden añadir diferentes tipo de datos dentro de ella (Strings, Float, Int, Boolean ,etc)
#No son únicas; los elementos que contiene pueden estar duplicados sin que arroje ningún error


#CARACTERÍSTICAS DE LAS LISTAS

#FUNCIÓN APPEND (Agrega un elemento al final de la lista)

(lista1.append("Lunes"))
print (lista1)

(lista1.append(570))
print (lista1)

#FUNCIÓN INSERT (Inserta un elemento en una posición específica)

#(lista2.insert(2,-2))
print (lista2)

#FUNCIÓN EXTEND (Simplemente combinas dos o más listas)

#(lista1.extend(lista2))
print (lista1)

#FUNCIÓN REMOVE (Remueve cualquier ocurrencia de la lista)

(lista2.remove(1))
print (lista2)

#FUNCIÓN POP (Borra y retorna al último elemento de una lista)

(lista1.pop(3))
print (lista1)

#FUNCIÓN SORT (Ordena los elementos de forma ascendente)

lista3 = [68,15,186,4,1,24,83,581,941,2]

(lista3.sort)
print(lista3)
