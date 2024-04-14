
"""Ejercicio 11:Un banco necesita para sus cajeros automáticos un programa que lea
una cantidad de dinero e imprima a cuántos billetes equivale, considerando
que existen billetes de $1000, $500, $100, $50, $10, $5 y $1.
Desarrollar dicho programa de tal forma que se minimice la cantidad de
billetes entregados por el cajero."""
print("EJERCICIO 11 :")

monto=int(input("Ingrese cantidad de dinero: "))
billetesDeMil=monto//1000
resto=monto%1000
billete_de_500=resto//500
resto=resto%500
billete_de_200=resto//200
resto=resto%200
billete_de_100=resto//100
resto=resto%100
billete_de_50=resto//50
resto=resto%50
billete20=resto//20
resto=resto%20
moneda10=resto//10
resto=resto%10
moneda5=resto//5
resto=resto%5
moneda2=resto//2
resto=resto%2
moneda1=resto//1
resto=resto%1

print("billete de 1000:",billetesDeMil)
print("billete de 500: ",billete_de_500)
print("billete de 200",billete_de_200)
print("billete de 100:",billete_de_100)
print("billete de 50",billete_de_50)
print("billete de 20",billete20)
print("moneda de 10:",moneda10)
print("moneda de 5:",moneda5)
print("moneda de 2:",moneda2)
print("moneda de 1:",moneda1)


