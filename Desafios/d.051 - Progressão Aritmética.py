#=====DESAFIO 051=====
# 051 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print('-' * 20)
print('\033[1m10 TERMOS DE UMA PA\033[m')
print('-' * 20)

termos = int(input('\nPrimeiro termo: '))
razao = int(input('Razão: '))
decimo = termos + (10 - 1) * razao

for c in range(termos, decimo + razao, razao):
    print('{} '.format(c), end='→ ')
print('FIM')
