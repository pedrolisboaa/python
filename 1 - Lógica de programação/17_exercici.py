nome = input('Informe seu nome: ')
idade = int(input('Informe sua idade? '))


if nome == "" or nome == " " or idade < 0:
    print(f'Desculpe, você deixou dados em branco!')
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if " " in nome:
        print(f'Seu nome  contêm espaço')
    else:
        print(f'Seu nome não tem espaço')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A  última  letar do seu nome é {nome[-1]}')
