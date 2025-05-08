"""
Cree una función que convierta dólares estadounidenses (USD) a yuanes chinos (CNY).
La entrada es la cantidad en USD como un entero y la salida debe ser una cadena que indique la cantidad
en yuanes seguida de "Yuan chino".

Ejemplos (Entrada -> Salida)

15  -> '101.25 Chinese Yuan'
465 -> '3138.75 Chinese Yuan'

El tipo de cambio que debe usar es 6,75 CNY por cada USD.
Todos los números deben representarse como una cadena con dos decimales (p. ej., "21,00" NO "21,0" ni "21").
"""

def usdcny(usd:int) -> str:
    """
    Esta función convierte los doláres a Yuan chino, multiplicando cada dolar por su equivalencia en 'Chinese Yuan' que es 6.75
    :param usd:
    :return: Regresa un str con la conversión dentro de la horación
    """
    return f"{(usd * 6.75):.2f} Chinese Yuan"


if __name__ == '__main__':
    print(usdcny(15))
    print(usdcny(465))

