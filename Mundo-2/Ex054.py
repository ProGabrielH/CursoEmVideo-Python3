# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas jã são de maiores.

from datetime import date
ano = int(date.today().year)
maior = []
menor = []

for i in range(0,7):
    idade = int(input('Qual ano você nasceu? '))
    if ano - idade >= 18:
        maior.append(idade)
    else:
        menor.append(idade)
print(f'Existem: \n{len(maior)} MAIORES DE IDADE \n{len(menor)} MENORES DE IDADE')
