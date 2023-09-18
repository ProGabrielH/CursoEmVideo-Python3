# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade. até 9: mirim. até 14: infantil. Até 19: juniot. Até 20: sênior. acima: master

from time import strftime

ano_atual = int(strftime("%Y"))
ano = int(input('Qual seu ano de nascimento? '))
idade = ano_atual - ano

if idade <= 9:
    print('Categoria MIRIM')
elif idade > 9 and idade <= 14:
    print('Categoria INFANTIL')
elif idade > 14 and idade <= 19:
    print('Categoria JUNIOR')
elif idade > 19 and idade <= 20:
    print('Categoria SÊNIOR')
elif idade > 20:
    print('Categoria MASTER')
