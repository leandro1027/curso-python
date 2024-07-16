# cont_linhas = 5
# cont_colunas = 5

# linha = 1 
# while linha <= cont_linhas:
#     coluna = 1
#     while coluna <= cont_colunas:
#         print(f"{linha = } {coluna = }")
#         coluna += 1
#     linha += 1


# print(".")


# nome = 'Leandro'
# indice = 0
# novo_nome =''


# while indice < len(nome):
#     letra = nome[indice]
#     novo_nome += f"*{letra}"
#     indice += 1
  
# print(novo_nome)

#calculadora com while

# while True:
   
#     num1 = int(input("Digite o numero 1: "))
#     num2 = int(input("Digite o numero 2: "))
#     op = (input("Escolha a operação: (-+*/) "))
    
#     numeros_permitidos = None

#     try:
#         num1_floaT = float(num1)
#         num2_float = float(num2)
#         numeros_permitidos = True
#     except:
#         numeros_permitidos = None

#     if numeros_permitidos is None:
#         print("Um ou ambos os numeros são invalidos")
#         continue

#     operadores_permitidos = '+-*/'

#     if op not in operadores_permitidos:
#         print("Operador invalido")
#         continue

#     if len(op) > 1:
#         print("Digite apenas um operador")
        
   
#     if op == '+':
#         resultado = num1 + num2
#     elif op == '-':
#         resultado = num1 - num2
#     elif op == '*':
#         resultado = num1 * num2
#     elif op == '/':
#         resultado = num1/num1
            
#     print(resultado)

#     sair = input("Digite 'sim' para sair e 'não' para não sair: ").lower().startswith('s')
#     if sair is True:
#         break

# string = ("coisa")

# i = 0

# while i < len(string):
#     letra = string[i] 
#     print(letra)
#     i+=1

# frase = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiuris nisi ut aliquip ex ea '

# i = 0

# while i < len(frase):
#     letra_atual = frase[i]
#     qtd_vezes_letra = frase.count(letra_atual)
    
#     print(letra_atual, qtd_vezes_letra)
#     i+=1





   
    
