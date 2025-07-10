#=====DESAFIO 16=====
# 016 - Crie um program que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
#EX: digite um numero: 4.543, o numero tem a parte inteira 4.

import math

num = float(input('Digite um número: '))

print('O número {}, tem parte inteira de {}.'.format(num, math.trunc(num)))

