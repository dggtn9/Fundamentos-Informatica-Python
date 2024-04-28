"""Un taller de cerámica municipal desea realizar un informe de la actividad de los socios.
Por cada socio se ingresa el número de socio (valor entero entre 1000 y 10000), la categoría (C= cadete / M=mayores y V=vitalicios)
VALIDAR EL INGRESO DE ESTE DATO y el año en que el socio se dio de alta (valor entero mayor o igual a 1970 cuando el taller comenzó a trabajar).
El programa iniciará preguntando el ingreso por teclado de la categoría del socio, pudiendo finalizar la
 ejecución mediante la letra F en dicho ingreso de dato, y luego se pedirá el año actual.
Los cadetes abonan una cuota social de $500, mientras los mayores abonan $1000. Para los
socios vitalicios con más de 30 años de antigüedad en la institución tendrán bonificada las cuotas mientras
 aquellos que aún no cumplan esa antigüedad pagarán un valor de $50.
Se desea conocer:
1. Recaudación total actual del taller.
2. Cuantos socios vitalicios con más de 30 años tiene el taller.
3. Cual fue el año en que ingreso el primer cadete , asumir que este valor es único """

recaudacion = 0
cadete_1=True
socios_vitalicios=0
anio_actual = int(input("Ingresa anio actual: "))
categoria = input("Ingresa categoria: ")


while categoria !="C" and categoria != "M" and categoria !="V" and categoria!="F":
      categoria = input("Ingresa categoria, debe ser M,C o V : ")

while categoria != "F":
    numero_de_socio=int(input("Ingrese numero de socio: "))
    while numero_de_socio <1000 or numero_de_socio >10000:
        numero_de_socio=int(input("Ingrese numero de socio,debe ser entre 1000 y 10000: "))

    anio_de_alta = int(input("Ingresa anio de alta: "))
    while anio_de_alta < 1970:
        anio_de_alta = int(input("Ingresa anio de alta a partir de 1970: "))

    antiguedad = anio_actual-anio_de_alta

    if categoria == "M":
                    recaudacion = recaudacion + 1000
    elif categoria == "V" and antiguedad >= 30:
                    recaudacion = recaudacion + 50
                    socios_vitalicios += 1
    elif categoria == "C":
             recaudacion = recaudacion + 500
             if cadete_1==True:
               anio_primer_ingreso=anio_de_alta
             else:
              if anio_de_alta<anio_primer_ingreso:
                anio_primer_ingreso=anio_de_alta
                cadete_1=False

    categoria = input("Ingresa categoria, debe ser M,C o V : ")
    while categoria !="C" and categoria != "M" and categoria !="V" and categoria!="F":
      categoria = input("Ingresa categoria, debe ser M,C o V : ")





print("Recaudación total actual del taller es: ",recaudacion)
print("Cuantos socios vitalicios con más de 30 años tiene el taller: ",socios_vitalicios)
print("Año en que ingreso el primer cadete: ",anio_primer_ingreso)



