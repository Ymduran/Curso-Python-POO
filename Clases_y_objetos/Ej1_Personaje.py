

class Personaje:
    """
        Clase que representa a un Personaje.
        Sus atributos son: no_id (atributo de clase), x, y y contador_id.
        Sus métodos son: __init__(), __str__(), aumentar_sueldo().
    """
    no_id = 1
    def __init__(self, x: int, y: int) ->None :
        self.x = x
        self.y = y
        self.contador_id = Personaje.contador_id
        Personaje.contador_id +=1
    def moverse(self, ordenes: str) -> None:



class Empleado:
    pass


    def aumentar_sueldo(self, porcentaje: float) -> None:
        """
        Se utiliza para aumentar el sueldo de acuerdo con un porcentaje.
        :param porcentaje: Porcentaje a incrementar el sueldo.
        """
        if porcentaje > 0:
            self.sueldo += self.sueldo * (porcentaje/100)
            print(f"El sueldo de {self.nombre} ahora es de {self.sueldo:,.2f}")

        else:
            print("No se aplicó ningún cambio, ya que por Ley, el sueldo no puede disminuir.")


    def __str__(self) -> str:
        """
        Se utiliza para definir la representación en cadena del empleado.
        :return: El objeto en forma de cadena.
        """
        return f"Empleado(id: {self.id_empleado}, Nombre: {self.nombre}, Sueldo: {self.sueldo:,.2f})"



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    # Ejemplo de uso de los atributos de clase.
    print("  -- Ejemplo de uso de los atributos de clase.")

    # Forma de acceder al atributo de clase.
    print(f"Atributo de clase: {Empleado.no_id = }")


    # Se crean varios objetos de la clase Empleado y se imprimen en consola.
    alberto = Empleado("Alberto Martínez", 1110.1)
    gerardo = Empleado("Gerardo Guerrero", 12_123.23)
    esteban = Empleado("Esteban Ramírez", 999.23)

    print()
    print("Se crean empleados:")
    print(alberto)
    print(gerardo)
    print(esteban)

    # Se muestra nuevamente el atributo de clase.
    print()
    print(f"Atributo de clase: {Empleado.no_id = }")


