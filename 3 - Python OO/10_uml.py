# associação
class Escritor:
    def __init__(self, nome, ferramenta):
        self.nome = nome
        self.ferramenta = ferramenta


class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} esta escrevendo.'


caneta = FerramentaDeEscrever('Caneta Bic')

print(caneta.nome)
print(caneta.escrever())

pedro = Escritor('Pedro', caneta)

print(pedro.nome)
print(pedro.ferramenta.nome)
