#=====DESAFIO 052=====
# 052 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número \033[1m{}\033[m foi divisível em \033[1m{}\033[m vezes.'.format(num, tot))

if tot == 2:
    print('E por isso, ele é \033[1;32mPRIMO\033[m.')
else:
    print('E por isso, ele \033[31mNÃO É PRIMO\033[m.')
