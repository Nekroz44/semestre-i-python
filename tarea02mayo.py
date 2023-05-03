a=input("Nombre del estudiante: ")
b=input("Nombre de la asignatura: ")
c=input("Nota Laboratorio 1: ")
d=input("Nota Laboratorio 2: ")

lista = (a,b,c,d)
c1=int(c)*(30/100)
d2=int(d)*(70/100)
cd=int(c1)+int(d2)

print(f"Datos ingresados: {lista}/y la nota final: {cd}")
