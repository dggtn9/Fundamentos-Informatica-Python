"""
Una cadena de servicio de combustible desea realizar una estadística diaria de sus ventas.
Se dispone del precio de cada uno de los productos que comercializa.
Ingresar los precios de los productos mediante una función de CargaPrecios conociendo que los códigos de combustible van de 1 a 10.
Cada vez que se realiza una carga de combustible en un determinado día, se tiene la siguiente información:
 Código del combustible (1 a 10) – utilizar funcion ingresaValidaRango
 Cantidad de litros cargados (mayor a cero) utilizar funcion mayorA
 Forma de Pago ( ‘E’ (Efectivo) o ‘T’(Tarjeta)) utilizar funcion ingresaFPago
Esta información termina con Código de combustible cero."""

"""
OJO!!!!-->Cuando la forma de pago es con Tarjeta hay un incremento del 5% sobre el total de la venta.
Con las informaciones anteriores, realizar e informar el siguiente resumen:
1-) Un listado donde indique la recaudación según combustible con el formato.
RECAUDACION según COMBUSTIBLE
CODIGO COMBUSTIBLE RECAUDACION
1 xxxxxx.xx
2 xxxxxx.xx
: :
10 xxxx.xx
Utilizar para el informe la función ListadoCombustible
2-) Cantidad de pagos con tarjeta.
3-) Mínima cantidad de litros cargados, indicando código de combustible. (Se considera único
"""

def main():

    def ingresaValidaRango(inicial,final,excepcion,texto):
        v=int(input(texto))
        while v<inicial or v>final and v!=excepcion:
            v=int(input(texto))
        return v
    def validar(inicial, final, texto):
        v = int(input(texto))
        while v < inicial or v > final:
            v = int(input(texto))
        return v
    def cargaPrecios(lista):
        precios_por_producto=va
        codigos_por_combustible=ingresaValidaRango(1,10,0,"")


while codigo_por_producto!=0:


if __name__=="__main__":
    main()