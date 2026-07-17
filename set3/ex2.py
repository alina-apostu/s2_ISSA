def f(s):
    dict={}
    for carac in s:
        if carac in dict:
            dict[carac]+=1
        else:
            dict[carac]=1

    return dict


if __name__=='__main__':
   frecv=f("Ana are mere.")
   print(frecv)
