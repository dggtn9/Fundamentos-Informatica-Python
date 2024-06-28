"""
Una municipalidad quiere procesar las multas que generan los vehículos que tienen registrados, ya que
los vehículos que no tengan multas tendrán beneficios a futuro en el pago de impuestos.
Sabemos que la municipalidad dispone de datos de como máximo 10000 vehículos registrados en su sistema. Cada vehículo está asociado a un número de DNI de su titular. Un titular puede tener más de un vehículo.
Como datos de inicio, se ingresarán el apellido, patente (String AA222BB por ejemplo) y el DNI del dueño del automóvil. El ingreso de estos datos finaliza con el número de DNI -1.
(LA CARGA INICIAL DEBE RESOLVERSE DENTRO DE UNA FUNCION LLAMADA cargaInicial)
Luego se procesarán los datos de las multas que se generan en un día de procesamiento. De cada multa se ingresa:
• Velocidad medida (Valor entero mayor a 0) UTILIZAR FUNCION INGRESA_VALIDA QUE VALIDE EL INGRESO DE ESTE DATO
• Patente
La carga de las multas finaliza con una velocidad -99
Si se ingresa alguna patente que no se encuentra dentro de los registrados informar NUMERO DE PATENTE y leyenda "PATENTE inexistente". – UTILIZAR FUNCION BUSQUEDA
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
# VERSION 1: La funcion modifica una lista existente y vacia inicialmente
    def cargaInicial(patentes):

        dni = int(input("Ingrese su dni de 8 digitos o -1 para finalizar"))
        while dni != -1:
            apellido = input("Ingrese su apellido")
            patente = input("Ingrese patente")
            patentes.append(patente)
            dni = int(input("Ingrese su dni de 8 digitos o -1 para finalizar"))

    """
    # VERSION 2: La funcion crear y retorna la lista
    def cargaInicial():
        patentes = []
        dni = int(input("Ingrese su dni de 8 digitos o -1 para finalizar"))
        while dni != -1:
            apellido = input("Ingrese su apellido")
            patente = input("Ingrese patente")
            patentes.append(patente)
            dni = int(input("Ingrese su dni de 8 digitos o -1 para finalizar"))
    
        return patentes
    
    """

    def buscar_patente(patente_buscada, patentes):
        posicion = -1
        indice = 0
        while posicion == -1 and indice < len(patentes):
            if patente_buscada == patentes[indice]:
                posicion = indice
            indice += 1
        return posicion

    def imprimir_multas_por_patente(multas, patentes):
        print("\tMULTAS POR PATENTE\t")
        print("CANTIDAD MULTAS", " ", "PATENTE")
        for i in range(len(patentes)):
            print(multas[i], " ", patentes[i])

    #-----------------------------------------------------------------------------------

    # INICIALIZACION DE VARIABLES
    patentes = []
    multas_por_patente = [0] * 10000
    total_de_multas = 0
    velocidad_mas_alta = 0

    # patentes = cargarInicial2()

    # CARGA DE DATOS
    cargaInicial(patentes)

    # PROGRAMA
    velocidad_medida = int(input("Ingresar velocidad (> 0) 0 -99 para terminar: "))
    while velocidad_medida < 0 and velocidad_medida != -99:
        velocidad_medida = int(input("Ingresar velocidad (> 0) 0 -99 para terminar: "))

    while velocidad_medida != -99:

        patente = input("Ingresar patente. Ej.: AA222EE")
        indice_patente = buscar_patente(patente, patentes)
        if  indice_patente != -1:

            if velocidad_medida > 100:
                multas_por_patente[indice_patente] += 1
                total_de_multas+=1
                if velocidad_medida > velocidad_mas_alta:
                    velocidad_mas_alta = velocidad_medida
        else:
            print(f"{patente} INEXISTENTE")

        velocidad_medida = int(input("Ingresar velocidad (> 0) 0 -99 para terminar"))
        while velocidad_medida < 0 and velocidad_medida != -99:
            velocidad_medida = int(input("Ingresar velocidad (> 0) 0 -99 para terminar"))

    # MULTAS POR PATENTES
    imprimir_multas_por_patente(multas_por_patente, patentes)
    print("La velocidad mas alta en generar multa fue: ", velocidad_mas_alta)
    print("Total de multas es: ", total_de_multas)

if __name__=="__main__":
    main()