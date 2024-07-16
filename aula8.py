"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

# lista = ['leandro', 123, True]

# print(lista[0])
# lista[0] = 'teste'
# print(lista[0])

# lista2 = [1,2,3]
# numero = lista2[1]
# print(numero)

# print(lista2)
# del lista2[0] #del exclue
# print(lista2)
# lista2.append(4) #append adiciona elemento a lista
# print(lista2)

# while True:
#     add_item_na_lista = int(input("Adicione algo na lista: "))
#     lista3 = [1,2,3]

#     lista3.append(add_item_na_lista)
   
#     print(lista3)
    
# lista = [1,2,3]

# lista.insert(0,2) insert = (posição que vc quer inserir(indice), depois da virgula é o valor) nesse caso insere na posição 0 o valor 2
# print(lista)

listaA = [1,2,3]
listaB = [4,5,6]

listaC = listaA + listaB

print(listaC)