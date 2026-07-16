def f(*liste):
    lung_max=0
    list_max=0
    rez=[]
    for l in liste:
        if len(l)>lung_max:
            lung_max=len(l)
            list_max=l
    for i in range(0,lung_max):
        list_temp=[]
        for l in liste:
            if i<=len(l)-1:
                list_temp.append(l[i])
            else:
                list_temp.append(None)

        rez.append(list_temp)
    return rez

if __name__=='__main__':
    a=[1,2,3]
    b=[5,6,7]
    c=["a", "b", "c", 'd']
    liste=[a,b,c]
    rez=f(*liste)
    print(rez)
