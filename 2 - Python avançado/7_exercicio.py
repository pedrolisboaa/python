def multiplica(*arg):
    multiplicador = 1

    for numero in arg:
        multiplicador *= numero

    return multiplicador


def parOuImpar(numero):
    par_ou_impar = numero % 2 == 0
    if par_ou_impar:
        return 'PAR'
    return 'IMPAR'


print(multiplica(1, 2, 3, 4, 5))
print(parOuImpar(5))
print(parOuImpar(6))
