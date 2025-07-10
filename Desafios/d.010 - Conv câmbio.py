#=====DESAFIO 10=====

#10 - Crie um programa que leia quanto dinheiro uma pessoa tem na conta e mostre quantos dólares ela pode comprar.
# Considere US$ 1,00 = R$5,50

dolar = float(input('Quanto você receberá esse mês? US$ '))
real = dolar * 5.48
desconto = real * 3 / 100
final = real - desconto

print('Com US${:.2f}, você irá receber R${:.2f}. Descontando R${:.2f} da taxa de câmbio (3%), o valor final será: R${:.2f}'.format(dolar, real, desconto, final))
