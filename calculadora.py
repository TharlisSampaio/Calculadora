operation = input('''
Selecione a operação desejada:
+ para somar
- para subtrair
* para multplicar
/ para dividir

''')

print('Entre com dois números')
num1 = int(input("primeiro número"))
num2 = int(input("segundo número"))

if(operation=='+'):
    print(f'{num1}+{num2} = ', num1 + num2)
elif operation == '-':
    # subtração
    print(f'{num1} - {num2} = ', num1 - num2)
elif operation == '*':
    # multiplicação 
    print(f'{num1} * {num2} = ', num1 * num2)
elif operation == '/':
    # divisão
    print(f'{num1} / {num2} = ', num1 / num2)
else:
    print('teve um erro inesperado, dados inseridos de forma errado')