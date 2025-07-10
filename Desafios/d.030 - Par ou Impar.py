#=====DESAFIO 030=====
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Digite um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O número {}{}{} é PAR!'.format('\033[1;31m', numero, '\033[m'))
else:
    print('O número {}{}{} é IMPAR!'.format('\033[1;32m', numero, '\033[m'))
