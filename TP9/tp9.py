print("TP9")
"""""Ejercicio 1: Leer los números de legajo de los alumnos de un curso y su nota de examen
final. El fin de la carga se determina ingresando un -1 como legajo. Se debe validar
que la nota ingresada esté entre 1 y 10. Terminada la lectura de datos, informar:
· Cantidad de alumnos que aprobaron con nota mayor o igual a 4
· Cantidad de alumnos que desaprobaron el examen. Nota menor a 4
· Promedio de nota y los legajos que superan el promedio
Luego se solicita mostrar un listado de legajos y calificaciones ordenado de manera
ascendente según el número de legajo. Resolver de dos formas: Utilizando
dos listas paralelas y utilizando una matriz de dos filas.
Ejercicio 2: Una Administradora de Consorcios necesita un sistema para poder gestionar el
cobro de las expensas de un edificio de departamentos de 20 unidades. En dos
listas almacena la siguiente información: Número de unidad y superficie en metros
cuadrados. Validar que no se ingresen números de unidades duplicadas. Cada
unidad paga de expensas un valor fijo por metro cuadrado, el que se ingresa
por teclado. Se pide:
· Informar el promedio de expensas del mes.
· Ordenar los listados de mayor a menor según la superficie. Mostrar por
pantalla el listado ordenado informando el número de unidad y la superficie
en metros cuadrados.
Ejercicio 3: Hora de jugar: Desarrollar un programa que genere un número entero al azar de
cuatro cifras y le proponga al usuario que lo descubra, ingresando valores repetidamente
hasta hallarlo. En cada intento el programa mostrará mensajes indicando
si el número ingresado es mayor o menor que el valor secreto. Permitir que el
usuario abandone la partida al ingresar -1. Al terminar el juego informar la cantidad
de intentos realizada, haciendo que el usuario ingrese su número de documento
si mejoró la mejor marca de intentos obtenida hasta el momento. Luego
mostrar la lista ordenada de los 5 mejores puntajes (indicando también a quién
pertenecen) y preguntar si se desea jugar otra vez, reiniciando el juego en caso
afirmativo.
Ejercicio 4: Modificar el programa anterior para que las pistas brindadas por el programa no
sean del tipo "es mayor" o "es menor" sino "M dígitos correctos y N dígitos
aproximados". Se considera que un dígito es correcto cuando tanto su valor
como su posición coinciden con los del número secreto, mientras que un dígito
es aproximado cuando coincide el valor, pero no su posición. Ejemplos:
Número secreto: 5739
· Intento 1: 1234 -> 1 correcto
· Intento 2: 5678 -> 1 correcto y 1 aproximado
· Intento 3: 9375 -> 4 aproximados
Ejercicio 5: Ingresar por teclado un número N y construir una lista llamada SECUENCIAS con
N números enteros al azar entre 1 y 20. Esta lista se caracterizará porque sus
valores deben encontrarse divididos en secuencias de números separadas por
ceros, cuya suma no sea mayor que 20. Para eso se deberá agregar un elemento
de valor 0 a fin de separar cada secuencia de la siguiente, cuidando que ninguna
secuencia sume más de 20. Agregar un 0 adicional al final de la lista y mostrar la
lista obtenida por pantalla. Ejemplo:
Valor de N ingresado: 11
Números al azar generados: 5, 2, 9, 6, 4, 15, 3, 19, 12, 1, 5
Lista SECUENCIAS construida:
5 2 9 0 6 4 0 15 3 0 19 0 12 1 5 0
Ejercicio 6: A partir de la lista SECUENCIAS generada en el ejercicio anterior, imprimir la
secuencia más larga almacenada en la misma. Si hubiera varias secuencias con
la misma longitud máxima deberán mostrarse todas las que correspondan."""







for i in range(42,177,-1):
    if i%2!=0:
        print(i)


