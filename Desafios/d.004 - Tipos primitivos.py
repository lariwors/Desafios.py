#=========DESAFIO 04=========
#04 - Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ela.

num = input('Digite qualquer caractere:')

print('O caractere digitado foi um(a):{}'.format(num))
print('O tipo primitivo desse valor é:', type(num))
print('É numérico?', num.isnumeric())
print('É alfabético?', num.isalpha())
print('É alfanumérico?', num.isalnum())
print('É maiúscula?', num.isupper())
print('É minúscula?', num.islower())
print('Está capitalizada?', num.istitle())
print('Tem espaços?', num.isspace())



