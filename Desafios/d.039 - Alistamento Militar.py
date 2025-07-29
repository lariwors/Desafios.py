#=====DESAFIO 039=====
#039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade.
# Se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano_atual = date.today().year
nasc = int(input('Digite seu ano de nascimento: '))
idade = ano_atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, ano_atual))

if idade == 18:
    print('Você precisa se alistar \033[31mIMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    ano = ano_atual + saldo
    print('Você precisará se alistar em {}, daqui há {} anos.'.format(ano, saldo))
elif idade > 18 and idade <= 70:
    saldo = idade - 18
    ano = ano_atual - saldo
    print('Você deveria ter se alistado há {} anos atrás.'.format(saldo))
    print('Seu alistamento foi em {}.'.format(ano))


