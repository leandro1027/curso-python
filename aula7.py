#for em py

# texto = 'python'
# nova_letra =''

# for letra in texto:
#     nova_letra += f"*{letra}"
#     print(letra)
# print(f"{nova_letra}*")

# ==========================================================

"""
For + Range
range -> range(start, stop, step) 
começo (start), vai até (stop) 
step é a quantidade de vezes que ele vai pular, se step for 2, vai pular de 2 em 2
"""
# numeros = range(10)

# for numero in numeros:
#     print(numero)

for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')