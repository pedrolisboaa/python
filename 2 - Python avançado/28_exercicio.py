from itertools import zip_longest

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
siglas = ['BA', 'SP', 'MG', 'RJ']


def unir_listas(lista1, lista2):
    return list(zip(lista1, lista2))


print(unir_listas(cidades, siglas))
print(list(zip_longest(cidades, siglas)))


lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [2, 4, 5, 6, 8, 10, 12]
lista3 = [sum(x) for x in list(zip(lista1, lista2))]

print(lista3)
