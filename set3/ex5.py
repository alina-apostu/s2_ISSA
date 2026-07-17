def validate_dict(reguli, dictionar):
    chei_reguli = {regula[0] for regula in reguli}

    for cheie in dictionar:
        if cheie not in chei_reguli:
            return False

    for cheie, prefix, middle, sufix in reguli:
        if cheie not in dictionar:
            continue

        valoare = dictionar[cheie]
        if not valoare.startswith(prefix):
            return False
        if not valoare.endswith(sufix):
            return False
        if middle:
            pozitie = valoare.find(middle)
            if pozitie <= 0 or pozitie + len(middle) >= len(valoare):
                return False
    return True


if __name__ == '__main__':
    reguli = {("key1", "", "inside", ""),("key2", "start", "middle", "winter")}

    dictionar_invalid = {
        "key2": "starting the engine in the middle of the winter",
        "key1": "come inside, it's too cold outside",
        "key3": "this is not valid"
    }

    dictionar_valid = {
        "key2": "starting the engine in the middle of the winter",
        "key1": "come inside, it's too cold outside"
    }

    print(validate_dict(reguli, dictionar_invalid))
    print(validate_dict(reguli, dictionar_valid))