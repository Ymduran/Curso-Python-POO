
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 13 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Personaje que se desplaza                                        * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

""" %%%%%%%     Clase    %%%%%%%%%%%%%%%%%%%%% """
class Personaje:
    """
    Clase que representa a un personaje en un videojuego.
    Atributos de clase: contador_id (para asignar IDs únicos).
    Atributos de instancia: x, y (posición en la ventana), id.
    Métodos: __init__(), moverse(), posicion_actual(), __str__().
    """

    # Atributo de clase
    contador_id = 1

    def __init__(self):
        """
        Constructor que inicializa la posición del personaje en (0, 0)
        y le asigna un ID único.
        """
        self.x = 0
        self.y = 0
        self.id = Personaje.contador_id
        Personaje.contador_id += 1

    def moverse(self, ordenes: str) -> None:
        """
        Mueve al personaje según las órdenes dadas.
        :param ordenes: Cadena de caracteres con las direcciones de movimiento.
        """
        for orden in ordenes:
            if orden in ('A', 'a') and self.y < 10:
                self.y += 1
            elif orden in ('R', 'r') and self.y > 0:
                self.y -= 1
            elif orden in ('D', 'd') and self.x < 10:
                self.x += 1
            elif orden in ('I', 'i') and self.x > 0:
                self.x -= 1
            elif orden in ('S', 's'):
                print("Programa detenido.")
                break

    def posicion_actual(self) -> None:
        """
        Muestra la posición actual del personaje.
        """
        print(f"Posición actual del Personaje {self.id}: ({self.x}, {self.y})")

    def __str__(self) -> str:
        """
        Representación en cadena del objeto Personaje.
        :return: Cadena con el ID y la posición del personaje.
        """
        return f"Personaje(id: {self.id}, Posición: ({self.x}, {self.y}))"


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    print("  -- Simulación de movimientos de un personaje --")

    personaje = Personaje()

    while True:
        personaje.posicion_actual()
        ordenes = input("Ingresa las ódenes de moviento: ")
        if 'S' in ordenes or 's' in ordenes:
            break
        personaje.moverse(ordenes)

    print("\nPosición final del personaje:")
    personaje.posicion_actual()

##################################


