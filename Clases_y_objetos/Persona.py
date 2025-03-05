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
    # Para tener a una "Persona" se debe contruir.
    def __init__(self, nombre: str, edad: int, altura: float, peso: float): # "self" se refiere a un mismo objeto.
        self.nombre = nombre # Se asigna al nombre del propio objeto.
        self.edad = edad
        self.altura = altura
        self.peso = peso

# Métodos.
    def caminar(self) -> None:
        print("¡Estoy caminando!")

    def comer(self) -> None:
        print("¡Estoy comiendo!")

    def jugar(self) -> None:
        print("¡Estoy jugando!")

    def dormir(self) -> None:
        print("¡Estoy durmiendo!")

if __name__ == '__main__':
    # Para crear a una persona.
    yam = Persona("Yam", 19, 1.59, 62.2 )
    print(yam.nombre)
    print(yam.edad)
    print(yam.altura)
    print(yam.peso)
    print()

    yam.caminar()
    yam.comer()
    yam.jugar()
    yam.dormir()

