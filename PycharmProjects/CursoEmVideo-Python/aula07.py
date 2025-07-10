#========OPERADORES ARITMÉTICOS=========

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 / n2
dinteira = n1 // n2
potencia = n1 ** n2

print('A soma vale {}, o produto é {} e a divisão é {}'. format(soma, multiplicacao, divisao), end=' ')
print('Divisão inteira {} e potência {}'.format(dinteira, potencia))