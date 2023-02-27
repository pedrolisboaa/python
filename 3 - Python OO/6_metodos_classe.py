# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def metodo_de_classe(self):
        print(
            f'Oi meu nome {self.nome.capitalize()} eu tenho {self.idade} anos!')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)


p1 = Pessoa('pedro', 30)
p2 = Pessoa.criar_com_50_anos('Rosangela')
p3 = Pessoa.criar_com_50_anos('Marcelo')
p1.metodo_de_classe()
p2.metodo_de_classe()
p3.metodo_de_classe()
