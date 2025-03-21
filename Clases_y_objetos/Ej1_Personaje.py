print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 13 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Personaje que se desplaza en coordenadas (x,y)                   * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

#Clase personaje
class Personaje:
    """
    Esta clase representa a un personaje, el cuál puede moverse en dos dimensiones mediante coordenadas.
    Tiene un contador_id para que cada personaje tenga un id diferente.
    Las posiciones se representan con las coordenas x (horizontal) y y (vertical).
    Métodos: __init__(), moverse(), posicion_actual(), __str__().
    """

    # Atributo de clase
    contador_id = 1 #Se inicializa en 1

    def __init__(self):
        """
        El constructor inicia la posición del personaje en (0,0)
        También un contador que aumenta id en 1
        """
        self.x = 0
        self.y = 0
        self.id = Personaje.contador_id
        Personaje.contador_id += 1




    def moverse(self, ordenes: str) -> None:
        """
        función moverse, mueve al personaje según la tecla que se presione.
        :param ordenes: como cadena de caracteres con las letras que indican el movimiento.
        """

        for orden in ordenes:
            if orden in ("A","a") and self.y < 10:
                self.y += 1
            elif orden in ("R","r") and self.y > 0:
                self.y -= 1
            elif orden in ("D","d") and self.x < 10:
                self.x += 1
            elif orden in ("I","i") and self.x > 0:
                self.x -= 1
            elif orden in ("S","s"):
                print("Saliendo...")
                break





    def posicion_actual(self) -> None:
        """
        Muestra la posición actual del personaje
        """
        print(f"Posición actual del Personaje {self.id}: ({self.x}, {self.y})")


    def __str__(self) -> str:
        """
        El str es una representación del objeto Personaje
        :return: Una cadenaa con el id y la posición del personaje
        """
        return f"Personaje(id: {self.id}, Posición: ({self.x}, {self.y}))"


if __name__ == "__main__":

    personaje_yam = Personaje() #Se crea a el primer personaje


    while True:
        personaje_yam.posicion_actual()
        ordenes = input("Ingresa las ódenes de moviento: ")
        if "S" in ordenes or "s" in ordenes:
            break
        personaje_yam.moverse( ordenes)


    print("Posición final del personaje:")
    personaje_yam.posicion_actual()



