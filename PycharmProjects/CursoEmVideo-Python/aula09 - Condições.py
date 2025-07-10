from os.path import split

nome = str(input('Qual é o seu nome? ')).strip()
if nome == 'Larissa':
    print('Você tem um nome lindo!!')
else:
    print('Seu nome é tão normal...')
print('Olá {}.'.format(nome).title())


n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
print('A sua média foi: {:.1f}'.format(media))

if media >= 6:
    print('Sua média foi ótima! Parabéns.')
else:
    print('Sua média não foi boa... Estude mais.')