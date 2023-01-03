def soma(a, b, c=None):
    if c is not None:
        print(f'{a=} {b=} {c=} ', a + b + c)
    else:
        print(f'{a=} {b=} ', a + b)


soma(1, 2, 3)
soma(5, 9)
soma(6, 7, 0)
