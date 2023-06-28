print ("#-#-#-#-#-# FUNCIONES #-#-#-#-#-#")

#Para trabajar con funciones: Palabra reservada es "def"

#Una función propia de python son: len(), str(), count(), sort(), etc

#Scope

def hola():
    print ("un simple saludo")

hola()

print ("#-#-#-#-# DECLARANDO FUNCIÓN Y UTILIDAD #-#-#-#-#")

def concatenar(lista1,lista2):
    return lista1 + lista2

lista1 = [1,2,3]
lista2 = [4,5,6]

#concatenar() va a dar error ya que a diferencia de la anterior en el paréntesis no se hace llamado a los parámetros designados (lista1 y 2)
print (concatenar(lista1,lista2))

def suma (num1, num2):
   return num1 + num2

print(suma(4,6))
print(suma(106,79))

def resta(num1, num2):
    return num1 - num2

print(resta(6,3))
print(resta(4756,512))

#Ahora con imput

def multiply (a,b):
    return a * b

a = int(input("Ingrese su primer número: "))
b = int(input("Ingrese su segundo número: "))

print("El resultado de su multiplicación es:", multiply(a,b))

#*AHORA TODOS LOS EJERCICIOS VISTO ANTES SERÁN CON FUNCIONES*

