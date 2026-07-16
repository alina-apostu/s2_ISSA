def f(x=1, flag=True, *siruri):
    rez=[]
    for sir in siruri:
        l=[]
        for i in range(0, len(sir)):
            if flag==True:
                if ord(sir[i])%x==0:
                    l.append(sir[i])
            elif flag==False:
                if ord(sir[i])%x!=0:
                    l.append(sir[i])

        rez.append(l)
    return rez;

if __name__=='__main__':
    a='test'
    b='hello'
    c='lab002'
    siruri=[a,b,c]
    rez=f(2,False,*siruri)
    print(rez)