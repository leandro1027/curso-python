#exercicio com while
#calculadora com while

while True:
   
    num1 = int(input("Digite o numero 1: "))
    num2 = int(input("Digite o numero 2: "))
    op = (input("Escolha a operação: (-+*/) "))
    
    numeros_permitidos = None

    try:
        num1_floaT = float(num1)
        num2_float = float(num2)
        numeros_permitidos = True
    except:
        numeros_permitidos = None

    if numeros_permitidos is None:
        print("Um ou ambos os numeros são invalidos")
        continue

    operadores_permitidos = '+-*/'

    if op not in operadores_permitidos:
        print("Operador invalido")
        continue

    if len(op) > 1:
        print("Digite apenas um operador")
        
   
    if op == '+':
        resultado = num1 + num2
    elif op == '-':
        resultado = num1 - num2
    elif op == '*':
        resultado = num1 * num2
    elif op == '/':
        resultado = num1/num1
            
    print(resultado)

    sair = input("Digite 'sim' para sair e 'não' para não sair: ").lower().startswith('s')
    if sair is True:
        break