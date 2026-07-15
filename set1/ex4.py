def f(a,b):
    l1=len(a)
    l2=len(b)
    nr=0
    for i in range(0,l2-l1+1):
        cuv=b[i:i+l1]
        if cuv== a:
            nr=nr+1;

    return nr

if __name__=='__main__':
    nr=f('ana', 'bananan')
    print(nr)