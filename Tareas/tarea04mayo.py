#EJERCICIO DE PACIENTES

print("\n# NOMBRE DE LOS PACIENTES\n")

paciente1 = str(input("Ingrese el nombre del primer paciente: "))
paciente2 = str(input("Ingrese el nombre del segundo paciente: "))
paciente3 = str(input("Ingrese el nombre del tercer paciente: "))

print("\n# PESO DE LOS PACIENTES\n")

peso1 = float(input("Ingrese el peso del primer paciente: "))
peso2 = float(input("Ingrese el peso del segundo paciente: "))
peso3 = float(input("Ingrese el peso del tercer paciente: "))

print("\n# ESTATURA DE LOS PACIENTES\n")

estatura1 = float(input("Ingrese la estatura del primer paciente: "))
estatura2 = float(input("Ingrese la estatura del segundo paciente: "))
estatura3 = float(input("Ingrese la estatura del tercer paciente: "))

print("\n# EDAD DE LOS PACIENTES\n")

edad1 = int(input("Ingrese la edad del primer paciente: "))
edad2 = int(input("Ingrese la edad del segundo paciente: "))
edad3 = int(input("Ingrese la edad del tercer paciente: "))

#WHILE DE EDADES

while edad1 <1 or edad1 >100:
    print("La edad ingresada es inválida")
    edad1 = int(input("Ingrese una edad válida: "))

while edad2 <1 or edad2 >100:
    print("La edad ingresada es inválida")
    edad2 = int(input("Ingrese una edad válida: "))

while edad3 <1 or edad3 >100:
    print("La edad ingresada es inválida")
    edad3 = int(input("Ingrese una edad válida: "))


#CONFORMANDO LAS TUPLAS POR LISTAS

Tupla1 = (paciente1, peso1, estatura1, edad1)
Tupla2 = (paciente2, peso2, estatura2, edad2)
Tupla3 = (paciente3, peso3, estatura3, edad3)

#LISTAS CONFORMADAS EN UNA TUPLA ÚNICA Y FINAL

Tuplafinal = [(Tupla1),(Tupla2),(Tupla3)]

#RESULTADO FINAL

print("Los datos quedaron conformados de la siguiente manera: ",Tuplafinal)

#ISDIGIT (EVITA QUE EN LA SENTENCIA SE INCLUYAN VALORES NUMÉRICOS)
