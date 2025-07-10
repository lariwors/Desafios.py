nome = str(input('Qual é o seu nome? ')).strip()
if nome == 'Larissa':
    print('Eu adoro esse nome!')
elif nome == 'Robson' or nome == 'Vinicius' or nome =='Minerva':
    print('Você deve ter uma família linda!')
elif nome in 'Julia Amanda Manuela Tais':
    print('Seu nome é feminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))