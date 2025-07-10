#=====DESAFIO 08=====

#008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Digite uma distância em metros: '))

cm = medida * 100
mm = medida * 1000

print('A medida de {} metros corresponde a: \n{:.0f}cm\n {:.0f}mm'.format(medida, cm, mm))
