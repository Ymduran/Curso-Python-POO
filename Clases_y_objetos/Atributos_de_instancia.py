print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 06 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Atributos de instancia                                           * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")


class Estudiante:
    def __init__(self,
                 nombre: str,
                 temas_aprendidos: list[str]
                 ):
        def __init__(self, nombre):
            self.nombre = nombre
            self.temas_aprendidos = []

        def aprender_tema(self, tema:str) ->None:
            self.temas_aprendidos.append(tema)
            print(f"{self.nombre} aprendió {tema}")




class Profesor:
    def __init__(self,
                 nombre: str,
                 temas_dominados: list[str]
                 ):
        def __init__(self, nombre:str):
            self.nombre = nombre
            self.temas_dominados = []

        def dominar_tema(self, tema:str)->None:
            self.temas_aprendidos.append(tema)
            print(f"{self.nombre} enseñó {tema}")

        def teach_topic(self, no_tema:int) -> str:
            self.temas_dominados[no_tema] = input("Ingresa el tema: ")
            return self.temas_dominados[no_tema]


