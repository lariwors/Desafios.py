#======DESAFIO 028======
#028 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou não.

from random import randint
import emoji

computador = randint(0, 1)
print('Olá! Bem vindo ao Jogo da Adivinhação!')
print('=**=' * 20)
print('Pensando em um número de 0 a 5... será que você consegue adivinhar?')
print('=**=' * 20)
usuario = int(input('Qual número você acha que o computador escolheu?\nDigite aqui: '))
if usuario == computador:
    print(emoji.emojize('Uau!!\nVocê acertou :trophy:! Parabéns.'))
else:
    print(emoji.emojize(':sad_but_relieved_face: Vish, não foi dessa vez...\nEu pensei no número {} e não no {}.\nTalvez um dia você acerte.'.format(computador, usuario)))




