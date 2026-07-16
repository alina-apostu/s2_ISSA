
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

def max_prim(s: str) -> int:
    numere=[]
    curent=''
    for c in s:
        if c.isdigit():
            curent += c
        else:
            if curent:
                numere.append(int(curent))
                curent=''
    if curent:
        numere.append(int(curent))


    prime = [x for x in numere if fun4(x)]
    if prime:
        return max(prime)
    return -1


if __name__=='__main__':
    text='ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda'
    rez=max_prim(text)
    print(rez)