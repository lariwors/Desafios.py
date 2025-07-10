#=====DESAFIO 15=====

#015 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dia = int(input('Quantos dias você ficou com o carro? '))
km = int(input('Quantos KM você andou? '))

total = (dia * 60) + (km * 0.15)

print('Total a pagar: R$  {:.2f}'.format(total))

