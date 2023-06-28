#SETS

random_tuple = (34, "Hola", False)

set1 = {"Hola", 21, True, random_tuple}
set2 = {1, 4, 7, 8, 15}
set3 = {4, 15, 6, 2, 1}

#FUNCIÓN ADD

set1.add(344)
set1.add("Diego")

print (set1)

#FUNCIÓN CLEAR

#set1.clear()

print (set1)

#FUNCIÓN DISCARD

set1.discard(21)

print (set1)

#FUNCIÓN INTERSECTION

Intersectiondesets = set2.intersection(set3)

print(Intersectiondesets)

#FUNCIÓN DIFFERENCE

Differencesets = set3.difference(set2)

print(Differencesets)

#FUNCIÓN COPY

Copy_Set = set2.copy()

Copy_Set.add(30)

print (set2)
print (Copy_Set)

#TAMBIÉN SE PUEDEN USAR FUNCIONES QUE SON PARTE DE LAS LISTAS COMO EL "POP", "REMOVE" O EL "LEN"


