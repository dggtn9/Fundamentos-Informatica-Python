"""
Ejercicio 9: Escribir una función que reciba como parámetros un número de día, un número
de mes y un número de año y devuelva la cantidad de días que faltan hasta fin
de mes.

 Luego desarrollar tres programas para:
· Ingresar una fecha formada por tres enteros (día, mes y año) e imprimir
la cantidad de días que faltan hasta fin de año.
· Ingresar una fecha formada por tres enteros (día, mes y año) e imprimir
la cantidad de días transcurridos en ese año hasta esa fecha.
· Ingresar dos fechas formadas por tres enteros (día, mes y año) e imprimir
cuánto tiempo transcurrió entre ambas, expresando el resultado en
años, meses y días.
Los tres programas deben realizar su trabajo a través de la función indicada al
comienzo.

"""
def es_bisiesto(a):
       return  a % 4 == 0 and (a % 100 != 0 or a % 400 == 0)
def calcular_dias_del_mes(m,a):
    d=0
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        d=31
    elif m == 4 or m == 6 or m == 9 or m == 11:
        d=30
    else:
        if m == 2:
            if es_bisiesto(a):
               d=29
            else:
                d=28
    return d
def calcular_dias_que_faltan(d,m,a):

    dias_que_faltan=calcular_dias_del_mes(m,a)-d
    return dias_que_faltan




"""Ingresar una fecha formada por tres enteros (día, mes y año) e imprimir
la cantidad de días que faltan hasta fin de año.

d=int(input("Ingresa dia"))
m=int(input("Ingresa mes"))
a=int(input("Ingresa anio"))

dias_faltantes = calcular_dias_que_faltan(d,m,a)
mes_actual=m+1

while mes_actual<=12:
    dias_faltantes=calcular_dias_del_mes(mes_actual, a) + dias_faltantes
    mes_actual = mes_actual + 1

print("Dias que faltan para llegar a fin de anio: ",dias_faltantes)

#Se incluye la fecha final e el calculo"""



"""Ingresar una fecha formada por tres enteros (día, mes y año) e imprimir
la cantidad de días transcurridos en ese año hasta esa fecha.

d=int(input("Ingresa dia"))
m=int(input("Ingresa mes"))
a=int(input("Ingresa anio"))

mes_actual=m
dias_transcurridos = d
for i in range (1,mes_actual):
    dias_transcurridos += calcular_dias_del_mes(i, a)


print("Dias que transcurrieron en el anio: ",dias_transcurridos)"""



"""Ingresar dos fechas formadas por tres enteros (día, mes y año) e imprimir
cuánto tiempo transcurrió entre ambas, expresando el resultado en
años, meses y días.
"""

def calcular_dias_para_fin_de_anio(d,m,a):
    dias_faltantes = calcular_dias_que_faltan(d, m, a)
    mes_actual = m + 1

    while mes_actual <= 12:
        dias_faltantes = calcular_dias_del_mes(mes_actual, a) + dias_faltantes
        mes_actual = mes_actual + 1
    return dias_faltantes

def calcular_dias_transcurridos(d,m,a):
    mes_actual = m
    dias_transcurridos = d
    for i in range(1, mes_actual):
        dias_transcurridos += calcular_dias_del_mes(i, a)
    return dias_transcurridos

d=int(input("Ingresa dia"))
m=int(input("Ingresa mes"))
a=int(input("Ingresa anio"))

d2=int(input("Ingresa dia"))
m2=int(input("Ingresa mes"))
a2=int(input("Ingresa anio"))

dias_entre_fechas = 0

anio_inicial = a
dia_inicial = d
mes_inicial = m

anio_objetivo = a2

dias_transcurridos = calcular_dias_transcurridos(d2,m2,a2)

while anio_inicial < anio_objetivo:
    dias_entre_fechas += calcular_dias_para_fin_de_anio(dia_inicial, mes_inicial, anio_inicial)
    anio_inicial += 1

dias_entre_fechas+=dias_transcurridos
print(dias_entre_fechas)




