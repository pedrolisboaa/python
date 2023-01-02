nome = 'Pedro Lisboa'
peso = 130
altura = 1.90
imc = peso / (altura * altura)

print(f'{nome} pesa {peso} sua altura é de {altura} e seu IMC: {imc:.2f}')

nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))


variavel_a = 1 or 0
variavel_b = 0 or 1
print(variavel_a, variavel_a)
