#En una carrera de ciclistas participan N competidores
#donde N se ingresa por teclado.

"""Desarrollar un programa que permita cargar, por cada competidor, su
número y el tiempo de carrera en horas, minutos y segundos. """

"""Luego se solicita:
Mostrar el número del ganador de la carrera y el tiempo que empleó.
Ingresando por teclado el tiempo record registrado para dicha carrera,
informar si el ganador batió el record anterior.
Calcular y mostrar el tiempo promedio entre todos los ciclistas.
Los ciclistas se identifican con números enteros, no necesariamente correlativos.
"""

def validar(valor,texto):
    x=int(input(texto))
    while x<=valor:
        x=int(input(texto))
    return x
   
def minimo(lista):
    minimo=lista[0]
    for i in range(1,len(lista)):
        if lista[i]<minimo:
            minimo=lista[i]
            pos=i
    return pos

numeros=[]
tiempoSegundos=[]
tiempoTotal=0
cantidadCompetidores=validar(0,"Ingresa cantidad de competidores")
for i in range(cantidadCompetidores):
    numeroCompetidor=int(input("Ingresa numero del competidor"))
    numeros.append(numeroCompetidor)
    print("Ahora vas a ingresar el tiempo")
    hora=int(input("Ingresa hora"))
    segundosHora=hora*3600
    minutos=int(input("Ingresa minutos"))
    segundosMinutos=minutos*60
    segundos=int(input("Ingresa segundos"))
    tiempo=segundos+segundosMinutos+segundosHora
    tiempoTotal+=tiempo
    tiempoSegundos.append(tiempo)
   
   
tiempoPromedio= tiempoTotal/cantidadCompetidores
print("Ahora vas a ingresar el tiempo record de la carrera anterior")
hora1=int(input("Ingresa hora"))
segundosHora1=hora*3600
minutos1=int(input("Ingresa minutos"))
segundosMinutos1=minutos*60
segundos1=int(input("Ingresa segundos"))
tiempo1=segundos+segundosMinutos+segundosHora

tiempoRecordCarreraAnterior=tiempo1

posicionMinimo=minimo(tiempoSegundos)
tiempoGanador=tiempoSegundos[posicionMinimo]

horaGanador=tiempoGanador//3600
residuo=tiempoGanador%3600
minutosGanador=residuo//60
residuo1=residuo%60
segundos=residuo1

if tiempoGanador<tiempoRecordCarreraAnterior:
    print("Batio tiempo record")
else:
    print("No batio tiempo record")

print("Numero del ganador es: ",numeros[posicionMinimo])
print("Tiempo ganador es: ",horaGanador,"horas",minutosGanador,"minutos",segundos,"segundos")

print("tiempo promedio en segundos es: ",tiempoPromedio) 