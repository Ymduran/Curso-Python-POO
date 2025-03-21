
def add_binary(a: int,b:int) -> str:
    suma = a + b
    lista = []
    while suma > 0:
        if suma % 2 == 0:
            lista.append("0")
        else:
            lista.append("1")
        suma = suma // 2

    return ''.join(lista[::-1])





if __name__ == '__main__':
    print(add_binary(1, 1))
    print(add_binary(2, 2))
    print(add_binary(51, 12))