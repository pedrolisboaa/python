def somar(*args):
    soma = 0
    for numero in args:
        soma += numero
    print(soma)


def somar2(*args):
    teste = list(args)
    return sum(teste)


somar(1, 2, 3, 4, 5)
print(somar2(1, 2, 3, 4, 5, 6))
