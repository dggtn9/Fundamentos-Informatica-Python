"""Una escuela necesita conocer cuántos alumnos cumplen años en cada mes del
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

def main():
    def validarRango(inicial,final,texto):
        v=int(input(texto))
        while v<inicial or v>final:
            v = int(input(texto))
        return v

    def validarRangoconExcepcion(ini,final,exce,texto):
        v = int(input(texto))
        while (v < ini or v >final)and v != exce:
            v = int(input(texto))
        return v
    def mayorA(inicial,texto):
        v = int(input(texto))
        while v < inicial:
            v = int(input(texto))
        return v
    def valorMaximo(lista):
        for i in range (len(lista)):
            if i==0 or lista[i]>valMax:
                valMax=lista[i]
                posMax=i
            return valMax
    def metodoPorBurbujeo(meses, cumples):
        for i in range(len(meses) - 1):
            for j in range(len(meses) - 1 - i):
                if cumples[j] > cumples[j + i]:
                    aux = cumples[j]
                    cumples[j] = cumples[j + 1]
                    cumples[j + 1] = aux

                    aux = meses[j]
                    meses[j] = meses[j + 1]
                    meses[j + 1] = aux
    def listado_cumples(meses, cumples):
        print("LISTADO DE CANTIDAD DE CUMPLEANOS")
        print('MES,"   ",CANTIDAD')
        for i in range(len(meses)):
            print(meses[i], cumples[i])


    cumples=[0]*12
    meses=[1,2,3,4,5,6,7,8,9,10,11,12]
    nroLegajo=validarRangoconExcepcion(1000,9999,-1,"Ingresa nro de legajo,recuerda que son 4 cifras o -1 para salir")
    while nroLegajo !=-1:
        print("Ahora vas a escribir tu fecha de nacimiento")
        dia=int(input(validarRango(1,30,"Ingresa el dia")))
        mes=int(input("Ingresa el mes"))
        anio=int(input(mayorA(2000,"Ingresa el anio")))

        cumples[mes-1]+=1
        nroLegajo = validarRangoconExcepcion(1000, 9999, -1, "Ingresa nro de legajo,recuerda que son 4 cifras")
    metodoPorBurbujeo(meses,cumples)
    print(cumples)
    print(meses)
    print(listado_cumples(meses, cumples))
    print("El mes con mayor cantidad de cumpleaños es: ",valorMaximo(cumples))

if __name__=="__main__":
    main()

