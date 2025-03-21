"""
Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case insensitive.
The string can contain any char.
"""
def xo(s) -> bool:
    countx, counts  = 0, 0
    for leter in s:
        if leter.lower() == "x": countx += 1
        if leter.lower() == "o": counts += 1
    return (countx == counts)

if __name__ == '__main__':
    print(xo("xxoo"))
    print(xo("xOxXo"))

