print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 22 de junio del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Simular sistema de rangos tipo Codewars con progreso acumulable  * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

"""
Instrucciones:

Crear una clase `User` que simule un sistema de rangos del -8 al 8 (sin 0).
Se acumula progreso con actividades. Al llegar a 100 de progreso, el usuario
sube de rango y el progreso sobrante se mantiene.

Reglas:
- Rangos permitidos: -8 a 8, sin incluir 0.
- Actividad igual al rango → +3 puntos
- Actividad 1 nivel abajo → +1 punto
- Actividad 2 o más niveles abajo → 0 puntos
- Actividad superior → +10*d*d donde d = diferencia de niveles
"""





class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, activity_rank: int):
        """
        Aumenta el progreso del usuario al completar una actividad.
        :param activity_rank: Rango de la actividad (-8 a -1, 1 a 8)
        """
        if activity_rank not in self._valid_ranks(): raise ValueError("Rango de actividad inválido")

        if self.rank == 8: return  #Ya no se progresa más

        diff = self._rank_difference(activity_rank)

        if diff == 0: self.progress += 3
        elif diff == -1: self.progress += 1
        elif diff > 0 self.progress += 10 * diff * diff
        #Si diff <= -2: no se suma nada

        self._update_rank()




  

    def _update_rank(self):
        """
        Revisa si el progreso acumulado basta para subir de rango.
        Si es así, se actualiza el rango y se conserva el sobrante.
        """
        while self.progress >= 100 and self.rank < 8:
            self.progress -= 100
            self.rank = self._next_rank(self.rank)

        if self.rank == 8:  self.progress = 0

    def _rank_difference(self, activity_rank: int) -> int:
        """
        Calcula la diferencia entre rangos, considerando que no hay rango 0.
        """
        user_index = self._rank_to_index(self.rank)
        activity_index = self._rank_to_index(activity_rank)
        return activity_index - user_index

    def _rank_to_index(self, rank: int) -> int:
        """
        Convierte un rango real en un índice (posición) lineal.
        Ej: -8 → 0, -1 → 7, 1 → 8, 8 → 15
        """
        if rank > 0: return rank + 7  # saltamos el 0
        else:   return rank + 8

    def _next_rank(self, current: int) -> int:
        """
        Obtiene el siguiente rango válido.
        """
        orden = self._valid_ranks()
        idx = orden.index(current)
        if idx + 1 < len(orden): return orden[idx + 1]
        return current

    def _valid_ranks(self):
        """
        Lista de rangos válidos.
        """
        return [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]



if __name__ == '__main__':
    user = User()
    print(user.rank)     # -8
    print(user.progress) # 0

    user.inc_progress(-7)
    print(user.progress) # 10

    user.inc_progress(-5)
    print(user.rank)     # -7
    print(user.progress) # 0

    user.inc_progress(-8)  # sin efecto
    print(user.rank)       # -7
    print(user.progress)   # 0

    # Avance múltiple
    user.inc_progress(-4)  # 90 puntos
    print(user.rank)       # -6
    print(user.progress)   # 80

    # Llegar a rango positivo
    while user.rank < 1:
        user.inc_progress(1)
    print(user.rank)       # al menos 1
    print(user.progress)


  

    # Subir hasta rango máximo
    while user.rank < 8:
        user.inc_progress(8)
    print(user.rank)       # 8
    print(user.progress)   # 0




"""
El truco es convertir los rangos en índices lineales para ignorar el hueco en el 0.
Entonces se usa una lista de rangos válidos para evitar errores de rango.
El método _update_rank() maneja muchas subidas si el progreso es mayor a 100.
Cuando el usuario alcanza el rango 8, el progreso se bloquea en 0.
"""
