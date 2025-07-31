#=====DESAFIO 055=====
# 055 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

totmaior = 0
totmenor = 0

for p in range(1, 6):
    peso = float(input('Digite o peso da {}º pessoa (Kg): '.format(p)))
    if p == 1:
        totmaior = peso
        totmenor = peso
    else:
        if peso > totmaior:
            totmaior = peso
        if peso < totmenor:
            totmenor = peso
print('Das 6 pessoas, o maior peso foi {}Kg e o menor foi {}Kg.'.format(totmaior, totmenor))

