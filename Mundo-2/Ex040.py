# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
# a média atingida

nota1 = float(input('Qual a primeira nota? '))
nota2 = float(input('Qual a segunda nota? '))

media = (nota1 + nota2)/2

if media >= 7:
    print(f'Parabéns, você passou da média com nota de {media:.1f}')
elif media <7 and media >= 6:
    print(f'Sua média foi de {media:.1f}, você está em recuperação')
elif media < 6:
    print(f'Sua média foi de {media:.1f}, você foi reprovado, estude mais')