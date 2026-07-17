def f(a,b):
    inter=[]
    for x in a:
        if x in b and x not in inter:
            inter.append(x);
    reun=[]
    for x in a:
        if x not in reun:
            reun.append(x)
    for y in b:
        if y not in reun:
            reun.append(y)
    dif1=[]
    dif2=[]
    for x in a:
        if x not in inter:
            dif1.append(x)
    for x in b:
        if x not in inter:
            dif2.append(x)

    return set(inter),set(reun),set(dif1),set(dif2)

if __name__=='__main__':
    a=[1,2,3,4,5]
    b=[1,2,7,8]
    i,r,d1,d2=f(a,b)
    print(i,r,d1,d2)