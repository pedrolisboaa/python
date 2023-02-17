# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json


class Animal:
    def __init__(self, nome, qtd_patas, cor):
        self.nome = nome
        self.qtd_patas = qtd_patas
        self.cor = cor

    def criar_json(self, classe):
        with open('arquivo_json.json', 'w+', encoding='utf-8') as arquivo:
            json.dump(classe, arquivo, indent=4)


if __name__ == '__main__':

    cachorro = Animal('Carrocho', 4, 'caramelo')
    cachorro.criar_json(vars(cachorro))
