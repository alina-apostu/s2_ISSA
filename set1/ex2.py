def f(s):
    nr=0
    for i in range(0,len(s)):
        if 'a' in s[i] or 'e' in s[i] or 'i' in s[i] or 'o' in s[i] or 'u' in s[i]:
            nr=nr+1;
    return nr

if __name__=="__main__":
    nr=f('alina')
    print(f'nr vocale={nr}')