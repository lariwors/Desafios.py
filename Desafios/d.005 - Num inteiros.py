#===== DESAFIO 005 ======

#005 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

numero = int(input('Digite um número: '))
ant = numero - 1
suc = numero + 1
print('Analizando o número {}, seu antecessor é {} e seu sucessor é {}'.format(numero, ant, suc))