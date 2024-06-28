"""
RESOLVER CON LISTAS OBLIGATORIAMENTE, utilizar función de BUSQUEDA/ORDENAMIENTO según corresponda,
TODO SE RESUELVE UNICAMENTE CON LO VISTO EN CLASE.
NO SE PUEDEN USAR FUNCIONES PROPIAS DEL LENGUAJE.
Un consultorio odontológico que atiende únicamente en forma PARTICULAR trabaja con tres tipos de prácticas:
- EXTRACCIONES (CODIGO=E)
- TRATAMIENTO DE CONDUCTO (CODIGO =T)
- IMPLANTES (CODIGO=I)
- CONSULTA DE CONTROL (CODIGO =C)
Cada practica tiene un costo que el paciente abona:
EXTRACCIONES $10000, TRATAMIENTO DE CONDUCTO $15000, IMPLANTES $90000, CONSULTA DE CONTROL $5000
Cada vez que un paciente se atiende se ingresa:
• DNI (Valor entre 10000000 y 99999999) - UTILIZAR FUNCION validarEnRango QUE VALIDE EL INGRESO DE ESTE DATO
• Código de práctica.
• Edad del paciente (únicamente mayores a 21 años)
El registro de las atenciones finaliza con un DNI de paciente igual a -1.
Si algún paciente refiere una practica que no se ofrece indicar un error, se deberán guardar e informar al finalizar el listado de practicas rechazadas y a que DNI las solicito.
a. Informar el total recaudado por practica y el total general.
b. Informar la cantidad de prácticas de cada tipo se atendieron
c. Informar la edad del paciente más joven que se realizaron implantes.
"""

tratamiento=input("Ingrese E para extraccion,T para tratamiento conducto,I para implantes,C para consulta de control")

extracciones=1000
tratamiento_conducto=15000
implantes=90000
control=5000

def validar(inicial,final,texto)
    v=int(input(texto))