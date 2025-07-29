#=====DESAFIO 038=====
#038 - Escreva um programa que leia dois números inteiros e compare-os. Mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O \033[4mPRIMEIRO\033[m valor é MAIOR')
elif n2 > n1:
    print('O \033[4mSEGUNDO\033[m valor é MAIOR')
else:
    print('Os dois valores são \033[35mIGUAIS\033[m')
