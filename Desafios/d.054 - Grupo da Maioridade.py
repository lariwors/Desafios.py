#=====DESAFIO 054=====
# 054 - Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for pessoa in range(1, 8):
    nasc = int(input(('Em que ano a {}º pessoa nasceu? '.format(pessoa))))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Há \033[1m{}\033[m pessoas maiores de idade e \033[1m{}\033[m pessoas menores de idade.'.format(totmaior, totmenor))


