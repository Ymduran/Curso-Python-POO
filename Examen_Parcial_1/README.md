Ejercicio: 
Descripción.

Se desea desarrollar un sistema en Python para gestionar un torneo de fútbol en el que participan varios equipos, y cada equipo está compuesto por jugadores. El sistema debe considerar lo siguiente:

1. Gestionar Jugadores:

        Cada jugador tiene un nombre, un número y una cantidad de goles anotados.
        Los jugadores pueden anotar goles, y el sistema debe actualizar su contador de goles.
        Los atributos de los jugadores deben estar protegidos, y se debe controlar el acceso a ellos mediante métodos de acceso.

2. Gestionar Equipos:

        Cada equipo tiene un nombre, un ID único (generado automáticamente) y una lista de jugadores.
        Los equipos pueden agregar o remover jugadores, ya sea individualmente o en grupos.
        Los atributos de los equipos deben estar protegidos, y se debe controlar el acceso a ellos mediante métodos de acceso.
        Cada equipo debe poder calcular el total de goles anotados por todos sus jugadores.

3. Gestionar Torneos:

        Cada torneo tiene un nombre y una lista de equipos participantes.
        Los torneos pueden agregar o remover equipos, ya sea individualmente o en grupos.
        El sistema debe permitir mostrar la lista de equipos participantes en el torneo.
        El sistema debe generar un rol de partidos estilo "todos contra todos", organizado por jornadas de todos los equipos participantes, donde cada jornada contenga un conjunto de partidos que no se solapen (es decir, ningún equipo juegue más de un partido por jornada).

4. Relaciones entre Clases:

        Un Equipo está compuesto por varios Jugadores (relación de agregación).
        Un Torneo está compuesto por varios Equipos (relación de agregación).




En este directorio, se van a almacenar los módulos de Python que resuelven el ejercicio:

Equipo.py

Jugador.py

Torneo.py

Main.py