def f(n):
    if n<=0:
        return []
    if n==1:
        return [1]

    lista = [1, 1]
    for i in range(2, n):
        urm= lista[-1] + lista[-2]
        lista.append(urm)

    return lista

if __name__=='__main__':
    list=f(5)
    print(list)