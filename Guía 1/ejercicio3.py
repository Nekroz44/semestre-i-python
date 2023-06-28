#EJERCICIO 3

a = float(input("Ingrese el primer lado del triángulo: "))
b = float(input("Ingrese el segundo lado del triángulo: "))
c = float(input("Ingrese el tercer lado del triángulo: "))

Triángulo = (a,b,c)

while a == b == c:
    print ("El triángulo corresponde a equilátero")
    break

while a == b != c or a != b == c or a != c == b: 
    print ("El triángulo corresponde a un isósceles")
    break

while a != b != c:
    print ("El triángulo corresponde a escaleno")
    break


print (Triángulo)
