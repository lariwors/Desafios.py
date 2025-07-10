#=========DESAFIO 02 ==========
#02 - Crie um script Python que leia o dia, mês e ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

dia = int(input ('Em qual dia você nasceu?'))
mes = str(input ('Em qual mês?'))
ano = int(input ('Em qual ano?'))

#print('Você nasceu no dia', dia, 'de', mes, 'de', ano, '. Certo?')
print("Você nasceu no dia {0} de {1} de {2}".format(dia, mes, ano))