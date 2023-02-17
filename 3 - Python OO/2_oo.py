class Comer:
    def __init__(self, nome):
        self.nome = nome

    def falar_nome(self):
        print(f'Oi meu nome é {self.nome}.')

    def comendo(self, comida):
        print(f'{self.nome} está comendo {comida}.')


pedro = Comer('Pedro')
pedro.comendo('macarrão')
pedro.falar_nome()
