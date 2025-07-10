#=====DESAFIO 13=====

#013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Informe o salário do funcionário: R$ '))
novo = salario + (salario * 15 / 100)

print('O funcionário recebia R${:.2f}, agora ganhará um aumento de 15% e receberá R$ {:.2f}'.format(salario, novo))