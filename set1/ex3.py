def f(s):
    semne=[',', ';', '?', '!','.']
    for i in semne:
        s=s.replace(i, " ")
    cuv=s.split()
    return len(cuv)

if __name__=="__main__":
    nr=f('ceva?de;test!!     ')
    print(nr)