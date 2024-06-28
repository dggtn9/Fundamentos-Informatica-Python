"""
Una escuela necesita conocer cuántos alumnos cumplen años en cada mes del
año, con el propósito de ofrecerles un agasajo especial en su día. Desarrollar un
programa que lea el
- número de legajo (4 digitos) y
- fecha de nacimiento (día (1-30),mes (1-12)y año (>2000))

de cada uno de los alumnos que concurren a dicha escuela.
La carga finaliza con un número de legajo igual a -1.

Emitir un informe ordenado por cantidad de cumpleanos de forma
ascendente donde aparezca -mes por mes-
cuántos alumnos cumplen años a lo largo del año.

LISTADO DE CANTIDAD DE CUMPLEANOS
MES    CANTIDAD
XX        X
X         X
..        ..
XX        XX

Imprimir también una leyenda
que indique cuál es el mes con mayor cantidad de cumpleaños"""
import random


def listadoCumples(liMe, liCu):
    print("LISTADO DE CANTIDAD DE CUMPLEANOS")
    print("MES\tCANTIDAD")
    for i in range(len(liMe)):
        print("%3d\t%4d" % (liMe[i], liCu[i]))


def maximo(lista):
    for i in range(len(lista)):
        if i == 0 or lista[i] > valMax:
            valMax = lista[i]
            posMax = i
    return posMax


def ingresaValidaRango(li, ls, texto):
    valor = int(input(texto))
    while valor < li or valor > ls:
        valor = int(input(texto))
    return valor


def ordenamiento(liMe, LiCu):
    for i in range(len(liMe) - 1):
        for j in range(len(liMe) - 1 - i):

            if LiCu[j] > LiCu[j + 1]:
                aux = LiCu[j]
                LiCu[j] = LiCu[j + 1]
                LiCu[j + 1] = aux

                aux = liMe[j]
                liMe[j] = liMe[j + 1]
                liMe[j + 1] = aux


def main():
    MESES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    CUMPLES = [0] * 12

    legajo = int(input("Ingrese un legajo,-1 para fin"))
    while (legajo < 1000 or legajo > 9999) and legajo != -1:
        legajo = int(input("Ingrese un legajo,-1 para fin"))

    while legajo != -1:
        dia = ingresaValidaRango(1, 30, "Ingrese dia de nacimiento")

        mes = ingresaValidaRango(1, 12, "Ingrese mes de nacimiento")

        anio = int(input("Ingrese anio de nacimiento"))

        while anio <= 2000:
            anio = int(input("Ingrese anio de nacimiento"))

        # voy a actualizar la lista de cumpleanos
        CUMPLES[mes - 1] += 1

        legajo = int(input("Ingrese un legajo,-1 para fin"))
        while (legajo < 1000 or legajo > 9999) and legajo != -1:
            legajo = int(input("Ingrese un legajo,-1 para fin"))

    print(MESES)
    print(CUMPLES)

    # Listado ordenado por CUMPLEANOS
    ordenamiento(MESES, CUMPLES)
    print(MESES)
    print(CUMPLES)
    listadoCumples(MESES, CUMPLES)

    # mes con mayor cantidad de cumpleaños
    posicionMaximo = maximo(CUMPLES)
    print("El mes con mas cumpleanos es ", MESES[posicionMaximo])

    # como la lista esta ordenada ascendente --> ES VALIDO!!
    print("El mes con mas cumples es ", MESES[-1])
    # print("El mes con mas cumples es ", MESES[len(MESES)-1])


if __name__ == "__main__":
    main()
