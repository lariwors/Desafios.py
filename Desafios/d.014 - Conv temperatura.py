#=====DESAFIO 14=====

#014 - Escreva um programa que converta uma temperatura digitada em ºC e para ºF.

C = float(input('Informe a temperatura em ºC: '))
F = ((9 * C) / 5 + 32)

print('A temperatura de {}ºC corresponde a {}ºF.'. format(C, F))

#==============================================

F = float(input('Informe a temperatura em ºF: '))
C = ((32 - F) * 5 / 9)

print('A temperatura de {}ºF corresponde a {}ºC.'. format(F, C))