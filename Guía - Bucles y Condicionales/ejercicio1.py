# """"""EJERCICIO 1"""""""

lista = ("La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional entrega una contribucion significativa al desarrollo sostenible en el territorio .Como Universidad sus pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participacion democratica")

lista_sub = lista.split()

lista_sub2 = lista_sub.count("Universidad")
lista_sub2 += lista_sub.count("universidad")

lista_sub3 = (str(lista_sub2))

print (tuple(lista_sub3))











