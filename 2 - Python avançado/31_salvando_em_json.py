import json

"""
pessoa = {
    'nome': 'Pedro',
    'Sobrenome': 'Lisboa',
    'enderecos': [
        {'rua': 'r1', 'numero': 3},
        {'rua': 'r1', 'numero': 2},
    ],
    'altura': 1.9,
    'numeros_da_sorte': (1, 2, 3, 5, 6, 9),
    'dev': True,
    'nada': None
}

with open('aula_json', 'w', encoding='utf-8') as arquivo:
    json.dump(pessoa, arquivo, indent=2)
"""

with open('aula_json', 'r') as arquivo:
    pessoa = json.load(arquivo)

    print(pessoa)
    print(pessoa['nome'])
