def cmmdc(a,b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a


def f(*nr):
    if not nr:
        return None
    r=nr[0]
    for i in nr[1:]:
        r=cmmdc(r,i)
    return r

if __name__=="__main__":
    lista=[6,18,24]
    rez=f(*lista)
    print(rez)