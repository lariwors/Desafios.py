#=====DESAFIO 036=====
# 036 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('==========EMPRÉSTIMOS=========')
casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o salário do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))
parcelas = casa / (anos * 12)
minimo = salario * 30/ 100

print('\nPara pagar uma casa de R${:.2f} em {} anos,'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}.'.format(parcelas))

if parcelas >= minimo:
    print('\nInfelizmente o seu empréstimo foi \033[1;31mNEGADO!\033[m')
else:
    print('\nSeu empréstimo foi \033[1;32mAPROVADO!\033[m')

