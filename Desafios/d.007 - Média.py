#=====DESAFIO 007=====

#007 - Desenvolva um programa que leia as duas notas de um aluno. Calcule e mostre sua média.

nome = (input('Digite o nome do aluno: '))
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))

soma = n1+n2
media = (n1+n2)/2

print('A soma das notas do aluno {} foram: {} pontos \nSua média foi: {:.1f}'.format(nome, soma, media))