#####EJERCICIO 5#####

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

prom = nota1 * 0.3 + nota2 * 0.7 + nota3 * 0.3

if prom > 6.0 and prom < 7.0:
    print(f'El estudiante aprobó la asignatura con distinción, su promedio fue de {round(prom, 1)}')
elif prom > 7.0:
    print(f'El resultado del promedio solicitado excede el límite legal calificación {round(prom, 1)}')
elif prom > 4.0 and prom < 5.9:
    print(f'El estudiante aprobó la asignatura con un promedio de {round(prom, 1)}') 
else:
    print(f'El estudiante reprobó la asignatura con un promedio de {round(prom, 1)}')

