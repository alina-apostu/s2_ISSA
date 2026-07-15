#5
# val=2**1024
# nr=len(str(val))
# print('numarul de cifre=', nr)
import math


#6
def fun1(a,b,c):
    rez=b
    if a>b:
        rez=a
    if c>rez:
        rez=c
    return rez



#7
def fun2(x,y,op):
    if '+' in op:
        rez=x+y
    elif '-' in op:
        rez=x-y
    elif '/' in op:
        rez=x/y
    elif '*' in op:
        rez=x*y
    return rez

#8
def fun3(x):
    orig=x
    x2=0
    while(x>0):
        r=x%10
        x2=x2*10+r
        x=x//10
    if x2==orig:
        return True
    elif x2!=x:
        return False

#9
def fun4(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    limita = math.isqrt(n) + 1

    for i in range(3, limita, 2):
        if n % i == 0:
            return False

    return True

#10
def fun5(list):
    for i in list:
        print(i)

#11
def fun6(list):
    minn=min(list)
    maxx=max(list)
    mean=(minn+maxx)/2
    gmean=math.sqrt(minn*maxx)
    return mean, gmean

#12
def fun7(list):
    m = len(list) // 2
    stanga = list[:m]
    dreapta = list[m:]

    return max(stanga), min(dreapta)

#13
def fun8(list):
    list2=[]

    for i in list:
        este_palindrom = fun3(i)
        are_cifre_pare = len(str(i)) % 2 == 0

        if este_palindrom and are_cifre_pare:
            list2.append(i)
    return list2

#14

def fun9(lst):
    val_min = min(lst)
    val_max = max(lst)

    idx_min = lst.index(val_min)
    idx_max = lst.index(val_max)

    start = min(idx_min, idx_max)
    stop = max(idx_min, idx_max)
    return lst[start: stop + 1]

#15
def fun10(mat):
    diag = []
    n = len(mat)
    for i in range(n):
        diag.append(mat[i][i])

    diag.sort(reverse=True)
    return diag

if __name__=="__main__":
    #6
    rez1=fun1(3,7,5)
    print(f'rez1={rez1}')

    rez2 = fun2(3, 7, '-')
    print(f'rez2={rez2}')

    rez3= fun3(322)
    print(f'rez3={rez3}')

    rez4 = fun4(23)
    print(f'rez4={rez4}')

    fun5([1,2,3,4])

    mean,gmean=fun6([7,4,3,1])
    print(f'mean={mean}, gmean={gmean}')

    m1, m2 = fun7([7, 4, 3, 1])
    print(f'm1={m1}, m2={m2}')

    lista_numere = [11, 121, 22, 1221, 43, 88]
    rez_test = fun8(lista_numere)
    print(f"lista nr palindorm cu nr par cifre: {rez_test}")

    lista_test = [3, 9, 4, 7, 2, 1, 8]
    print("sublista:", fun9(lista_test))

    mat_test = [
        [5, 1, 3],
        [2, 9, 4],
        [8, 6, 2]
    ]
    print("diag descresc:", fun10(mat_test))