"""Escribir un algoritmo que permita ingresar los números de legajo de los alumnos de un curso y su nota de examen final.
 El fin de la carga se determina ingresando un -1 en el legajo. Informar para cada alumno si aprobó o no el examen
 considerando que se aprueba con nota mayor o igual a 4. Se debe validar que la nota ingresada sea entre 1 y 10. Terminada
 la carga de datos, informar:


Cantidad de alumnos que aprobaron con nota mayor o igual a 4.
Cantidad de alumnos que desaprobaron el examen. Nota menor a 4.
Porcentaje de alumnos que están aplazados (tienen 1 en el examen).
"""
legajo = int(input("Ingresa tu legajo"))
mes=int(input("Ingresa mes"))
nota=int(input("Ingresa nota"))
promocionados=0
aprobados=0
reprobados=0
cantidad=0
while legajo!=-1:
    legajo = int(input("Ingresa tu legajo"))
    mes = int(input("Ingresa mes"))
    nota = int(input("Ingresa nota"))
    cantidad+=1
    if legajo <0:
        legajo = int(input("Ingresa tu legajo"))
    if  mes !=3 or mes !=6 or mes!=12 :
        mes=int(input("Ingresa mes"))
    if nota < 1 and nota > 10:
       nota=int(input("Ingresa nota"))
    if nota >=7:
        promocionados+=1
    if nota >=4:
       aprobados+=1
    if nota <4:
       reprobados+=1
       porcentaje_reprobados=reprobados/cantidad
else:
       print("Finaliza programa")

print("Promocionados:",promocionados)
print("aprobados: ",aprobados)
print("reprobados: ",reprobados)