"""Ejercicio 5:

Tres personas invierten dinero para fundar una empresa (no necesariamente
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

