####EJERCICIO 4####

nom1 = input("Ingrese un primer nombre: ")
nom2 = input("Ingrese un segundo nombre: ")

if nom1[0] == nom2[0]:
    print("Ambos nombres comienzan con la misma letra")
elif nom1[-1] == nom2[-1]:
    print("Ambos nombres terminan con la misma letra")
else:
    print("Ambos nombres no coincinden ni en la primera ni última letra")