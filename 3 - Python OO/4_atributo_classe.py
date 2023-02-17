from datetime import datetime


class Pessoa:
    ANO_ATUAL = datetime.now().year

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def buscar_ano_nascimento(self):
        return self.ANO_ATUAL - self.idade


teste = {'nome': 'Juliana', 'idade': 26}

p1 = Pessoa('Pedro', 30)
p2 = Pessoa('Olívia', 2)
p3 = Pessoa(**teste)


print(p1.buscar_ano_nascimento())
print(p2.buscar_ano_nascimento())
print(p3.buscar_ano_nascimento())

print(p1.__dict__)
print(vars(p1))
print(vars(p3))

print(p3.nome)
