"""Ejercicio 4: Ingresar las notas de los dos parciales de un alumno e indicar si promocionó,
aprobó o si debe recuperar. Informar un error si el valor de alguna nota no está
entre 0 y 10.
· Se promociona cuando las notas de ambos parciales son mayores o
iguales a 7.
· Se aprueba cuando las notas de ambos parciales son mayores o iguales
a 4.
· Se debe recuperar cuando al menos una de las dos notas es menor a 4."""

print("Ejercicio 4")
parcialUno=int(input("Ingrese su nota del parcial 1"))
parcialDos=int(input("Ingrese su nota del parcial 2"))
if parcialUno & parcialDos <=10:
   if parcialUno & parcialDos >=7:
     print("Promociona")
   elif parcialUno & parcialDos >=4:
     print("aprueba")
   elif parcialUno <4 & parcialDos<4 :
     print("Debe recursar")
   else:
       print("Debe recuperar")
