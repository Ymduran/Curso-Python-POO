"""
Hubo un examen en tu clase y lo aprobaste. ¡Felicidades!
Pero eres ambicioso. Quieres saber si eres mejor que el promedio de tu clase.
Recibirás una matriz con las puntuaciones de tus compañeros. ¡Ahora calcula el promedio y compáralo!
Devuelve "true" si eres mejor; de lo contrario, "false".
Nota:
Tus puntos no se incluyen en la matriz de puntos de tu clase. ¡No los olvides al calcular el promedio!
"""

def better_than_average(class_points:int, your_points:int) -> bool:
    """
    Esta función compara los promedios de las calificaciones de la clase con tus puntos, como se trata de un booleano
    retorna directamente una operación booleana.
    suma de tod0s los puntos de la clase/ cantidad de elementos(calificaciones) < tu promedio
    :param class_points: Una lista con todas las calificaciones del grupo, excepto la tuya
    :param your_points: Tu calificación
    :return: Un valor verdadero o falso si tu promedio es mayor que el del grupo
    """
    return sum(class_points)/len(class_points) < your_points

if __name__ == '__main__':
    print(better_than_average([2, 3], 5))
    print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75))
    print(better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69))
    print(better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50))