def f(char_len, *cuv):
    if len(cuv) < 2:
        return True
    for i in range(len(cuv) - 1):
        cuv_curent = cuv[i]
        cuv_urm = cuv[i + 1]

        end = cuv_curent[-char_len:]
        if not cuv_urm.startswith(end):
            return False

    return True



if __name__=='__main__':
    print(f(2, "abecedar", "arici", "ciocan"))
    print(f(2, "abecedar", "arici", "mere"))
