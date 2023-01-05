lista = [1, 4, 2, 6, 87, 5, 234, 68, 234, -10, 0]
lista.sort()
print(lista)

lista_de_nomes = [
    {'nome': 'Pedro', 'sobrenome': 'Lisboa'},
    {'nome': 'Juliana', 'sobrenome': 'Oliveira'},
    {'nome': 'Olivia', 'sobrenome': 'Oliveira Lisboa'},
]


lista_de_nomes.sort(lambda item: item['nome'])
for item in lista:
    print(item)
