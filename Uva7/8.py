"""
Una escuela necesita conocer cuántos alumnos cumplen años en cada mes del año,
 con el propósito de ofrecerles un agasajo especial en su día.
 Desarrollar un programa que lea el número de legajo y fecha de nacimiento (día, mes y año)
  de cada uno de los alumnos que concurren a dicha escuela. La carga finaliza con un número de legajo igual a -1.
  Emitir un informe donde aparezca (mes por mes) cuántos alumnos cumplen años a lo largo del año.
  Mostrar también una leyenda que indique cuál es el mes con mayor cantidad de cumpleaños.


"""
def calcular_maximo(lista):
    maximo=lista[0]
    mes=1
    for i in range(1,len(lista)):
        if lista[i]>maximo:
            maximo=lista[i]
            mes=i+1
    return mes

def __main__():
    cumpleanios_por_mes=[0,0,0,0,0,0,0,0,0,0,0,0]

    legajo= int(input("Ingresa numero de legajo del alumno"))
    while legajo != -1:
        dia = int(input("ingresa numero de dia del mes"))
        while dia>31 or dia<1:
            dia = int(input("ingresa numero de dia del mes"))
        mes = int(input("ingresa numero del mes"))
        while mes > 31 or mes < 1:
            mes = int(input("ingresa numero del mes"))
        cumpleanios_por_mes[mes-1]+=1

        anio=int(input("Ingresa anio de nacimiento"))
        while anio<0 or anio>2024:
            anio = int(input("Ingresa anio de nacimiento"))
        legajo= int(input("Ingresa numero de legajo del alumno"))

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
    mes_con_mas_cumples=calcular_maximo(cumpleanios_por_mes)
    print("Numero de mes con mas cumples: ",mes_con_mas_cumples)
if __name__=="__main__":
    __main__()