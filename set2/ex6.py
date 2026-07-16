def f(x, *liste):
    total=[]
    rez=[]
    for l in liste:
        for i in l:
            if i not in total:
                total.append(i)
    for i in total:
        count=0
        for l in liste:
            if i in l:
                count=count+1;
        if count==x:
            rez.append(i);
    return rez

if __name__=='__main__':
    a=[1,2,3]
    b=[2,3,4,5]
    c=[2,4,6]
    d=[4,9,8]
    liste=[a,b,c,d]
    rez=f(3,*liste)
    print(rez)