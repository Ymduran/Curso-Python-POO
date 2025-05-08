"""
fecha:040425
Usando n como parámetro en la función patrón, donde n > 0, complete el código para obtener el patrón:
1
1*2
1**3
1***4
... y así sucesivamente...
Nota: No hay salto de línea al final (después del final del patrón).
Ejemplos:
patrón(3) debe devolver "1\n1*2\n1**3", por ejemplo:
1
1*2
1**3
patrón(10): debe devolver lo siguiente:
1
1*2
1**3
1***4
1****5
1*****6
1******7
1*******8
1*********9
1*********10
"""
def pattern(n)->None:
    new_list = [] #Crear lista vacía para guardar las cadenas
    star = "*"
    for i in range(n+1):
        if i == 1 : print(i)
        else: print(f"1{star * (i-1)}{i}")






if __name__ == '__main__':
    print(pattern(1) )
    print(pattern(3))
    print(pattern(7))
    print(pattern(20))