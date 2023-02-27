import json

class Animal:
    def __init__(self, nome, qtd_patas, cor):
        self.nome = nome
        self.qtd_patas = qtd_patas
        self.cor = cor


if __name__ == '__main__':

    with open('arquivo_json.json', 'r') as arquivo:
        infomacao = json.loads(arquivo.read())

    doguinho = Animal(**infomacao)

    print(doguinho.nome)
    print(doguinho.qtd_patas)
    print(doguinho.cor)
