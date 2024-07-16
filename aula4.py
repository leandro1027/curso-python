# CONSTANTE = "Variáveis" que não vão mudar
# Muitas condições no mesmo if (ruim)
#     <- Contagem de complexidade (ruim)

# velocidade = 61
# local_carro = 99

# RADAR_1 = 60  # velocidade máxima do radar 1
# LOCAL_1 = 100  # local onde o radar 1 está
# RADAR_RANGE = 1  # A distância onde o radar pega

# vel_carro_pass_radar_1 = velocidade > RADAR_1
# carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
#     local_carro <= (LOCAL_1 + RADAR_RANGE)
# carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

# if vel_carro_pass_radar_1:
#     print('Velocidade carro passou do radar 1')

# if carro_passou_radar_1:
#     print('Carro passou radar 1')

# if carro_multado_radar_1:
#     print('carro multado em radar 1')


#variaveis diferentes com valores iguais as vezes possuem o mesmo endereço
# var1=("a")
# var2=("a")

# print(id(var1))
# print(id(var2))

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# num_int = int(input("Digite um numero inteiro: "))
# par = num_int % 2 == 0

# try:
#     if par:
#         print("Seu numero é par")
#     else:
#         print("Seu numero é impar")
# except:
#     print("Seu numero não é int")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# hora = int(input("Digite o horario atual: "))

# try:
#     if hora >= 0 and hora <= 11:
#         print("Bom dia")
#     elif hora >=12 12 and hora <= 17:
#         print("Boa tarde")
#     elif hora >= 18 and hora <= 23:
#         print("Boa noite")
#     else:
#         print("Não conheço essa hora")
# except:
#     print("Digite um horario entre 0-23")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
# nome = input("Digite seu nome: ")

# tamanho = len(nome)
# # print(tamanho)

# if tamanho > 1:
#     if tamanho <= 4:
#         print("Seu nome é curto")
#     elif tamanho >= 5 and tamanho <= 6:
#         print("Seu nome é normal")
#     else:
#         print("Seu nome é muito grande")
# else:
#     print("Digite mais de uma letra")

# contador = 0

# while contador < 10:
#     contador = contador +1
#     print(contador)

"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""
# contador = 10


# contador += 5
# print(contador)

# cont = 0

# while cont <= 100:
#     cont += 1

#     if cont == 6:
#         continue

#     print(cont)

#     if cont == 40:
       
#         break
        