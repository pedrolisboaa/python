def saudacao(msg):
    return msg


def executa(funcao, msg):
    return funcao(msg)


teste = executa(saudacao, 'bom dia')
print(teste)
