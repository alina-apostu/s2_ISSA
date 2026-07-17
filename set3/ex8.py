def f(s):
    elem_unice=len(s)
    duplicate=0
    return (elem_unice, duplicate)


if __name__ == '__main__':
    multime = {1, 2, 2, 3, 4, 4, 4}
    print("set:", multime)
    rez = f(multime)
    print(rez)