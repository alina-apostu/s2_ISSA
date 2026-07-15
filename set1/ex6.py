def f(s):
    rez=""
    for i in s:
        if i.isupper():
            rez=rez+'_'+i.lower()
        else:
            rez=rez+i
    return rez.lstrip('_')



if __name__=='__main__':
    print(f("ExempluCodPython"))