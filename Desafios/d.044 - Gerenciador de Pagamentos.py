#=====DESAFIO 044=====
#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/pix: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros


print('{:=^40}'.format(' QUITANDA DA LARI '))

preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[1] À vista DINHEIRO/PIX 
[2] À vista CARTÃO
[3] 2x no CARTÃO
[4] 3x ou mais no CARTÃO''')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcelas = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(parcelas))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcelas = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(totalparc, parcelas))
else:
    total = preco
    print('\033[1;31mOPÇÃO INCORRETA!\033[m Tente novamente.')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))
