"""
Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:
Aplica el precio base a la primera docena de unidades. 
Aplica un 10% de descuento a todas las unidades entre 13 y 100. 
Aplica un 25% de descuento a todas las unidades por encima de las 100. 
Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100. El cálculo resultante sería: 
100 * 12 + 90 * 88 + 75 * 130 = 18870, y el precio promedio será 18870 / 230 = 82,04 
Escribir un algoritmo que lea la cantidad solicitada de un producto y su precio base, y muestre el valor total de la venta y el precio promedio por unidad. El fin de carga se determina ingresando -1 como cantidad solicitada. 
Al finalizar informar: 
Cantidad de ventas realizadas total. 
Cantidad de ventas que se aplicaron un 10% de descuento. 
Cantidad de ventas que SOLO se aplicó el precio base, a los productos que no se le realizaron descuentos. """