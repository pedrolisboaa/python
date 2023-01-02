LISTAS_DE_COMPRAS = []

inserir_item = input('Favor infomar item para inserir na lista: ')
LISTAS_DE_COMPRAS.append(inserir_item)

flag = True
while flag:
    print('O que você deseja fazer')
    opcao = input(
        '[1] - Inserir item - [2] - Listar itens - [3] Apagar item: - [4] Sair ')

    if opcao == '1':
        inserir_item = input('Favor infomar item para inserirr na lista: ')
        LISTAS_DE_COMPRAS.append(inserir_item)
        
    elif opcao == '2':
        for item in LISTAS_DE_COMPRAS:
            print(item)
            
    elif opcao == '3':
        item_antigo = input('informe item a ser apagado: ')
        if item_antigo in LISTAS_DE_COMPRAS:
            LISTAS_DE_COMPRAS.remove(item_antigo)
        else:
            print(f'Item não encontrado.')
                 
    elif opcao == '4':
        flag = False
        
    else:
        print(f'O que você digitou não esta nas opções.')
    

print('Fim do Programa')