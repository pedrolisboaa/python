from decimal import Decimal

numero1 = 0.1
numero2 = 0.7
NUMERO = numero1 + numero2

print(NUMERO)
print(f'{NUMERO:.2f}')
print(round(NUMERO, 2))
numero1 = Decimal('0.1')
numero2 = Decimal('0.7')
print(NUMERO)
