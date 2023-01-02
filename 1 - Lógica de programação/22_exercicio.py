nome = 'Pedro Lisboa'
contador = 0
novo_nome = ''

while contador < len(nome):
    novo_nome += f'*{nome[contador]}'
    contador += 1

print(novo_nome)
