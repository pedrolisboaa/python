try:
    print(1234)
    print(5678)
    int('a')
except ValueError as e:
    print(f'O correu um erro: {e}')
