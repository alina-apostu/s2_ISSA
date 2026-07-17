def f(tag, content, **kwargs):
    atribute = []

    for cheie, valoare in kwargs.items():
        if cheie.startswith('_'):
            nume_atribut = cheie[1:]
        elif cheie == 'class_':
            nume_atribut = 'class'
        else:
            nume_atribut = cheie
        atribute.append(f'{nume_atribut}="{valoare}"')

    sir_atribute = " " + " ".join(atribute) if atribute else ""
    return f"<{tag}{sir_atribute}>{content}</{tag}>"


if __name__ == '__main__':
    rezultat = f(
        "a",
        "Hello there",
        href="http://python.org",
        _class="my-link",
        id="someid"
    )
    print(rezultat)