#=====DESAFIO 059=====
# 059 - Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
sleep(0.5)

opcao = 0
while opcao != 5:
    print('-' * 25)
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
    opcao = int(input('>>> Qual é a sua opção? '))
    print('-' * 25)

    if opcao == 1:
        soma = n1 + n2
        print('{} + {} é igual a {}.'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('{} x {} é igual a {}.'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('Entre os números {} e {}, o {} é o MAIOR.'.format(n1, n2, maior))
        elif n2 > n1:
            maior = n2
            print('Entre os números {} e {}, o {} é o MAIOR.'.format(n1, n2, maior))
        else:
            maior = n1
            print('Os dois números são IGUAIS.')
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente.')
    sleep(2)
print('Fim do programa. Volte sempre!')
