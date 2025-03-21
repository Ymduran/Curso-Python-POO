print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 19 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Relaciones entre objetos                                         * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

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




class Empresa:
    def __init__(self, nombre: str, *empleados: list[Empleado]):
        self.nombre = nombre
        self.empleados = list(empleados)


    def agregar_empleados(self, *nuevos_empleados : Empleado) -> None:
        for empleado in list(nuevos_empleados):
            self.empleados.append(empleado)

    def __str__(self) -> str:
        empleados = ", ".join(str(empleado) for empleado in self.empleados)
        return f"Empresa({self.nombre = }, {empleados})"


# Se crean varios empleados.
martin = Empleado("Martín", 1110.1)
roger = Empleado("Roger", 1123.23)
eleuterio = Empleado("Eleuterio Guadalupe", 30000)


print(" Empleados.")
print(martin)
print(roger)


# Se crea la empresa con dos empleados y se llama al métod0 mostrar_empleados().
unsij = Empresa("Universidad de la Sierra Juárez", eleuterio,martin)
print(eleuterio)


