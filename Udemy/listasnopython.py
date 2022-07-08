"""
Listas em Python
• Fatiamento
append, insert, pop, del, clear, extend
min, max
range
"""
# question =: if question()

print('Deseja ver as listas antes do processo? [S] ou [N]')
#input(question)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]
l4 = [9,8,7,6,5,4,3,2,1]
l1.extend(l2) # Desse modo, a l1 contém o valor dela e de ela 2. (Concatenar)
print("Essa é a l1 depois do 'extend': ", l1)

l2.append("cavalo") # Insere um valor sempre no final da lista.
print("Essa é a l2 depois do 'append': ", l2)

l3.insert(0, 'banana') # Você escolhe o índice de onde quer inserir determinado valor.
print("Essa é a l3 depois do 'insert': ", l3)

l4.pop() # Apaga o último índice da lista.
print("Essa é a l4 depois do 'pop': ", l4)

l5 = list(range(0, 100, 8))
print("Essa lista foi criada com o range: ", l5)