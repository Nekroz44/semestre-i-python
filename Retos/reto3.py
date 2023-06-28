#RETO 3 (03/05/2023)

Ciudades = ["Santiago","Temuco","Osorno","Punta Arenas"]
CO = [134,99,245,50]

Índice_Mínimo = min(CO)
Índice_Máximo = max(CO)

CiudadconMaxIndice = Ciudades[CO.index(Índice_Mínimo)]
CiudadconMinIndice = Ciudades[CO.index(Índice_Máximo)]

print("La ciudad con el índice más alto es", CiudadconMaxIndice , Índice_Máximo)
print("La ciudad con el índice más bajo es", CiudadconMinIndice , Índice_Mínimo)


 

