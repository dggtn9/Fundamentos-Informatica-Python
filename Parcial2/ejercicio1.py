"""#Realizar Python
# Escribir una función para ingresar números
# enteros en una lista y devolverla como valor de
# retorno.
# La cantidad de valores a leer se recibe como
# parámetro."""

def cargarLista(cantidad):
    lista=[]
    for i in range(cantidad):
        numero=int(input("Ingrese un numero \n"))
        lista.append(numero)
    return lista

