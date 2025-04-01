"""
Jugador.py
"""
"""
class Torneo:
    def __init__(self, nombre: str, equipos: list[Equipo]):

"""

class Jugador:
    """
    Atributos:
        _nombre: Nombre del jugador (protegido).
        _numero: Número del jugador (protegido).
        _goles: Cantidad de goles anotados por el jugador (protegido).
    Métodos:
        __init__(nombre: str, numero: int, goles: int = 0): Constructor para inicializar los atributos.
        nombre, numero, goles: Métodos de acceso para obtener y modificar los atributos.
        anotar_goles(no_goles: int): Mét0do para incrementar la cantidad de goles anotados.
        __str__(): Mét0do para mostrar la información del jugador.
    """
    def __init__(self, nombre: str, numero: int, goles: int = 0):
        self._nombre = nombre
        self._numero = numero
        self._goles = goles

    def anotar_goles(self, no_goles: int) -> None:
        self._goles += no_goles
        print(f"Actualizando Número de goles... ")
        print(f"Goles = {self._goles}")


    def __str__(self) -> str:
        return f"Nombre: {self._nombre} | Número = {self._numero} | Goles = {self._goles}"



        @property
        def nombre(self) -> str:
            return self._nombre
        @nombre.setter
        def nombre(self, value: str):
            self._nombre = value


        @property
        def numero(self) -> int:
            return self._numero
        @numero.setter
        def numero(self, value: int):
            self._numero = value

        @property
        def goles(self) -> int:
            return self._goles
        @goles.setter
        def goles(self, value: int):
            self._goles = value





"""

"""



""" %%%%%%%     Clase    %%%%%%%%%%%%%%%%%%%%% """
class Empleado:
    """
    Clase que representa a un empleado.
    Sus atributos son: no_id (atributo de clase), nombre y sueldo.
    Sus métodos son: __init__(), __str__(), aumentar_sueldo().
    """

    no_id = 1   # Id del empleado.

    def __init__(self, nombre: str, sueldo: float):
        """
        Constructor del empleado.
        :param nombre: Nombre del empleado.
        :param sueldo: Sueldo mensual del empleado.
        """
        self.nombre = nombre
        self.sueldo = sueldo
        self.id_empleado = Empleado.no_id
        Empleado.no_id += 1


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
        return f"Empleado(id: {self.id_empleado}, Nombre: {self.nombre}, Sueldo: {self.sueldo:,.2f})"



""" %%%%%%%     Clase    %%%%%%%%%%%%%%%%%%%%% """
class Empresa:
    """
    Clase que representa a una empresa.
    Sus atributos son: nombre y lista de empleados.
    Sus métodos son: __init__(), __str__(), agregar_empleados(), remover_empleados(),
                     aumentar_sueldo_empleados(), mostrar_empleados().
    """
    def __init__(self, nombre: str, *empleados: Empleado):
        """
        Constructor de la clase que representa una empresa.
        :param nombre: Nombre de la empresa.
        :param empleados: Los empleados (*vargs) que forman parte de la empresa.
        """
        self.nombre = nombre
        self.empleados = list(empleados)


    def agregar_empleados(self, *nuevos_empleados: Empleado) -> None:
        """
        Se utiliza para agregar más empleados (*vargs) a la empresa.
        :param nuevos_empleados: Los empleados (*vargs) que se agregan a la empresa.
        """
        for empleado in list(nuevos_empleados):
            self.empleados.append(empleado)


    def remover_empleados(self, *empleados_a_remover: Empleado) -> None:
        """
        Se utiliza para remover un empleado de la empresa.
        :param empleados_a_remover: Empleado a remover de la empresa.
        """
        for empleado in empleados_a_remover:
            if empleado in self.empleados:
                self.empleados.remove(empleado)

            else:
                print(f"El empleado {empleado} no forma parte de {self.nombre}.")


    def aumentar_sueldo_empleados(self, porcentaje: float) -> None:
        """
        Se utiliza para aumentar el sueldo a todos los empleados de acuerdo con un porcentaje.
        :param porcentaje: Porcentaje a incrementar el sueldo.
        """
        for empleado in self.empleados:
            empleado.aumentar_sueldo(porcentaje=porcentaje)


    def mostrar_empleados(self) -> None:
        """
        Se utiliza para mostrar los empleados de la empresa en forma de lista.
        """
        print(f"*** Lista de empleados de {self.nombre} ***")

        for empleado in self.empleados:
            print(empleado)


    def __str__(self) -> str:
        """
        Se utiliza para mostrar los empleados de la empresa en forma de lista.
        """
        # Se convierte los elementos de la lista en cadenas (invocando str() para cada uno de ellos) y
        # se unen con ", " a través del métod0 str.join().
        # Este patrón es muy común en Python para obtener una cadena a partir de una lista.
        empleados = ", ".join(str(empleado) for empleado in self.empleados)
        return f"Empresa({self.nombre = }, {empleados})"



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":

    # Se crean varios empleados.
    alberto = Empleado("Alberto Martínez", 1110.1)
    gerardo = Empleado("Gerardo Guerrero", 12_123.23)
    esteban = Empleado("Esteban Ramírez", 999.23)
    esmeralda = Empleado("Esmeralda Cerqueda", 1000.99)

    print("  -- Se crean empleados y se imprimen en consola.")
    print(alberto)
    print(gerardo)
    print(esteban)
    print(esmeralda)


    # Se crea la empresa con dos empleados y se llama al métod0 mostrar_empleados().
    unsij = Empresa("Universidad de la Sierra Juárez",alberto, gerardo)

    print()
    print("  -- Se crea la empresa con dos empleados.")
    unsij.mostrar_empleados()


    # Se agregan y remueven empleados de la empresa.
    print()
    print("  -- Se agregan y remueven empleados.")

    unsij.agregar_empleados(esteban, esmeralda)
    unsij.remover_empleados(alberto)
    unsij.mostrar_empleados()


    # Se aumenta el sueldo a todos los empleados. Además, se muestra a todos los empleados
    # (incluyendo el que no forma parte de la empresa) para observar los cambios.
    print()
    print("  -- Se aumenta el sueldo de todos los empleados.")
    unsij.aumentar_sueldo_empleados(porcentaje=3)
    unsij.mostrar_empleados()
    print("Empleado que no forma parte de la empresa:")
    print(alberto)
"""































