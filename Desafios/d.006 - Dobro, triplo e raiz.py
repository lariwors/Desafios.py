#=====EXERCÍCIO 006=====

#006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

numero = int(input('Digite um número:'))
double = numero * 2
triple = numero * 3
raiz = numero ** (1/2)

print('Analizando o número {} \nO dobro de é: {} \nO triplo é: {} \nA raiz quadrada é: {:.2f}'.format(numero, double, triple, raiz))