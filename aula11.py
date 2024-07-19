"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
# frase = '   Olha só que   , coisa interessante          '
# lista_frases_cruas = frase.split(',')

# lista_frases = []
# for i, frase in enumerate(lista_frases_cruas):
#     lista_frases.append(lista_frases_cruas[i].strip())

# # print(lista_frases_cruas)
# # print(lista_frases)
# frases_unidas = ', '.join(lista_frases)
# print(frases_unidas)

#lista de lista e seus indices (no C matrizes)

lista = [
    ['Balaban', 'teste1'],
    ['teste', 'Leandro', (1,2,3)]
]

print(lista[1][1])
print(lista[1][2])
print(lista[1][2][1])