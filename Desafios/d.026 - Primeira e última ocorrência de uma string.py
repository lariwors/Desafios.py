#=====DESAFIO 026=====
#026 - Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper()

print('Na sua frase, a letra A aparece {} vezes'.format(frase.count('A')))
print('O primeiro A fica na posição {}'.format(frase.find('A') + 1))
print( 'O último A fica na posição {}'.format(frase.rfind('A') + 1))