print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 13 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Atributos de clase                                               * ")
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
     def __str__(self) -> str:
        return f"Empleado id = {self.id}, nombre: {self.nombre}, sueldo: {self.sueldo}"

if __name__ == '__main__':
    print(Empleado.__no_id__)
    empleado1 =  Empleado("Jezzini", 1700)
    empleado2 =  Empleado("Empleado no 2", 1400)
    print(Empleado.__no_id__)
    print(empleado1)
    print(empleado2)

