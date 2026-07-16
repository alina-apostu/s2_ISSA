import math


#functie pt nr prime
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

def f(list):
    list2=[]
    for x in list:
        if fun4(x) and x not in list2:
            list2.append(x)
    return list2

if __name__=='__main__':
    l1=[2,3,22,24,7,88,76, 7]
    l2=f(l1)
    print(l2)

