dict={
    "+": lambda a, b: a + b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "%": lambda a, b: a % b
}

def f(operator, a, b):
    if operator in dict:
        return dict[operator](a, b)
    else:
        return None


if __name__ == '__main__':
    print(f("+", 5, 3))
    print(f("*", 4, 3))

    dict["-"] = lambda a, b: a - b
    print(f("-", 10, 4))
