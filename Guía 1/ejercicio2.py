##EJERCICIO 2##

nom1=(str(input("Ingrese la primera palabra: ")))
nom2=(str(input("Ingrese la segunda palabra: ")))

if len(nom1)>len(nom2):
    print(f"La palabra '{nom1}' contiene más carácteres.")
    print(f"La palabra '{nom2}' contiene menos carácteres.")

elif len(nom1)<len(nom2):
    print(f"La palabra '{nom1}' contiene menos carácteres.")
    print(f"La palabra '{nom2}' contiene más carácteres.")

else:
    print("Ambas contienen los mismos carácteres")