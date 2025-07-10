 #=====DESAFIO 35=====
 #Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('==-' * 10)
print('Analizador de Triângulos')
print('==-' * 10)

# Cada um desses segmentos tem que ser menor do que a soma do cumprimento dos outros 2
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')