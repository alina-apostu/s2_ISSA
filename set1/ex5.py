def f(b):
    caract= ['\r', '\t', '\n', '\a', '\b', '\f', '\v']

    for c in caract:
        if c in b:
            return True

    return False

if __name__=='__main__':
    nr=f( 'bananan\r')
    print(nr)