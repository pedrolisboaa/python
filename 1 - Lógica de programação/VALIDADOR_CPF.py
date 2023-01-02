
CPF_A_SER_VALIDADO = '68536194149'
MULTIPLICADOR1 = [10, 9, 8, 7, 6, 5, 4, 3, 2,]
MULTIPLICADOR2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

# PRIMEIRO DÍGITO CPF
primeira_soma = 0
cpf_cortado = CPF_A_SER_VALIDADO[:9]

for indice, numero in enumerate(cpf_cortado):
    primeira_soma += MULTIPLICADOR1[indice] * int(numero)

resto_primeira_divisao = primeira_soma % 11
if resto_primeira_divisao < 2:
    cpf_cortado += str(0)
else:
    cpf_cortado += str(11 - resto_primeira_divisao)

# SEGUNDO DÍGITIRO CPF
segunda_soma = 0

for indice, numero in enumerate(cpf_cortado):
    segunda_soma += MULTIPLICADOR2[indice] * int(numero)

resto_segunda_divisao = segunda_soma % 11
if resto_segunda_divisao < 2:
    cpf_cortado += str(0)
else:
    cpf_cortado += str(11 - resto_segunda_divisao)


# RESPOSTA FINAL

if CPF_A_SER_VALIDADO == cpf_cortado:
    print(f'O CPF {cpf_cortado} é válido.')
else:
    print(f'O CPF {CPF_A_SER_VALIDADO} não é válido.')
