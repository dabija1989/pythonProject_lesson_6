integer = int(input("Introduceti un numar pozitiv:\n"))
este_prim = 0
if integer > 1:
    este_prim = 1
    divisor = 2
    while divisor * divisor <= integer and este_prim:
        if integer % divisor == 0:
            este_prim = 0
        divisor += 1
if este_prim:
    print(f"{integer} este un numar prim.")
else:
    print(f"{integer} nu este un numar prim.")
