def eval_pol(s:str, x:float) -> float:
    ec=s.replace("^", "**").replace("x", "*x").replace(" ", "")

    if ec.startswith("*"):
        ec=ec[1:]

    ec=ec.replace("+*", "+").replace("-*", "-")
    return float(eval(ec))


if __name__ == "__main__":
    p = "3x^3 + 5x^2 - 2x - 5"
    val = 2
    rez = eval_pol(p, val)
    print(f"rez: {rez}")