"""
Dados dos números enteros a y b, que pueden ser positivos o negativos,
calcula la suma de todos los números enteros entre ellos (incluyéndolos) y devuélvela.
Si los dos números son iguales, devuelve a o b.
Nota: ¡a y b no están ordenados!
"""
def get_sum(a: int,b:int )-> int:

    mayor, menor = max(a,b), min(a,b)
    if a != b:
        return (mayor * (mayor +1)//2) - ((menor -1) * menor //2) #Fórmulla de la suma de una serie aritmética
    else:
        return a



if __name__ == '__main__':
    print(get_sum(0,1))
    print(get_sum(1, 1))
    print(get_sum(-30, -30))
    print(get_sum(-434, 1172))
    print(get_sum(-4977,-2640))



