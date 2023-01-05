s1 = set()
s2 = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
s3 = {1, 1, 1, 3, 3, 3, 2, 2, 12, 12, 3, 5}

lista = [1, 2, 3, 4, 1, 2, 3, 4, 5, 123, 2, 3, 2, 1, 6]


print(s1)
print(s2)
print(s3)
print(list(set(lista)))


print(s1)
s1.add(99)
s1.add(50)
s1.update((100, 1))
s1.discard(100)
print(s1)

# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos


set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3 = set1 ^ set2
print(set3)
