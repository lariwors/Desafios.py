#=====DESAFIO 058=====
# 058 - Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

computador = randint(0, 10)
print('\033[1mOlá! Bem vindo ao Jogo da Adivinhação!\033[m')
print('-' * 40)
print('''Estou pensando em um número de \033[1m0 a 10\033[m... 
Será que você consegue adivinhar?''')
print('-' * 40)
acertou = False
palpites = 0
while not acertou:
    usuario = int(input('Em qual número você acha que o computador pensou? '))
    palpites += 1
    if usuario == computador:
        acertou = True
    else:
        if usuario < computador:
            print('É um número Maior... Tente mais uma vez!')
        elif usuario > computador:
            print('É um número MENOR... Tente novamente!')
print('O computador pensou no número {}. Você acertou!'.format(computador))
print('Acertou com {} tentativas.'.format(palpites))