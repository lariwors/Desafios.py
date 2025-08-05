#=====DESAFIO 062=====
# 062 - Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('-' * 20)
print('\033[1m10 TERMOS DE UMA PA\033[m')
print('-' * 20)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

termo = primeiro
cont = 1
total = 0
continua = 10

while continua != 0:
    total = total + continua
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    continua = int(input('\nQuantos termos você quer mostrar a mais? '))
    if continua == 0:
        print('Progressão finalizada com {} termos mostrados.'.format(total))