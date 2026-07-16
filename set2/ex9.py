def f(lista):
    return sorted(lista, key=lambda t: t[1][2])

if __name__=='__main__':
    list=[('abc', 'bcd'), ('abc', 'zza')]
    rez=f(list)

    print(rez)