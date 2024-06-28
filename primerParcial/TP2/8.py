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

