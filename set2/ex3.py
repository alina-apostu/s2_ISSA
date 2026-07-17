

def cmmdc(a,b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a

def f(puncte):
    drepte_unice = set()
    n=len(puncte)

    for i in range(n):
        for j in range(i + 1, n):
            x1,y1=puncte[i]
            x2,y2=puncte[j]
            if x1==x2 and y1==y2:
                continue
            a=y1-y2
            b=x2-x1
            c=x1*y2 -x2*y1

            cmmdc_rez=cmmdc(c,cmmdc(a,b))
            if cmmdc_rez!=0:
                a//=cmmdc_rez
                b//=cmmdc_rez
                c//=cmmdc_rez

            if a<0 or(a==0 and b<0) or (a==0 and b==0 and c< 0):
                a,b,c=-a,-b,-c
            drepte_unice.add((a,b,c))
    return list(drepte_unice)


if __name__ == '__main__':
    lista_puncte=[(0, 0), (2, 2), (3, 3), (0, 2), (2, 0)]
    rezultat=f(lista_puncte)
    print(rezultat)