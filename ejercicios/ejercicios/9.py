"""Hacer un programa que calcule si el saldo actual que tenemos en la tarjeta nos alcanza para hacer x
viajes en un dia.
Para eso:
El usuario debe ingresar saldo actual de la tarjeta.
Luego se le va a pedir por cada viaje, el monto a pagar. La carga termina con un monto igual o menor a 0"""


saldo_actual=float(input("Ingresa saldo actual "))
monto_a_pagar_por_viaje=float(input("Ingresa monto a pagar por viaje"))
while monto_a_pagar_por_viaje <0:
    monto_a_pagar_por_viaje=float(input("Ingresa monto a pagar por viaje"))

while monto_a_pagar_por_viaje!=0 :
    saldo_actual = saldo_actual - monto_a_pagar_por_viaje
    monto_a_pagar_por_viaje = float(input("Ingresa monto a pagar por viaje"))
    while monto_a_pagar_por_viaje < 0:
        monto_a_pagar_por_viaje = float(input("Ingresa monto a pagar por viaje"))


if saldo_actual <0:
        print("Es imposible realizar ese viaje con el saldo actual.")
else:
        print("Es posible hacer el viaje,el saldo va a ser de: ",saldo_actual)

"""Ejemplo:
El usuario ingresa un saldo de 200.
Luego el usuario ingresa:
100
50
-1

El resultado deberia ser:
Es posible hacer el viaje
El saldo va a ser de 50

En caso de que no nos alcance el saldo el resultado debe ser:
Es imposible realizar ese viaje con el saldo actual de <saldo_original>.
"""












