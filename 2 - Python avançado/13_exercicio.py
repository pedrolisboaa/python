
perguntas = [
    {
        'pergunta': 'Quanto é 2+2?',
        'opcoes': ['1', '2', '3', '4'],
        'resposta': '4'
    },
    {
        'pergunta': 'Quanto é 5*5?',
        'opcoes': ['25', '55', '10', '100'],
        'resposta': '25'
    },
    {
        'pergunta': 'Quanto é 10/2?',
        'opcoes': ['4', '2', '5', '21'],
        'resposta': '5'
    },
]
acertos = 0
erros = 0

for i in range(len(perguntas)):
    print(f"Pergunta: {perguntas[i]['pergunta']}")

    for indice, j in enumerate(perguntas[i]['opcoes']):
        print(f'{indice}) {j}')

    opcao = input('Qual a resposta? : ')

    if opcao == perguntas[i]['resposta']:
        print('Acertou 👍')
        acertos += 1
    else:
        print('Errou ❌')
        erros += 1

print()
print(f'Você acertou {acertos}\n de {len(perguntas)} perguntas')
