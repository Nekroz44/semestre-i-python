Habitantes_Rios = 404432
Superficie_Rios = 18429
Habitantes_Magallanes = 166533
Superficie_Magallanes = 1382291

Densidad_Ríos = Habitantes_Rios / Superficie_Rios
Densidad_Magallanes = Habitantes_Magallanes / Superficie_Rios


print (" {0:.1f}".format (Densidad_Ríos))
print (" {0:.1f}".format (Densidad_Magallanes))

censo2017 = dict(
    ID_Región1 = "14",
    Nombre1 = "Los Ríos",
    Superficie_Km2_1 = "18.429",
    Habitantes_2017_1 = "404.432", 
    Densidad1 = "21.9",
    Capital1 = "Valdivia",
    Comunas1 = ("Río Bueno", "La Unión", "Paillaco"),
    Provincias1 = ("Ranco", "Valdivia"),

    ID_Región2 = "12",
    Nombre2 = "Magallanes",
    Superficie_Km2_2 = "1.328.291",
    Habitantes_2017_2 = "166.533",
    Densidad2 = "9.0",
    Capital2 = "Punta Arenas",
    Comunas2 = ("Cabo de Hornos", "Puerto Williams", "Porvenir"),
    Provincias2 = ("Antártica Chilena", "Magallanes", "Tierra del Fuego", "Última Esperanza"),
    )

print (censo2017)