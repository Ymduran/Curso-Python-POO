


def calculator(x:int, y:int , op: str) -> int or str:
    """

    :param x:
    :param y:
    :param op:
    :return:
    """
    if (op in ('+','-','*','/')):
        if op == '+':
            result = x + y
        elif op == '-':
            result = x - y
        elif op == '*':
            result = x * y
        elif op == '/':
            result = x / y
    else:
        result = "Número inválido :("

    return result

if __name__ == '__main__':
    print(calculator(1,8,'/'))

