"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro: ')
condicao = numero.isnumeric()

if condicao:
    if int(numero) % 2 == 0:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é impar')
else:
    print('Número invalido.')
    
