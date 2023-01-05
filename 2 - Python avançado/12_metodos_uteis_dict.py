dicionario = {
    'nome': 'Pedro',
    'sobrenome': 'Lisboa'
}


print(len(dicionario))
print(list(dicionario.keys()))
print(list(dicionario.values()))

dicionario.setdefault('idade', None)
print(dicionario['idade'])

dicionario.update({
    'nome': 'Pedrão',
    'signo': 'virgem'
})


for chave, valor in dicionario.items():
    print(chave, valor)
