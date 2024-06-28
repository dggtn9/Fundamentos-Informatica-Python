"""Escribir un algoritmo que permita ingresar los números de legajo de los alumnos de un curso y su nota de examen final.
El fin de la carga se determina ingresando un -1 en el legajo.
Informar para cada alumno si aprobó o no el examen considerando que se aprueba con nota mayor o igual a 4.
Se debe validar que la nota ingresada sea entre 1 y 10. Terminada la carga de datos, informar:


Cantidad de alumnos que aprobaron con nota mayor o igual a 4.
Cantidad de alumnos que desaprobaron el examen. Nota menor a 4.
Porcentaje de alumnos que están aplazados (tienen 1 en el examen). """

cantidad_aprobados=0
cantidad_desaprobados=0
cantidad=0
cantidad1=0
notas=0
legajo=int(input("Ingresa numero de legajo"))
while legajo !=-1:
    nota = int(input("Ingrese nota"))
    cantidad+=1
    while nota<1 and nota>10:
        nota=int(input("Ingrese nota"))
    if nota>=4:
        cantidad_aprobados+=1
    elif nota == 1:
        cantidad1+=1
    else:
        cantidad_desaprobados+=1

    legajo = int(input("Ingresa numero de legajo"))
porcentaje1=(cantidad1/cantidad)*100

print("Cantidad aprobados: ",cantidad_aprobados)
print("Cantidad desaprobados: ",cantidad_desaprobados)
print("Porcentaje con 1: ",porcentaje1)



