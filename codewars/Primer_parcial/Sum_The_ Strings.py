"""
Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):

Example: (Input1, Input2 -->Output)
"""
def sum_str(a, b):
        if a == "":
            a = 0
        if b == "":
            b = 0
        return f"{int(a)+int(b)}"


if __name__ == '__main__':
    print(sum_str("4", "5"))
    print(sum_str("9", ""))