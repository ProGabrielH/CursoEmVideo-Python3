# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da prograssão usando
# a estrutura while

termo = 0
pnum = int(input('Qual o primeiro termo da PA: '))
razao = int(input('Qual a razão da PA: '))

while termo != 10:
    print(pnum, end=' ')
    pnum += razao
    termo += 1
