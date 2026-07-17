dict={
    "print_all": lambda *a, **k: print(a, k),
    "print_args_commas": lambda *a, **k: print(a, k, sep=", "),
    "print_only_args": lambda *a, **k: print(a),
    "print_only_kwargs": lambda *a, **k: print(k)
}


def f(nume_fct, *args, **kwargs):
    if nume_fct in dict:
        return dict[nume_fct](*args, **kwargs)
    else:
        return None


if __name__ == '__main__':
    f("print_all", 1, 2, 3, x=10, y=20)
    f("print_only_args", "test", "demo")
    f("print_only_kwargs", a=1, b=2)

    dict["media_aritmetica"] = lambda *a, **k: sum(a) / len(a) if a else 0

    rezultat=f("media_aritmetica", 10, 20)
    print(f"Media este: {rezultat}")