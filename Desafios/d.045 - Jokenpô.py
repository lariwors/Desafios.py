#=====DESAFIO 045=====
#045 - Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
import emoji
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = (randint(0, 2))

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('\033[30;46m JO \033[m')
sleep(1)
print('\033[30;46m KEN \033[m')
sleep(1)
print('\033[30;46m PÔ!!!\033[m')

print('-' * 25)

if jogador >= 0 and jogador <= 2:
    print('Computador jogou {}.'.format(itens[computador]))
    print('Jogador jogou {}.'.format(itens[jogador]))
    print('-' * 25)
else:
    print('\033[1;31mJOGADA INVÁLIDA!\033[m\u274C')


if computador == 0: #Computador jogou PEDRA
    if jogador == 0:
        print('\033[1;34mEMPATE!\033[m \U0001F91D')
    elif jogador == 1:
        print(emoji.emojize('Você \033[1;32mVENCEU!\033[m \U0001F3C6'))
    elif jogador == 2:
        print('O Computador \033[1;32mVENCEU!\033[m')

elif computador == 1: #Computador jogou PAPEL
    if jogador == 0:
        print('O Computador \033[1;32mVENCEU!\033[m')
    elif jogador == 1:
        print('\033[1;34mEMPATE!\033[m \U0001F91D')
    elif jogador == 2:
        print(emoji.emojize('Você \033[1;32mVENCEU!\033[m \U0001F3C6'))

elif computador == 2: #Computador jogou TESOURA
    if jogador == 0:
        print(emoji.emojize('Você \033[1;32mVENCEU!\033[m \U0001F3C6'))
    elif jogador == 1:
        print('O Computador \033[1;32mVENCEU!\033[m')
    elif jogador == 2:
        print('\033[1;34mEMPATE!\033[m \U0001F91D')
