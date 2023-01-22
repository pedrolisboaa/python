a = 19
b = 0
try:
    c = a / b
    print(c)
except ZeroDivisionError as e:
    print(f'Erro : {e}')


print(f'Fim do código')
