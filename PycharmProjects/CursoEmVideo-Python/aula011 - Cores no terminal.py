print('\033[4;30;45mOlá, mundo!\033[m')
print('\033[0;34;40mOlá Mundo!\033[m')
print('\033[7;40mOlá Mundo!\033[m')

nome = 'Larissa'
print('Olá, muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;32;40m', nome, '\033[m'))

nome = ('Larissa')
cores = {'limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'\033[33m', 'vermelho':'\033[31m', 'roxo':'\033[35m' }

print('Olá, prazer em te conhecer, {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))