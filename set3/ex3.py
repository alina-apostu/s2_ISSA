def sunt_egale(v1, v2):
    if type(v1) is not type(v2):
        return False

    if isinstance(v1, (int, float, str, bool)) or v1 is None:
        return v1 == v2

    if isinstance(v1, dict):
        if len(v1) != len(v2):
            return False
        for k in v1:
            if k not in v2 or not sunt_egale(v1[k], v2[k]):
                return False
        return True

    if isinstance(v1, (list, tuple)):
        if len(v1) != len(v2):
            return False
        for i in range(len(v1)):
            if not sunt_egale(v1[i], v2[i]):
                return False
        return True

    if isinstance(v1, set):
        if len(v1) != len(v2):
            return False
        for elem1 in v1:
            gasit = False
            for elem2 in v2:
                if sunt_egale(elem1, elem2):
                    gasit = True
                    break
            if not gasit:
                return False
        return True

    return v1 == v2


def f(d1, d2):
    comune_diferite = []
    doar_in_d1 = []
    doar_in_d2 = []

    for k in d1:
        if k not in d2:
            doar_in_d1.append(k)
        elif not sunt_egale(d1[k], d2[k]):
            comune_diferite.append(k)

    for k in d2:
        if k not in d1:
            doar_in_d2.append(k)

    return comune_diferite, doar_in_d1, doar_in_d2


if __name__ == '__main__':
    dict_a = {
        "nume": "George",
        "varsta": 25,
        "adresa": {"oras": "Iasi", "strada": "Palat"},
        "note": [10, 9, 8],
        "hobbies": {"citit", "sport"},
        "doar_a": True
    }

    dict_b = {
        "nume": "George",
        "varsta": 26,
        "adresa": {"oras": "Iasi", "strada": "Unirii"},
        "note": [10, 9, 8],
        "hobbies": {"sport", "citit"},
        "doar_b": False
    }

    rez = f(dict_a, dict_b)
    print(rez)