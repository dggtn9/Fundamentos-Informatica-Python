"""Ejercicio 5:

Una editorial determina el precio de un libro según la cantidad de páginas que
contiene. El costo básico del libro es de $500, más $3,20 por página con encuadernación
rústica. Si el número de páginas supera las 300 la encuadernación
debe ser en tela, lo que incrementa el costo en $200. Además, si el número de
páginas sobrepasa las 600 se hace necesario un procedimiento especial de encuadernación
que incrementa el costo en otros $336. Desarrollar un programa
que calcule el costo de un libro dado el número de páginas."""

paginas =int(input("Ingrese numero de paginas"))
costo= (paginas * 3.20) + 500

if paginas >1:
   if paginas > 600:
    costo = costo + 336

   elif paginas > 300:
    costo = costo + 200

print("Tu libro cuesta:",costo)






