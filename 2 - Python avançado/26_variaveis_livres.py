# variaveis livres
def fora(x):
    a = x

    def dentro():
        return a
    return dentro


dentro = fora(10)
dentro1 = fora(20)

print(dentro())
print(dentro1())
