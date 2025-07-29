#=====DESAFIO 043=====
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
# de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O seu IMC é {:.2f}'.format(imc))

if imc < 18.2:
    print('Você está ABAIXO DO PESO.')
elif imc >= 18.5 and imc < 25:
    print('PARABÉNS! Você está no seu \033[32mPESO IDEAL\033[m.')
elif imc >= 25 and imc < 30:
    print('Você está em \033[33mSOBREPESO\033[m.')
elif imc >= 30 and imc < 40:
    print('Você está com \033[1;35mOBESIDADE\033[m.')
else:
    print('Você está com \033[1;31mOBESIDADE MÓRBIDA!\033[m')

