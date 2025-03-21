"""
Hubo un examen en tu clase y lo aprobaste. ¡Felicidades!
Pero eres ambicioso. Quieres saber si eres mejor que el promedio de tu clase.
Recibirás una matriz con las puntuaciones de tus compañeros. ¡Ahora calcula el promedio y compáralo!
Devuelve "true" si eres mejor; de lo contrario, "false".
Nota:
Tus puntos no se incluyen en la matriz de puntos de tu clase. ¡No los olvides al calcular el promedio!
"""

def better_than_average(class_points, your_points):
    return sum(class_points)/len(class_points) < your_points

if __name__ == '__main__':
    print(better_than_average([2, 3], 5))
    print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75))
    print(better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69))
    print(better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50))