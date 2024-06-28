"""Ejercicio 2: Escribir un programa que permita ingresar los números de legajo de los alumnos
de un curso y su nota de examen final.

El fin de la carga se determina ingresando un -1 en el legajo.

Informar para cada alumno si aprobó o no el examen considerando
que se aprueba con nota mayor o igual a 4.

Se debe validar que la nota ingresada sea entre 1 y 10. Terminada la carga de datos, informar:
· Cantidad de alumnos que aprobaron con nota mayor o igual a 4.
· Cantidad de alumnos que desaprobaron el examen con nota menor a 4.
· Porcentaje de alumnos que están aplazados (tienen 1 en el examen)."""

numero_legajo=int(input("Ingrese su numero de legajo"))
cantidad_alumnos_aprobados=0
cantidad_alumnos_desaprobados=0
cantidad_alumnos_aplazados=0
cantidad_alumnos=0
while numero_legajo !=-1:
    nota_final = int(input("Ingrese su nota final"))
    cantidad_alumnos+=1
    if nota_final>=1 and nota_final<=10:
        if nota_final >=4:
            cantidad_alumnos_aprobados+=1
        elif nota_final<4:
            cantidad_alumnos_desaprobados+=1
        elif nota_final == 1:
            cantidad_alumnos_aplazados +=1
        else:
            print("Error")
    numero_legajo = int(input("Ingrese su numero de legajo"))



print("Cantidad de alumnos que aprobaron con nota mayor o igual a 4: ",cantidad_alumnos_aprobados)
print("Cantidad de alumnos que desaprobaron el examen con nota menor a 4: ",cantidad_alumnos_desaprobados)
print("Porcentaje de alumnos que están aplazados (tienen 1 en el examen): ",(cantidad_alumnos_aplazados*100)/cantidad_alumnos)
