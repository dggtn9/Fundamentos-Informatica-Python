"""Ejercicio 10: Leer un período en segundos e imprimirlo expresado en días, horas,
minutos y segundos. Por ejemplo, 200000 segundos equivalen a 2 días,
7 horas, 33 minutos y 20 segundos."""
print("EJERCICIO 10 :")
segundos=int(input("Ingresa los segundos")
dias=segundos/60*60*24
horas=segundos/3600
minutos=segundos/60

print(dias," dias y ",horas," horas ",minutos," minutos")
