"""Ejercicio 12: La sucesión de Fibonacci es una sucesión de números enteros donde cada término
se obtiene como suma de los dos anteriores, siendo los dos primeros 0 y 1.
Por lo tanto, Fib=0, 1, 1, 2, 3, 5, 8, 13, 21.... Realizar un programa que lea N e
imprima los N primeros términos de esta sucesión, como así también la suma de
los mismos."""


n=(int(input("Ingresa un numero")))
suma=0
for i in range (0,n+1):
    suma = +i
    print(suma)
    print(i)


print(suma)