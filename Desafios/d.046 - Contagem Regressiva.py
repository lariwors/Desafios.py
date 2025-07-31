#=====DESAFIO 046=====
#046 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import emoji
from time import sleep

print(emoji.emojize(':fireworks: \033[1mContagem Regressiva\033[m :fireworks:'))
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[7;40mFELIZ ANO NOVO!!\033[m')