print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 03 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Persona                                                          * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

class Persona: # Para definir una clase, la primera letra es en mayúscula.

    # Para tener a una "Persona" se debe construir:
    # Mét odo constructor.
    def __init__(self, # "self" se refiere a un mismo objeto.
                 nombre: str,
                 edad: int,
                 altura: float,
                 peso: float):

        self.nombre = nombre # Se asigna al nombre del propio objeto.
        self.edad = edad
        self.altura = altura
        self.peso = peso


# Métodos.
    def caminar(self) -> None:
        print(f" {self.nombre} está caminando para bajar sus {self.peso} kg")

    def comer(self) -> None:
        print(f"¡{self.nombre} está  comiendo para tener energía a sus {self.edad} años!")


    def jugar(self) -> None:
        print(f"¡{self.nombre} está  jugando!")

    def dormir(self) -> None:
        print(f"¡{self.nombre} está  durmiendo!")

if __name__ == '__main__':
    # Para crear a una persona:
    yam = Persona("Yam", 19, 1.59, 62.2 )
    print(yam.nombre)
    print(yam.edad)
    print(yam.altura)
    print(yam.peso)
    yam.caminar()
    yam.comer()
    yam.jugar()
    yam.dormir()
    print()

    companero = Persona("El Compañero", 19, 1.7, 70)
    companero.caminar()
    companero.comer()
    companero.jugar()
    companero.dormir()

    yam.edad = 20
    yam.peso = 62.30
    print(yam.nombre)
    print(yam.edad)
    print(yam.altura)
    print(yam.peso)
