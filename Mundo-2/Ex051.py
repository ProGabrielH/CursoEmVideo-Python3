# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão
p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

for i in range(p, p+(10)*r, r):
    print(i, end=' ')
