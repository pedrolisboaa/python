""" 
def duplicar(numero):
    return numero * 2


def triplicar(numero):
    return numero * 3


def quadriplicar(numero):
    return numero * 4


def fazerTodos(numero):
    return duplicar(numero)
"""


def criar_multiplicador(multiplicador):
    def multiplica(numero):
        return multiplicador * numero
    return multiplica


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(10))
print(triplicar(100))
print(quadruplicar(100))
