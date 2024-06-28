"""Desarrollar un programa para cargar 5 notas. Validar que se encuentren entre 1 y 10. Al finalizar,
mostrar el promedio de las notas.  """

notas=0
cantidad=0
for i in range (5):
    nota = int(input("Ingresar nota"))
    while nota<0 or nota >10:
        nota=int(input("Ingresar nota"))
    cantidad+=1
    notas+=nota
promedio=notas/cantidad
print("El promedio de las notas es: ",promedio)