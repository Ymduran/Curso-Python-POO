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

# Definición de la clase Estudiante
class Estudiante:
    def __init__(self, nombre: str, temas_aprendidos: list[str] = None):
        self.nombre = nombre
        self.temas_aprendidos = temas_aprendidos if temas_aprendidos is not None else []

    def aprender_tema(self, tema: str) -> None:
        self.temas_aprendidos.append(tema)
        print(f"{self.nombre} aprendió {tema}")
    def __str__(self) -> str:
        return f"Estudiante(nombre: {self.nombre}, temas aprendidos: {self.temas_aprendidos})"


# Definición de la clase Profesor
class Profesor:
    def __init__(self, nombre: str, temas_dominados: list[str] = None):
        self.nombre = nombre
        self.temas_dominados = temas_dominados if temas_dominados is not None else []

    def dominar_tema(self, tema: str) -> None:
        self.temas_dominados.append(tema)
        print(f"{self.nombre} dominó el tema {tema}")

    def teach_topic(self, no_tema: int) -> str:
        #tema = input("Ingresa el tema que vas a enseñar: ")
        #self.temas_dominados.append(tema)
        #print(f"{self.nombre} añadió el tema {tema} a su lista.")
        print(f"no tema: {no_tema}")
        print(f"len(self.temas_dominados) {len(self.temas_dominados)}")
        if no_tema < len(self.temas_dominados):
            return self.temas_dominados[no_tema]
        else:
            return "Fuera de rango"


    def __str__(self) -> str:
        return f"Profesor (nombre: {self.nombre}, temas aprendidos: {self.temas_dominados})"


if __name__ == '__main__':
    estudiante1 = Estudiante("Yamm")
    estudiante2 = Estudiante("Estudiante 2")
    estudiante1.aprender_tema("Evolución sitios web")
    estudiante2.aprender_tema("Internet de las cosas")
    print()
    print(estudiante1)
    print()
    print(estudiante2)
    print()
    profesor1 = Profesor("Profesor")
    profesor1.dominar_tema("Class")
    profesor1.dominar_tema("Objets")
    profesor1.dominar_tema("Math")
    profesor1.teach_topic(2)
    print(profesor1)

    tema1 = profesor1.teach_topic((1))
    estudiante1.aprender_tema(tema1)
    estudiante2.aprender_tema(tema1)

    #Dicho de otra forma
    #estudiante2.aprender_tema(profesor1.teach_topic(2))

    print(estudiante1)
    print(estudiante2)



