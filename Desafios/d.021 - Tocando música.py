#=====DESAFIO 021=====
# 021 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3

import pygame

pygame.init()
pygame.mixer.music.load('d021.mp3')
pygame.mixer.music.play()

input('Pressione Enter para encerrar.')
pygame.event.wait()

#QUE MANEIRO AAAAAAAAAAAAAAAAAAAAAAAAAAAA
