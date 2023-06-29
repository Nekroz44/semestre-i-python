###EJERCICIO 3###

a = float(input("Ingrese el primer lado del triángulo: "))
b = float(input("Ingrese el segundo lado del triángulo: "))
c = float(input("Ingrese el tercer lado del triángulo: "))

triangulo = (a,b,c)
    
p = (a + b + c) / 2

area = p * (p - a) * (p - b) * (p - c)

if a != b and b != c and a != c:
    print("El triángulo corresponde a un escaleno")
elif a==b and a!=c or a!=b and a==c or b==a and b!=c or b!=a and b==c or c==a and c!=b or c!=a and c==b:
    print ("El triángulo corresponde a un isósceles")
else:
    print ("Es un triángulo equilátero")

print("El área del triángulo es la siguiente:",area)
