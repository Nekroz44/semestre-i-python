habitantes_rios = 404432
superficie_rios = 18429
habitantes_magallanes = 166533
superficie_magallanes = 1382291

densidad_ríos = habitantes_rios / superficie_rios
densidad_magallanes = habitantes_magallanes / superficie_rios


print (" {0:.1f}".format (densidad_ríos))
print (" {0:.1f}".format (densidad_magallanes))

censo2017 = dict(
    id_región1 = "14",
    nombre1 = "Los Ríos",
    
    id_región2 = "12",
    nombre2 = "Magallanes",
    )

censo2017 ["densidad1":densidad_ríos][0][1]
censo2017 ["densidad2"] = densidad_magallanes
print (censo2017)