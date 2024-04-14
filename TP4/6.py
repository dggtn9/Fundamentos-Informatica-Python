"""Ejercicio 6: Mostrar la tabla de multiplicar (entre 1 y 12) del número 4. ¿Cómo cambiaría el
algoritmo para que el usuario pueda decidir la tabla de multiplicar a mostrar?"""



tabla = int(input("Ingrese numero del que desea mostrar su tabla de multiplicar:"))

for i in range (1,12+1):

    print(tabla*i)