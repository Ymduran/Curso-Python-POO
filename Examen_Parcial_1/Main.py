
from colorama import Fore
from Codedex.guess import jugadores, torneo
from Examen_Parcial_1.Jugador import Jugador
from Examen_Parcial_1.Equipo import Equipo
from Examen_Parcial_1.Torneo import Torneo


"""
Se requiere diseñar una interfaz en consola (menú) que permita:
Crear nuevos jugadores y equipos, solicitando los datos requeridos para cada objeto.
Ver lista de jugadores y equipos, mostrando la lista de todos los objetos. 
Agregar jugadores a algún equipo. En este caso, se debe mostrar un submenú que indique los jugadores para seleccionar, luego otro submenú que indique a qué equipo se quiere añadir. Nota: No se considera el caso de que un jugador pertenezca a dos equipos.
Eliminar jugadores de un equipo. En este caso, se debe mostrar un submenú con la lista de equipos, después de seleccionar a alguno de ellos, se debe de mostrar la lista de jugadores a eliminar del equipo.
Agregar equipos al torneo. En este caso, se debe mostrar un submenú que indique los equipos a añadir al torneo. 
Nota: no se considera el caso de que un equipo se inscriba más de una vez.
Eliminar equipos del torneo. En este caso, se debe mostrar un submenú con la lista de equipos a remover del torneo.
Anotar gol(es) a un jugador. En este caso, se debe solicitar la cantidad de goles a anotar y que escoja a un jugador (mostrando la lista).
Conocer el número total de goles de los equipos. En este caso, se debe mostrar los goles totales de cada equipo.
Generar rol de juegos. Generar un rol de juegos con los equipos del torneo estilo "todos contra todos" organizado por jornadas.
Nota: Se considera que se tiene un único objeto de la clase Torneo.

El sistema debe ser escalable para manejar un gran número de jugadores, equipos y torneos.
El método generar_rol() debe funcionar eficientemente incluso con muchos equipos, no se debe 
diseñar para cierta cantidad de equipos específicamente.

"""
print(Fore.GREEN+ "████████╗ ██████╗ ██████╗ ███╗   ██╗███████╗ ██████╗     ██████╗ ███████╗   ")
print(Fore.RED+   "╚══██╔══╝██╔═══██╗██╔══██╗████╗  ██║██╔════╝██╔═══██╗    ██╔══██╗██╔════╝    ")
print(Fore.CYAN+  "   ██║   ██║   ██║██████╔╝██╔██╗ ██║█████╗  ██║   ██║    ██║  ██║█████╗      ")
print(Fore.YELLOW+"   ██║   ██║   ██║██╔══██╗██║╚██╗██║██╔══╝  ██║   ██║    ██║  ██║██╔══╝       ")
print(Fore.BLUE+  "   ██║   ╚██████╔╝██║  ██║██║ ╚████║███████╗╚██████╔╝    ██████╔╝███████╗    ")
print(Fore.GREEN+ "   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝     ╚═════╝ ╚══════╝    ")
print(Fore.RED+   " ███████╗██╗   ██╗████████╗██████╗  ██████╗ ██╗ ")
print(Fore.CYAN+  " ██╔════╝██║   ██║╚══██╔══╝██╔══██╗██╔═══██╗██║   ")
print(Fore.YELLOW+" █████╗  ██║   ██║   ██║   ██████╔╝██║   ██║██║ ")
print(Fore.BLUE+  " ██╔══╝  ██║   ██║   ██║   ██╔══██╗██║   ██║██║  ")
print(Fore.GREEN+ " ██║     ╚██████╔╝   ██║   ██████╔╝╚██████╔╝███████╗  ")
print(Fore.RED+   " ╚═╝      ╚═════╝    ╚═╝   ╚═════╝  ╚═════╝ ╚══════╝ ")
print(Fore.CYAN+  "   Por Durán Breceda Lourdes Jamileth. 403     ")

# inicializar listas globales
jugadores_disponibles = []
equipos_disponibles = []


def menu_principal() -> int:       # >>>>>>>>>>>>>>>>>>>>>>>>>>> Menú principal

    """
    Función que imprime menú principal
    :return: retorna un valor entero según haya elegido el usuario.
    """
    print("[1].- Crear nuevo jugador.")
    print("[2].- Crear nuevo equipo.")
    print("[3].- Ver lista de jugadores.")
    print("[4].- Ver lista de equipos.")
    print("[5].- Agregar jugadores a algún equipo.")
    print("[6].- Eliminar jugadores de un equipo.")
    print("[7].- Agregar equipos al torneo. ")
    print("[8].- Eliminar equipos del torneo. ")
    print("[9].- Anotar gol(es) a un jugador. ")
    print("[10].- Mostrar número total de goles de los equipos")
    print("[11].- Generar rol de juegos. ")
    print("[0].- Salir. ")

    opcion = input( "Selecciona una opción: ")
    while not opcion.isnumeric() or int(opcion) not in range(0, 12): #Sí no es numérica ni está en el rango del 0 al 12
        print( "Opción no válida, intenta de nuevo :(")
        opcion = input( "Selecciona una opción: ")

    return int(opcion)


def menu_equipos(lista_equipos: list[Equipo]):        # >>>>>>>>>>>>>>>>>>>>>>>>>>> Menú equipos
    """
    Fúnción que muestra los equipos
    :return: retorna un valor entero según haya elegido el usuario.
    """
    print("-----Equipos")
    for i, equipo_n in enumerate(lista_equipos, start=1):
        print( f"[{i}].- {equipo_n.nombre}")

    opcion = input("Selecciona una opción: ")
    while not opcion.isnumeric() or int(opcion) not in range(1, len(lista_equipos) + 1): #Mientras no sea numérica, que sea un entero ni esté en el rango de los equipos
        print("Opción no válida. Intenta de nuevo")
        opcion = input("Selecciona una opción: ")

    return int(opcion) - 1


def menu_jugadores(lista_jugadores: list[Jugador]):     # >>>>>>>>>>>>>>>>>>>>>>>>>>> Menú jugadores
    """
    :return: retorna un valor entero según haya elegido el usuario.
    """
    print("     Jugadores")
    for i, integrante in enumerate(lista_jugadores, start=1):
        print(f"[{i}].- {integrante.nombre}")

    opcion = input(Fore.WHITE + "Selecciona una opción: ")
    while not opcion.isnumeric() or int(opcion) not in range(1, len(lista_jugadores) + 1):
        print( "Opción no válida. Intenta de nuevo")
        opcion = input( "Selecciona una opción: ")

    return int(opcion) - 1


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Código a nivel de módulo.
if __name__ == '__main__':

    flag = 0

    #Crear jugadores
    torneo_predeterminado = Torneo("Torneo Juegos")

    while flag == 0:

        option = menu_principal()

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Crear nuevo jugador.
        if option == 1:
            nombre_jugador = input("Ingrese el nombre del nuevo jugador: ")
            numero_jugador = (input("Ingresa el número del nuevo jugador: "))
            while not numero_jugador.isnumeric(): #Sí goles es un número, si no, entonces es inválida
                print( "Opción no válida, Intenta de nuevo :(")
                numero_jugador = input( "Selecciona una opción: ")
            numero_jugador = int(numero_jugador)
            nuevo_jugador = Jugador(nombre_jugador,numero_jugador)

            jugadores_disponibles.append(nuevo_jugador)


        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  Crear nuevo equipo jugador.
        elif option == 2:
            nombre_equipo = input("Ingrese nombre del equipo a crear: ")
            nuevo_equipo = Equipo(nombre_equipo)
            equipos_disponibles.append(nuevo_equipo)

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Ver lista de jugadores.
        elif option == 3:
            if not torneo_predeterminado.equipos:
                print("No hay jugadores creados.")
            else:
                for equipo in torneo_predeterminado.equipos:
                    print( f"{equipo}")
                    equipo.mostrar_jugadores()

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Ver lista de equipos.
        elif option == 4:
            if not torneo_predeterminado.equipos:
                print("No hay equipos en el torneo.")
            else:
                torneo_predeterminado.mostrar_equipos()

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Agregar jugadores a un nuevo equipo.
        elif option == 5:
            salir = 1
            if not torneo_predeterminado.equipos:   # Verificar que existen equipos en el torneo.
                print("Aún no hay equipos en el torneo")
            else:
                jugadores_elejidos = []
                equipo = torneo_predeterminado.equipos[menu_equipos(torneo_predeterminado.equipos)]
                if not jugadores_disponibles:       # Verificar que existen jugadores disponibles.
                    print( "Aún no hay jugadores disponibles. :(")
                else:
                    while salir != 0 :       # Seleccionar jugadores a agregar
                        jugador = jugadores_disponibles[menu_jugadores(jugadores_disponibles)]
                        jugadores_elejidos.append(jugador)
                        print("Seleccionado correctamente.")

                        jugadores_disponibles.remove(jugador)  #Se agrega a jugadores elegidos para posteriormente remover

                        salir = input("Ingrese [1] para seguir o [0] para terminar: ")
                        while not salir.isdigit() or int(salir) not in [0, 1]: #Sí no es un dígito ni es O ni  1
                            print( "Opción no válida. Intenta de nuevo.  :/")
                            salir = input("Ingrese un [1] para seguir o [0] para terminar: ")
                        salir = int(salir)

                    if jugadores_elejidos:  #sí hay jugadores seleccionados, entonces agrega al equipo como argumento variable
                        equipo.agregar_jugadores(*jugadores_elejidos)
                    else:
                        print("No se agregó ningún jugador al equipo :(")

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Eliminar jugadores de un equipo.
        elif option == 6:
            salir = 1
            if not torneo_predeterminado.equipos:       # Verificar que existen equipos en el torneo.
                print( "Aún no hay equipos en el torneo :(")
            else:
                jugadores_eliminar = []
                equipo = torneo_predeterminado.equipos[menu_equipos(torneo_predeterminado.equipos)]
                if not equipo.jugadores_existentes:      # Verificar que existen jugadores dentro del equipo.
                    print( "Aún no hay jugadores en el equipo :(")
                else:
                    while salir != 0:
                        jugador = equipo.jugadores_existentes[menu_jugadores(equipo.jugadores_existentes)]
                        jugadores_eliminar.append(jugador)
                        print("Seleccionado correctamente.")

                        salir = input("Ingrese un 1 para seguir o 0 para terminar: ")
                        while not salir.isdigit() or int(salir) not in [0, 1]:
                            print("Opción no válida. Intenta de nuevo.")
                            salir = input( "Ingrese un [1] para seguir o [0] para terminar: ")
                        salir = int(salir)

                    if jugadores_eliminar:  # Si hay jugadores seleccionados, agregarlos al equipo
                        equipo.remover_jugadores(*jugadores_eliminar)
                    else:
                        print("No se eliminó ningún jugador del equipo ")
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Agregar equipos al torneo.
        elif option == 7:
            salir = 1
            if not equipos_disponibles:  # Verificar que existen equipos disponibles.
                print( "No hay equipos en el torneo.")
            else:
                equipos_elejidos = []

                while salir != 0:  # Seleccionar equipos a agregar
                    equipo = equipos_disponibles[menu_equipos(equipos_disponibles)]
                    equipos_elejidos.append(equipo)
                    print("Seleccionado correctamente.")

                    equipos_disponibles.remove(equipo)  # Eliminar el equipo elejido de los equipos disponibles despues de agregarlo a equipos elejidos.

                    salir = input("Ingrese [1] para seguir o [0] para terminar: ")
                    while not salir.isdigit() or int(salir) not in [0, 1]:
                        print( "Opción no válida. Intenta de nuevo.")
                        salir = input("Ingrese  [1] para seguir o [0]para terminar: ")
                    salir = int(salir)

                if equipos_elejidos:  # Si hay jugadores seleccionados, agregarlos al equipo
                    torneo_predeterminado.agregar_equipos(*equipos_elejidos)
                else:
                    print("No se agregó ningún jugador al equipo.  :/")

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Eliminar equipos del torneo
        elif option == 8:
            salir = 1
            if not torneo_predeterminado.equipos:#Verificar que haya equipos en torneo
                print( "Aún no hay equipos en el torneo.  :/")
            else:
                equipos_eliminar = []
                while salir != 0:
                    equipo = torneo_predeterminado.equipos[menu_equipos(torneo_predeterminado.equipos)]
                    equipos_eliminar.append(equipo)
                    print("Seleccionado correctamente.")

                    salir = input("Ingrese un [1 ]para seguir o [0] para terminar: ")#
                    while not salir.isdigit() or int(salir) not in [0, 1]: #si no es un dígito, o si salir no se puede convertir a un entero ni se encuentra entre el 0 ni es uno
                        print( "Opción no válida, intenta de nuevo :(")
                        salir = input("Ingrese un [1] para seguir o [0 ]para terminar: ")
                    salir = int(salir) #Convierte a entero

                if equipos_eliminar:  #si sí hay jugadores seleccionados, agregarlos al equipo
                    torneo_predeterminado.remover_equipos(*equipos_eliminar)
                else:
                    print( "No se eliminó ningún equipo del torneo :(")

        elif option == 9:# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Anotar goles a un jugador
            equipo = torneo_predeterminado.equipos[menu_equipos(torneo_predeterminado.equipos)]
            jugador = equipo.jugadores_existentes[menu_jugadores(equipo.jugadores_existentes)]

            goles = input(f"ingrese la cantidad de goles que se le anotaran al jugador {jugador.nombre}: ")
            while not goles.isnumeric(): #Sí goles es un número, si no, entonces es inválida
                print( "Opción no válida, intenta de nuevo :(")
                goles = input( "Selecciona una opción: ")
            goles = int(goles)
            jugador.anotar_goles(goles)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Conocer el número total de goles de los equipos
        elif option == 10:
            for equipo in torneo_predeterminado.equipos:
                total_goles = sum(jugador.goles for jugador in equipo.jugadores_existentes)
                print(f"El total de goles del equipo {equipo.nombre} es: {total_goles}")
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Generar rol de juegos
        elif option == 11:
            torneo_predeterminado.generar_rol()
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Salir
        elif option == 0:
            print("Saliendo del programa... ")
            flag = 1


            """
            equipos = [] #Se crea la lista de equipos
            numero_equipos = int(input("Ingrese número (PAR) de equipos que jugarán:  "))#Debe ser par porque los emparejamientos deben ser par
            for i in range(0,numero_equipos):
                equipo = input(f"Ingrese el nombre del equipo {i}: ") #Se lee por teclado el nombre del equipo
                equipos.append(equipo) #Se añade el equipo a la lista de equipos

            numero_partidos = int(input("Ingrese cantidad de veces que se jugará: "))
            rol = [] #Se crea la lista de rol
            pivote = equipos[0] #Se crea el pivote que es el primero
            ultimo_equipo = numero_equipos-1
            
           
            #Este for solo se encarga de hacer las asignaciones, posteriormente se hará el reordenamiento de la lista
            for partido in range(numero_partidos):
                print(f"** Ronda {partido} **")
                ultimo_equipo = numero_equipos-1
                for j in range(0, len(equipos)//2): #División entera, la palabra "len" accede al número de elementos que hay en la lista, se divide entre dos porque solo hará la mitad de los equipos para asignarlos con la otra mitad
                    if j == 0: #Cuando se esté en el caso 1, se asigna ese par. el primero con el último y se guarda como tupla en la lista de rol
                        rol.append((pivote, equipos[ultimo_equipo]))
                    else: #Para todos los demás casos solo se van guardando tal cual los pares en las tuplas
                        rol.append((equipos[j], equipos[ultimo_equipo - j])) 
            
            
                # Imprimir los vs en pantalla
                for versus in rol:
                    print(f"{versus[0]} vs {versus[1]}") #Imprime la lista
            #Lista[-1] refiere al último elemento de la lista
                equipos = [equipos[0]] +[equipos[-1]] + equipos[1:-1]   #el primero siempre se mantiene pues es el pivote, el siguiente es el último y el resto sigue igual
                rol = [] #Reincia la lista cada vez solo para imprimirlos
            """

        print()
        print( "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print()