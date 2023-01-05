pessoa = {
    'nome': 'Pedro',
    'sobrenome': 'Lisboa',
    'idade': 30,
    'endereco': [
        {'rua': 1, 'casa': 10},
        {'rua': 1, 'casa': 11},
    ]
}


print(pessoa['nome'])
print(pessoa['idade'])

print(pessoa.get('nome'))
print(pessoa.get('nome2'))
