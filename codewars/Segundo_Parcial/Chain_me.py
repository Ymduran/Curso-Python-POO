def chain(init_val, functions):
    """
    Aplica una lista de funciones en orden a un valor inicial.
    :param: init_val : cualquier tipo (usualmente numérico) - valor inicial sobre el que se aplican las funciones.
    :param: functions : lista de funciones - cada función toma un argumento y devuelve un valor.
    :return
    El valor resultante después de aplicar todas las funciones en secuencia.
    """
    resultado = init_val  # Comenzamos con el valor inicial

    indice = 0
    while indice < len(functions):
        funcion_actual = functions[indice]
        resultado = funcion_actual(resultado)  # Se aplica la función
        indice = indice + 1  # Avanza al siguiente índice

    return resultado


# Ejemplo de funciones para probar:
def add10(x):
    return x + 10

def mul30(x):
    return x * 30

# Prueba de la función chain
print(chain(50, [add10, mul30]))  # Resultado esperado: 1800

