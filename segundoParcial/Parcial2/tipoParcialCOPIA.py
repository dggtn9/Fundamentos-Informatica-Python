"""
Una municipalidad quiere procesar las multas que generan los vehículos que tienen registrados, ya que
los vehículos que no tengan multas tendrán beneficios a futuro en el pago de impuestos."""

"""Sabemos que la municipalidad dispone de datos de como máximo 10000 vehículos registrados en su sistema.

Cada vehículo está asociado a un número de DNI de su titular.
 
Un titular puede tener más de un vehículo.
 
Como datos de inicio, se ingresarán el apellido, patente (String AA222BB por ejemplo) y el DNI del dueño del automóvil.

El ingreso de estos datos finaliza con el número de DNI -1.

(LA CARGA INICIAL DEBE RESOLVERSE DENTRO DE UNA FUNCION LLAMADA cargaInicial)
Luego se procesarán los datos de las multas que se generan en un día de procesamiento. De cada multa se ingresa:

• Velocidad_medida (Valor entero mayor a 0) UTILIZAR FUNCION INGRESA_VALIDA QUE VALIDE EL INGRESO DE ESTE DATO
• Patente
La carga de las multas finaliza con una velocidad -99
Si se ingresa alguna patente que no se encuentra dentro de los registrados informar
 NUMERO DE PATENTE y leyenda "PATENTE inexistente". – UTILIZAR FUNCION BUSQUEDA
Luego de procesar las multas informar:
a. Listado de Patentes que no presentan multas
b. Velocidad máxima que genero multa. (Se asume que es un valor único)
c. Listado de cantidad de multas por patente
MULTAS POR PATENTE
CANTIDAD MULTAS PATENTE
1 xxxxxx
2 xxxxxx
5 xxxxxx
15 xxxxxx
… xxxxxx
TOTAL de multas: XXXX
"""
def main():
    def cargaInicial(lista):
        dni =int(input("Ingresa tu dni o -1 para terminar el programa"))
        while dni!=-1:
            apellido=input("Ingresa apellido")
            patente=int(input("Ingresa numero de patente"))
            dni=int(input("Ingresa tu dni"))
            lista.append(patente)
    def busquedaSecuencial(lista,dato):
        i=0
        while i<len(lista) and lista[i]!=dato:
            i+=1
            if i<len(lista):
                return lista[i]
            else:
                return-1
    def imprimir(lista1,lista2,titulo,texto):
        print(titulo)
        print(texto)
        for i in range (len(lista1)):
            print(lista1[i],lista2[i])
    cant=0
    patentes=[]
    multas_por_patente=[]
    cargaInicial(patentes)
    velocidad_medida = int(input("Ingresa velocidad o -99 para salir"))
    while velocidad_medida!= -99:
        patente = int(input("Ingresa numero de patente"))
        velocidad_medida=int(input("Ingresa velocidad o -99 para salir"))
        if busquedaSecuencial(patentes,patente)==patente:
            if velocidad_medida>100:
                cant+=1
                multas_por_patente=[]
                multas_por_patente.append(cant)
            else:
                multas_por_patente = []
                multas_por_patente.append(0)
        else:
            print(patente,"PATENTE inexistente")
    def maximo(lista):
        i=0
        pos=0
        for i in range(len(lista)):
            if i==0 or lista[i]<valMin:
                valMin=lista[i]
                posMin=i
        return valMin


    print(patentes[busquedaSecuencial(multas_por_patente,0)])
    print("Velocidad maxima es:",maximo(multas_por_patente) )
    imprimir(patentes,multas_por_patente,"INFORME","MULTAS POR PATENTE" "CANTIDAD MULTAS PATENTE")
    print("TOTAL de multas: ", cant)





if __name__=="__main__":
    main()






