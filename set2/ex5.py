def f(x, k):
    rez=[]
    stiva=[]

    def back(index_start):
        if len(stiva)==k:
            rez.append(tuple(stiva))
            return
        for i in range(index_start, len(x)):
            stiva.append(x[i])
            back(i + 1)
            stiva.pop()

    back(0)
    return rez

x = [6, 7, 8, 9]
k = 3
print(f(x, k))