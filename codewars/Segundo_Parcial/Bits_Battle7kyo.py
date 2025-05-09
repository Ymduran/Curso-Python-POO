def bits_battle(numbers):
    """
    Compara la cantidad de bits '1' de los números impares contra los bits '0' de los números pares.
    Los números impares luchan con sus bits '1' en binario.
    Los números pares luchan con sus bits '0' en binario.
    El número 0 es neutral y no participa.
    Param: numbers: lista de enteros positivos.
    :return: Una cadena: 'odds win', 'evens win' o 'tie'.
    """
    
    total_unos_impares = 0
    total_ceros_pares = 0

    i = 0
    while i < len(numbers):
        numero = numbers[i]

        if numero == 0:
            i = i + 1
            continue

        binario = bin(numero)[2:]  # Convertir a binario y quitamos el prefijo '0b'

        if numero % 2 == 0:
            j = 0
            while j < len(binario):
                if binario[j] == '0':
                    total_ceros_pares = total_ceros_pares + 1
                j = j + 1
        else:
            j = 0
            while j < len(binario):
                if binario[j] == '1':
                    total_unos_impares = total_unos_impares + 1
                j = j + 1

        i = i + 1

    if total_unos_impares > total_ceros_pares:
        return "odds win"
    elif total_unos_impares < total_ceros_pares:
        return "evens win"
    else:
        return "tie"
