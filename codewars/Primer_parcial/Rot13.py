def rot13(message):
    diccionario_conversion_Caesar_cipher = {
        'a': 'n',
        'A': 'N',

        'b': 'o',
        'B': 'O',

        'c': 'p',
        'C': 'P',

        'd': 'q',
        'D': 'Q',

        'e': 'r',
        'E': 'R',

        'f': 's',
        'F': 'S',

        'g': 't',
        'G': 'T',

        'h': 'u',
        'H': 'U',

        'i': 'v',
        'I': 'V',

        'j': 'w',
        'J': 'W',

        'k': 'x',
        'K': 'X',

        'l': 'y',
        'L': 'Y',

        'm': 'z',
        'M': 'Z',

        'n': 'a',
        'N': 'A',

        'o': 'b',
        'O': 'B',

        'p': 'c',
        'P': 'C',

        'q': 'd',
        'Q': 'D',

        'r': 'e',
        'R': 'E',

        's': 'f',
        'S': 'F',

        't': 'g',
        'T': 'G',

        'u': 'h',
        'U': 'H',

        'v': 'i',
        'V': 'I',

        'w': 'j',
        'W': 'J',

        'x': 'k',
        'X': 'K',

        'y': 'l',
        'Y': 'L',

        'z': 'm',
        'Z': 'M'

    }

    texto_convertido = ""  # Texto_convertido inica como cadena vacía
    for caracter in message:
        if caracter in diccionario_conversion_Caesar_cipher:
            # Reemplaza el carácter si está en el diccionario, si no, queda igual
            texto_convertido += diccionario_conversion_Caesar_cipher.get(caracter, caracter)
        else:
            texto_convertido += caracter
    return texto_convertido

if __name__ == '__main__':
    print( rot13('test'))
    print(rot13('Test'))
    print(rot13('aA bB zZ 1234 *!?%'))

