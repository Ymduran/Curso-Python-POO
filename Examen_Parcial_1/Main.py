
from colorama import Fore
from colorama import Fore
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
jugadores = []
equipos = []
torneo = []


def menu_principal() -> None:

    """
    Función que imprime menú principal
    :return:
    """
    print("\n" * 5)
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



def ver_jugadores()-> None:
    """
    Esta función es para ver a todos los jugadores iterando en jugadores.
    :return:
    """
    if jugadores:
        print("Lista de jugadores:")
        for i, jugador in enumerate(jugadores):
            print(f"[{i}] - {jugador.nombre} (Número: {jugador.numero})")
    else:
        print("Aún no hay jugadores registrados:(")

def ver_equipos(*equipos:Equipo) -> None:
    """
    Función que imprime los equipos iterando en todos los equipo.
    :return:
    """
    count = 1
    if equipos:
        print("Lista de equipos:")
        for equi in equipos:
            print(f"[{count}].-{equi.nombre}")
            count +=1
    else:
        print("Aún no hay jugadores resgistrados :(.")




if __name__ == '__main__':

    flag = 0

    #Crear jugadores

    torneo_predeterminado = Torneo("Torneo predeterminado")


    juagador_predeterminado_01 = Jugador("Romero", 1)
    jugadores.append(juagador_predeterminado_01)

    juagador_predeterminado_02 = Jugador("Guadalupe", 2)
    jugadores.append(juagador_predeterminado_02)

    juagador_predeterminado_03 = Jugador("Sof", 3)
    jugadores.append(juagador_predeterminado_03)

    juagador_predeterminado_04 = Jugador("Pato", 4)
    jugadores.append(juagador_predeterminado_04)


    while flag == 0:
        menu_principal()
        option = int(input("Por favor, ingresa una de las opciones anteriores: "))
        if option == 1: #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Crear nuevo jugador
            nombre_jugador = input("Ingrese el nombre del nuevo jugador: ")
            numero_jugador = int(input("Ingresa el número del nuevo jugador: "))
            nuevo_jugador = Jugador(nombre_jugador,numero_jugador)
            jugadores.append(nuevo_jugador)


        elif option == 2: #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  Crear nuevo equipo jugador
            nombre_equipo = input("Ingrese nombre del equipo a crear: ")
            nuevo_equipo = Equipo(nombre_equipo)
            equipos.append(nuevo_equipo)
        elif option == 3: #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Ver lista de jugadores
            ver_jugadores()


        elif option == 4: #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Ver lista de equipos
            ver_equipos()


        elif option == 5: #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Agregar jugadores a un nuevo equipo
            ver_equipos(torneo_predeterminado._equipos)
            indice_equipo = int(input("Seleccione el índice del equipo: "))
            salir = input("Presiona enter para continuar o S para salir")

            while salir not in ("S","s"):
                ver_jugadores()
                indice_jugador = int(input("Selecciona índice del juagador: "))
                salir = input("Presiona enter para continuar o S para salir")
                equipo = equipos[indice_equipo]
                jugador = jugadores[indice_jugador]
                equipo.agregar_jugadores(jugador)






        elif option == 6: #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Eliminar jugadores de un equipo
            ver_equipos()
            indice_equipo = int(input("Seleccione el equipo: "))
            equipo = equipos[indice_equipo]
            equipo.mostrar_jugadores()
            indice_jugador = int(input("Seleccione el jugador a eliminar: "))
            equipo.remover_jugadores(equipo._jugadores[indice_jugador])



        elif option == 7: #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Agregar equipos al torneo
            lista_equipos_agregar = []
            ver_equipos()
            indice_equipo = None
            while indice_equipo not in ("S" , "s"):
                indice_equipo = int(input("Seleccione el índice del equipo a agregar al torneo o 'S' para salir " ))
                lista_equipos_agregar.append(equipos[indice_equipo])
            torneo_predeterminado.agregar_equipos(*lista_equipos_agregar)



        elif option == 8: #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Eliminar equipos del torneo
            print(f"Equipos en el torneo: {torneo._equipos}")
            indice_equipo = int(input("Seleccione el equipo a eliminar del torneo: "))
            torneo.remover_equipos(torneo._equipos[indice_equipo])



        elif option == 9: #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Anotar goles a un jugador
            ver_jugadores()
            indice_jugador = int(input("Seleccione el jugador al que se le anotarán goles: "))
            goles_anotar = int(input("Número de goles a anotar: "))
            jugadores[indice_jugador].anotar_goles(goles_anotar)


        elif option == 10: #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Conocer el número total de goles de los equipos
            for equipo in equipos:
                print(f"Equipo: {equipo.nombre} - Goles totales: {equipo.total_goles()}")


        elif option == 11:  #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Generar rol de juegos
            torneo.generar_rol()


        elif option == 0:  #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Salir
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














