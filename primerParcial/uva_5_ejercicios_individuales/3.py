"""
Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:
Aplica el precio base a la primera docena de unidades. 
Aplica un 10% de descuento a todas las unidades entre 13 y 100. 
Aplica un 25% de descuento a todas las unidades por encima de las 100. 
Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100. El cálculo resultante sería: 
100 * 12 + 90 * 88 + 75 * 130 = 18870, y el precio promedio será 18870 / 230 = 82,04 
Escribir un algoritmo que lea la cantidad solicitada de un producto y su precio base, y muestre el valor total de la venta
y el precio promedio por unidad.
El fin de carga se determina ingresando -1 como cantidad solicitada.
Al finalizar informar: 
Cantidad de ventas realizadas total. 
Cantidad de ventas que se aplicaron un 10% de descuento. 
Cantidad de ventas que SOLO se aplicó el precio base, a los productos que no se le realizaron descuentos. """


cantidad_producto=int(input("Ingrese cantidad solicitada"))
cantidad_ventas_diez_descuento=0

cantidad_ventas_sin_descuento=0
ventas_base=0

while cantidad_producto!=-1:
    producto_entre_13_y_100 = cantidad_producto - 12
    precio_base = float(input("ingrese precio"))
    producto_encima_100 = (producto_entre_13_y_100 - 100)
    cantidad_ventas_encima_100 = 0
    diez_por_ciento = (precio_base * 10) / 100
    veinticinco_por_ciento = (precio_base * 25) / 100

    if cantidad_producto <=12:
       ventas_base= cantidad_producto *precio_base
       cantidad_ventas_sin_descuento+=1
    if producto_entre_13_y_100 >12 and producto_entre_13_y_100<100:
       venta_diez=producto_entre_13_y_100*diez_por_ciento
       cantidad_ventas_diez_descuento +=1
    if producto_encima_100 == 0:
       cantidad_ventas_encima_100+=1
       venta_veinticinco=producto_encima_100*veinticinco_por_ciento
    cantidad_producto=int(input("Ingrese cantidad solicitada"))
    if venta_veinticinco!=0 and venta_diez!=0 and ventas_base!=0:
       valor_total_venta=(venta_veinticinco+venta_diez+ventas_base)
    if cantidad_ventas_sin_descuento!=0 and cantidad_ventas_diez_descuento!=0 and cantidad_ventas_encima_100!=0:
       cantidad_ventas_realizadas_total=(cantidad_ventas_encima_100+cantidad_ventas_sin_descuento+cantidad_ventas_diez_descuento)
precio_promedio_por_unidad= valor_total_venta/cantidad_ventas_realizadas_total
print("valor total de la venta: ",valor_total_venta)
print("precio promedio por unidad: ",precio_promedio_por_unidad)
print("Cantidad de ventas realizadas total: ",cantidad_ventas_realizadas_total)
print("Cantidad de ventas que se aplicaron un 10% de descuento",cantidad_ventas_diez_descuento)
print("Cantidad de ventas que SOLO se aplicó el precio base, a los productos que no se le realizaron descuentos: ",cantidad_ventas_sin_descuento)
