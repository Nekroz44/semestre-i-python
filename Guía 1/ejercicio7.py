#######EJERCICIO 7#######

workers = ["Ramiro", "Ernesto", "Alex", "Pablo", "Fernando"]
ages = [48, 21, 53, 37, 40]

info = workers + ages
   
info = tuple((zip(workers, ages)))
print(info)

