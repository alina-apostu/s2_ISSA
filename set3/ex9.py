def f(*seturi):
    rez={}
    n = len(seturi)
    for i in range(n):
        for j in range(i + 1, n):
            set_a=seturi[i]
            set_b=seturi[j]
            reun=set_a|set_b
            inters=set_a&set_b
            dif_ab=set_a-set_b
            dif_ba=set_b-set_a

            str_a = str(set_a)
            str_b = str(set_b)
            rez[f"{str_a} | {str_b}"]=len(reun)
            rez[f"{str_a} & {str_b}"]=len(inters)
            rez[f"{str_a} - {str_b}"]=len(dif_ab)
            rez[f"{str_b} - {str_a}"]=len(dif_ba)
    return rez


if __name__ == '__main__':
    s1 = {1, 2}
    s2 = {2, 3}
    dict=f(s1, s2)
    for cheie, val in dict.items():
        print(f"'{cheie}': {val}")