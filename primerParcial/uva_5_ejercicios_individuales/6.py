"""Leer tres números D, M y A correspondientes al día, mes y año de una fecha, y un número entero N que representa
una cantidad de días. Realizar un programa que imprima la nueva fecha que resulta de sumar N días a la fecha dada.
 Tener en cuenta los años bisiestos tal como se detalla en el ejercicio 7 de la práctica de estructura condicional
 de la UVA 4. """


n=int(input("Ingrese dias a sumar: "))
bisiesto=366
no_bisiesto=365
d=int(input("dia del anio: "))
while d >31 or d<0:
   d=int(input("Ingrese dia: "))
m=int(input("Ingrese mes: "))
while m >12 or m<1:
    m = int(input("Ingrese mes: "))
a=int(input("Ingrese anio: "))
while a<=0:
    a = int(input("Ingrese anio: "))

anios_a_sumar=int(n/no_bisiesto)
nuevo_anio=int(a+anios_a_sumar)
resto=int(n%no_bisiesto)
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    meses_a_sumar=int(resto/31)
    dias_a_sumar = int(resto % 31)
    dias_extra = (dias_a_sumar + d)-31

elif m==4 or m==6 or m==9 or m==11:
    meses_a_sumar = int(resto / 30)
    dias_a_sumar = int(resto % 30)
    dias_extra = (dias_a_sumar + d) - 30
else:
    if a%4==0:
        if m==2:
            meses_a_sumar = int(resto / 29)
            dias_a_sumar = int(resto % 29)
            dias_extra = (dias_a_sumar + d) - 29
    else:
        if m==2:
            meses_a_sumar = int(resto / 28)
            dias_a_sumar = int(resto % 28)
            dias_extra = (dias_a_sumar + d) - 28
if dias_extra>0:
    nuevo_dia = dias_extra
    meses_a_sumar+=1

else:
    nuevo_dia = dias_a_sumar+d

nuevo_mes=meses_a_sumar+m
if nuevo_mes > 12:
    nuevo_mes= nuevo_mes-12
    nuevo_anio+=1


print("nuevo dia",nuevo_dia)
print(" nuevo mes ",round(nuevo_mes))
print("nuevo anio",round(nuevo_anio))











