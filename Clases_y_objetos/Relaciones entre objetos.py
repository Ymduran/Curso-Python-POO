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
    __no_id__: int = 1
    def __init__(self, nombre:str,sueldo: float):
        self.nombre = nombre
        self.sueldo = sueldo
        self.id = Empleado.__no_id__
        Empleado.__no_id__ += 1

    def aumentar_sueldo(self, porcentaje: float) -> None:
        pass

    def __str__(self) -> str:
        return f"Empleado(id: {self.id}, Nombre: {self.nombre}, Sueldo: {self.sueldo:,.2f})"

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

if __name__ == '__main__':
    print(Empleado.__no_id__)
    empleado1 =  Empleado("Jezzini", 1700)
    empleado2 =  Empleado("Empleado no 2", 1400)
    print(Empleado.__no_id__)
    print(empleado1)
    print(empleado2)
    unsij = Empresa("unsij", empleado1)
    unsij.agregar_empleados(empleado2)
    print(unsij)


