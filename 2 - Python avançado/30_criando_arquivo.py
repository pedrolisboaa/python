# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load


caminho = 'C:\\Users\Pedro Henrique\\Desktop\\PYTHON 3\\'
caminho += 'teste_do_pedro.txt'

# arquivo = open(caminho, 'w')

# arquivo.close()

with open(caminho, 'w+', encoding='utf8') as arquivo:
    arquivo.write('Linha um! \n')
    arquivo.write('Atenção, bem vindo Pedrão! Você comeu maçã! \n')
    arquivo.write('Linha dois! \n')
    arquivo.seek(0, 0)
    print(arquivo.read())


with open(caminho, 'r') as arquivo:
    print(arquivo.read())
