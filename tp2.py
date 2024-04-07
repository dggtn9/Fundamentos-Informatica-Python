print("TP2")
""""Ejercicio 1: Calcular el valor de las siguientes expresiones, respetando el orden de operaciones
establecido.
a. 12 * 4 + 4 * 5
b. (12 * (1 - 5) + 4) * 3
c. 12 * 1 - 5 + 4 * 3
d. (17 - 2) / 5
e. 3 + 2 * 2 - (8 * 4 + 1 / 2.0) * 3
f. 5 * 4 / 2
g. 5 * (4 / 2)
h. 24 / 2 ** 2
i. (24 / 2) ** 2
j. 3 + 4 * 6 / 2 – 5
k. 3 + 4 * 6 / (2 – 5)
l. (- 0.1) * 3
m. – 9 ** 2
n. (– 9) ** 2
o. 10 / 3
p. 10 // 3
q. 12 % 5"""

"""Ejercicio 2: Desarrollar un programa que permita ingresar dos números enteros A y
B a través del teclado. Imprimir su suma y su diferencia."""
print("EJERCICIO 2 :")
numeroUno=int(input("Ingrese un numero entero"))
numeroDos=int(input("Ingrese un numero entero"))
resta= numeroUno-numeroDos
suma=numeroUno+numeroDos
print("el resultado de la suma es:",suma)
print("el resultado de la resta es:",resta)
"""Ejercicio 3: Calcular el promedio de las notas que obtiene un alumno al rendir los dos
parciales."""
print("EJERCICIO 3 :")
parcial1=int(input("Ingresa tu nota del parcial 1"))
parcial2=int(input("Ingresa tu nota del parcial 2"))
promedio = (parcial2+parcial1)/2
print("Promedio de tus notas es: ",promedio)

"""Ejercicio 4: Escribir un programa que permita ingresar la edad de una persona en
años y la convierta a días, imprimiendo el resultado. Considerar que todos
los años tienen 365 días."""
print("EJERCICIO 4 :")
edad=int(input("Ingresa tu edad en anios"))
edadEnDias= edad*365
print("Tu edad en dias es:",edadEnDias)

"""Ejercicio 5: Tres personas invierten dinero para fundar una empresa (no necesariamente
en partes iguales). Calcular qué porcentaje invirtió cada una."""
print("EJERCICIO 5 :")
persona1=float(input("Ingrese valor a invertir"))
persona2=float(input("ingrese valor a invertir"))
persona3=float(input("Ingrese valor a invertir"))
total=persona1+persona2+persona3
porcentajePersona1= (persona1*100)/total
print("Persona 1 invirtio",round(porcentajePersona1),"%")
porcentajePersona2=(persona1*100)/total
print("Persona 2 invirtio",round(porcentajePersona2),"%")
porcentajePersona3=(persona1*100)/total
print("Persona 3 invirtio",round(porcentajePersona3),"%")

"""Ejercicio 6: Ingresar tres números enteros, calcular su promedio y mostrarlo por
pantalla."""
print("EJERCICIO 6 :")

numero1=int(input("Ingresa un numero entero"))
numero2=int(input("ingresa un numero entero"))
numero3=int(input("Ingresa un numero entero"))

promedio=round(numero1+numero2+numero3)/3

print("Promedio es:",promedio)

"""Ejercicio 7: Una persona invierte su capital en un banco y desea saber cuánto dinero
ganará en un mes, teniendo en cuenta que el banco paga 2% mensual.
¿Cuánto ganará en seis meses si deja su dinero invertido?"""
print("EJERCICIO 7 :")

capital=int(input("Ingrese su capital"))
mesesAInvertir= int(input("Ingrese el mes o meses a invertir"))

montoQuePagaElBanco= (((2 * 100)/capital) * mesesAInvertir) + capital

print("En ",mesesAInvertir,"ganaras: ",montoQuePagaElBanco)


"""Ejercicio 8: Leer una medida en metros e imprimir esta medida expresada en centímetros,
pulgadas, pies y yardas. Los factores de conversión son:
· 1 pie = 12 pulgadas
· 1 yarda = 3 pies
· 1 pulgada = 2,54 cm.
· 1 metro = 100 cm."""
print("EJERCICIO 8 :")
medidaEnMetros=float(input("Medida en metros: "))
cms= medidaEnMetros*100
pulgadas= medidaEnMetros/2.54
pies= pulgadas/12
yardas= pies/3
print("Medida en cms: ",cms)
print("Medida en pulgadas: ",pulgadas)
print("Medida en pies: ",pies)
print("Medida en yardas: ",yardas)

"""Ejercicio 9: Una inmobiliaria paga a sus vendedores un salario de $50000, más una
comisión de $5000 por cada venta realizada, más el 5% del valor de las
ventas. Realizar un programa que imprima el número del vendedor y el
salario que le corresponde en un determinado mes. Se leen el número
del vendedor, la cantidad de ventas que realizó y el valor total de las
mismas."""
print("EJERCICIO 9 :")
numeroDeVendedor=
mes=
salario=
cantidadDeVentas=
valorDeLasVentas=
"""Ejercicio 10: Leer un período en segundos e imprimirlo expresado en días, horas,
minutos y segundos. Por ejemplo, 200000 segundos equivalen a 2 días,
7 horas, 33 minutos y 20 segundos."""
print("EJERCICIO 10 :")
segundos=int(input("Ingresa los segundos")
dias=
horas=
minutos=

"""Ejercicio 11:Un banco necesita para sus cajeros automáticos un programa que lea
una cantidad de dinero e imprima a cuántos billetes equivale, considerando
que existen billetes de $1000, $500, $100, $50, $10, $5 y $1.
Desarrollar dicho programa de tal forma que se minimice la cantidad de
billetes entregados por el cajero."""
print("EJERCICIO 11 :")


"""Ejercicio 12: Escribir un programa para convertir un número binario de 4 cifras en un
número decimal. El número binario se ingresa como un solo número
entero de cuatro dígitos.
Procedimiento: Para convertir un número binario a decimal es necesario
multiplicar el valor de cada dígito por el número 2 elevado a un exponente.
Este exponente se obtiene de la posición que ocupa el dígito
dentro del número, comenzando desde la derecha con la posición 0. Todos
estos resultados se suman para obtener el valor final. Ejemplo: Convertir
1011 a decimal:
13 02 11 10 = 1 * 23 + 0 * 22 + 1 * 21 + 1 * 20 = 11"""
print("EJERCICIO 12 :")
binario("ingrese numero binario como un solo número entero de cuatro dígitos: ")
