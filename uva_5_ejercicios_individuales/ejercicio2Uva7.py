"""
Una escuela necesita conocer cuántos alumnos cumplen años en cada mes, con el propósito de ofrecerles un agasajo especial en su día.
 Desarrollar un programa que lea el nombre, día y mes de cumpleaños de cada uno de los alumnos que concurren a dicha escuela.
 La carga finaliza ingresando una cadena vacía en el nombre del alumno (es decir, presionando solo la tecla ENTER).
  A medida que se ingresan los datos se deberá ir cargando en una lista (podría usar 2 también si lo considera necesario)
  la cantidad de cumpleaños por mes, según los datos ingresados en el programa hasta ese momento.
Al finalizar, deberá imprimir el contenido de esa lista/s, de forma tal de informar cuántos alumnos cumplen años según el mes.
"""


cumpleanios_por_mes=[0,0,0,0,0,0,0,0,0,0,0,0]

alumno = input("Ingresa nombre de alumno")
while alumno != "":
    dia = int(input("ingresa numero de dia del mes"))
    while dia>31 or dia<1:
        dia = int(input("ingresa numero de dia del mes"))
    mes = int(input("ingresa numero del mes"))
    while mes > 31 or mes < 1:
        mes = int(input("ingresa numero del mes"))
    cumpleanios_por_mes[mes-1]+=1
    alumno = input("Ingresa nombre de alumno")
print("Enero: ",cumpleanios_por_mes[0])
print("Febrero: ",cumpleanios_por_mes[1])
print("Marzo: ",cumpleanios_por_mes[2])
print("Abril: ",cumpleanios_por_mes[3])
print("Mayo: ",cumpleanios_por_mes[4])
print("Junio: ",cumpleanios_por_mes[5])
print("Julio: ",cumpleanios_por_mes[6])
print("Agosto: ",cumpleanios_por_mes[7])
print("Septiembre: ",cumpleanios_por_mes[8])
print("Octubre: ",cumpleanios_por_mes[9])
print("Noviembre: ",cumpleanios_por_mes[10])
print("Diciembre: ",cumpleanios_por_mes[11])



