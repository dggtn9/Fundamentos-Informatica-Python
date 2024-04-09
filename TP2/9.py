"""Ejercicio 9: Una inmobiliaria paga a sus vendedores un salario de $50000, más una
comisión de $5000 por cada venta realizada, más el 5% del valor de las
ventas. Realizar un programa que imprima el número del vendedor y el
salario que le corresponde en un determinado mes. Se leen el número
del vendedor, la cantidad de ventas que realizó y el valor total de las
mismas."""
print("EJERCICIO 9 :")

numeroDeVendedor=int(input("Ingresa el numero del vendedor"))
cantidadDeVentas=int(input("Ingresa cantidad de ventas realizadas"))
valorVenta=int(input("Ingresa valor de la venta"))
salario= 50000*mes
porcentaje=(5 *100)/valorVenta
comisionPorVenta= 5000* cantidadDeVentas
if cantidadDeVentas>0:
    salarioTotal=salario+comisionPorVenta+porcentaje
    print("Su salario fue de:",salarioTotal)
else:
    print("No realizo una venta")

