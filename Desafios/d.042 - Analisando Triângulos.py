#=====DESAFIO 042=====
#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

print('==-' * 10)
print('Analizador de Triângulos')
print('==-' * 10)

# Cada um desses segmentos tem que ser menor do que a soma do cumprimento dos outros 2
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('\033[32mEQUILÁTERO!\033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[32mESCALENO!\033[m')
    else:
        print('\033[32mISÓSCELES!\033[m')
else:
    print('Os segmentos acima \033[31mNÃO PODEM\033[m formar um triângulo.')