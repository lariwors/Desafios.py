#=====DESAFIO 060=====
# 060 - Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial

num = int(input('Digite um número para calcular seu fatorial: '))
fact = factorial(num)
print('O fatorial de {} é {}.'.format(num, fact))

print('\n\033[1m======OUTRA POSSIBILIDADE======\033[m\n')

num = int(input('Digite um número para calcular seu fatorial: '))
c = num
f = 1
print('Calculando {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}.'.format(f))