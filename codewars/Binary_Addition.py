
def add_binary(a: int,b:int) -> str:
    suma = a + b
    lista = []
    while True:
        if suma % 2 == 0:
            lista.append("0")
        elif suma % 2 != 0:
            lista.append("1")
        suma = suma // 2
        if suma == 0:
            #lista.append(1)
            break
    lista_auxiliar = []
    for i in range(len(lista)):
        lista_auxiliar.append(lista[-i])

    return lista_auxiliar





if __name__ == '__main__':
    print(add_binary(1, 1))
    print(add_binary(2, 2))
    print(add_binary(51, 12))