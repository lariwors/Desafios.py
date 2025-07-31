#=====DESAFIO 053=====
# 053 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = juntar[::-1]

print('O inverso de {} é {}.'.format(juntar, inverso))
if inverso == juntar:
    print('Temos um \033[1mPALÍNDROMO!.\033[m')
else:
    print('A frase \033[31mNÃO\033[m é um \033[1mPALÍNDROMO.\033[m')

