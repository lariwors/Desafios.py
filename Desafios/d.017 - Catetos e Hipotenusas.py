#=====DESAFIO 017=====
# 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

import math

co = float(input('O comprimento do cateto oposto: '))
ca = float(input('O comprimento do cateto adjacente: '))

hip = math.hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hip))
