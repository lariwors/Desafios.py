#=====DESAFIO 031=====
#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

km = int(input('Qual é a distância da sua viagem? '))
print('Bacana! Sua viagem será de {}Km.'.format(km))

if km <= 200:
    preco = km * 0.50
    print('A passagem custa {:.2f}'.format(preco))
else:
    preco = km * 0.45
    print('A passagem custa {:.2f}'.format(preco))