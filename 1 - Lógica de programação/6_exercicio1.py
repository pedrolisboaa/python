from datetime import datetime

nome = 'Pedro'
sobrenome = 'Nascimento Lisboa'
idade = 30
ano_nascimento = datetime.now().year - idade
maior_de_idade = idade >= 18
altura = 1.90


print(f'Nome: {nome.upper()}')
print(f'Sobrenome {sobrenome.lower()}')
print(f'Idade: {idade} anos')
print(f'Anos de nascimento {ano_nascimento}')
print(f'É maior de idade {maior_de_idade}')
print(f'Altura em metros {altura}')
