"""Ejercicio 3:
Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:
· Aplica el precio base a la primera docena de unidades.
· Aplica un 10% de descuento a todas las unidades entre 13 y 100.
· Aplica un 25% de descuento a todas las unidades por encima de las 100.
#Escribir un programa que lea la cantidad solicitada de un producto y su precio base,

#muestre el valor total de la venta y el precio promedio por unidad.
#El fin de carga se determina ingresando -1 como cantidad solicitada.
#informar:
# Cantidad de ventas realizadas total.
# Cantidad de ventas en las que se aplicó un 10% de descuento.
#Cantidad de ventas en las que SOLO se aplicó el precio base, es decir que no se le realizaron descuentos."""

cantidad=int(input("Cantidad solicitada de un producto"))
precio_base=int(input("Ingrese el precio base del producto"))
precio=cantidad * precio_base



cantidad_total_con_descuento_25=(cantidad-100) -(cantidad-12)
venta_con_25_desc=((cantidad_total_con_descuento_25*precio_base)*0.25)+(cantidad_total_con_descuento_25*precio_base)

cantidad_total_con_descuento_10=(cantidad_total_con_descuento_25-12)
venta_con_10_desc=((cantidad_total_con_descuento_10*precio_base)*0.25)+(cantidad_total_con_descuento_10*precio_base)



print("Cantidad de ventas realizadas con 10%descuento ",cantidad_total_con_descuento_10)
print("Cantidad de ventas realizadas con 25%descuento ",cantidad_total_con_descuento_25)



"""Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio
base es 100. El cálculo resultante sería:
100 * 12 + 90 * 88 + 75 * 130 = 18870
y el precio promedio es de 18870/230 = 82.04"""