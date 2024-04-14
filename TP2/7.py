"""Ejercicio 7:
Una persona invierte su capital en un banco y desea saber cuánto dinero
ganará en un mes, teniendo en cuenta que el banco paga 2% mensual.
¿Cuánto ganará en seis meses si deja su dinero invertido?"""
print("EJERCICIO 7 :")

capital=int(input("Ingrese su capital"))
mesesAInvertir= int(input("Ingrese el mes o meses a invertir"))

montoQuePagaElBanco= (((2 * 100)/capital) * mesesAInvertir) + capital

print("En ",mesesAInvertir,"ganaras: ",montoQuePagaElBanco)


