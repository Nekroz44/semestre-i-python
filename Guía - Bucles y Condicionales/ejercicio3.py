###EJERCICIO 3###

hora_diu = 12000
hora_noc = 16000
turno_sem_diu = hora_diu + 2000
turno_sem_noc = hora_noc + 3000
hora_diu_dom = 14000
hora_diu_noc = 19000

pago_diario_diu = hora_diu * 10
pago_diario_noc = hora_noc * 10 
pago_diario_diu_dom = hora_diu_dom * 10
pago_diario_noc_dom = hora_diu_noc * 10

empleado1 = {
 "lunes1": "",
 "martes1": "",
 "miercoles1": "",
 "jueves1": "",
 "viernes1": "",
 "semanal1": ""
}

empleado1['lunes1'] = pago_diario_noc
empleado1["martes1"] = pago_diario_noc
empleado1["miercoles1"] = pago_diario_noc
empleado1["jueves1"] = pago_diario_diu
empleado1["viernes1"] = pago_diario_diu
empleado1["semanal1"] = empleado1["lunes1"] + empleado1["martes1"] + empleado1["miercoles1"] + empleado1["jueves1"] + empleado1["viernes1"]

empleado2 = {
 "martes2": "",
 "miercoles2": "",
 "jueves2": "",
 "domingo2": "",
 "semanal2": ""
}

empleado2["martes2"] = pago_diario_noc
empleado2["miercoles2"] = pago_diario_noc
empleado2["jueves2"] = pago_diario_noc
empleado2["domingo2"] = pago_diario_diu_dom
empleado2["semanal2"] = empleado2["martes2"] + empleado2["miercoles2"] + empleado2["jueves2"] + empleado2["domingo2"]

empleado3 = {
 "miercoles3": "",
 "jueves3": "",
 "viernes3": "",
 "sabado3": "",
 "domingo3": "",
 "semanal3": "",
}

empleado3["miercoles3"] = pago_diario_diu
empleado3["jueves3"] = pago_diario_diu
empleado3["viernes3"] = pago_diario_diu
empleado3["sabado3"] = pago_diario_noc
empleado3["domingo3"] = pago_diario_noc_dom
empleado3["semanal3"] = empleado3["miercoles3"] + empleado3["jueves3"] + empleado3["viernes3"] + empleado3["sabado3"] + empleado3["domingo3"]

print(empleado1)
print(empleado2)
print(empleado3)