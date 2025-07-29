#=====DESAFIO 040=====
#040 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Com as notas {:.1f} e {}, a média do aluno é {:.1f}'.format(n1, n2, media))

if media < 5:
    print('O aluno está \033[1;31mREPROVADO!\033[m')
elif 7 > media >= 5:
    print('O aluno está de \033[1;33mRECUPERAÇÃO!\033[m')
elif media >= 7:
    print('O aluno está \033[1;32mAPROVADO!\033[m')