#=====DESAFIO 029=====
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('Você está acima da velocidade permitida (80km/h)!')
    multa = (velocidade - 80) * 7
    print('VOCÊ FOI MULTADO. você deverá pagar {:.2f}.\n'.format(multa))
print('Tenha um bom dia! Dirija com cuidado.')