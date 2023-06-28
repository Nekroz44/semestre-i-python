#RETO 2 (02/05/2023)

a=input("Nombre del estudiante: ")
b=input("Nombre de la asignatura: ")
c= float(input("Nota Laboratorio 1: "))
d= float(input("Nota Laboratorio 2: "))

e = (c * 0.3) + (d * 0.7)

dic = {
    "student_name": a,
    "student_subject": b,
    "fist_note": c,
    "second_note": d,
    "promedy": round(e, 1)
}

print(f"Datos ingresados: {dic}")
