########EJERCICIO 8########

mes = (str(input("Ingrese un mes correspondiente: "))).lower()

if mes == "diciembre" or mes == "enero" or mes =="febrero":
    print("Este mes corresponde a la estación de verano")
elif mes == "marzo" or mes == "abril" or mes == "mayo":
    print("Este mes corresponde a la estación de otoño")
elif mes == "junio" or mes == "julio" or mes == "agosto":
    print("Este mes corresponde a la estación de invierno")
elif mes == "septiembre" or mes == "octubre" or mes == "noviembre":
    print("Este mes corresponde a la estación de primavera")
else:
    print("Ingrese un mes válido")




