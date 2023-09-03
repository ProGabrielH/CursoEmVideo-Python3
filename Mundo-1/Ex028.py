# Escreva um programa que faça o computador escolher um número de 1 a 5, e o usuário tem que advinhar
from random import choice
pcnum = choice(['1', '2', '3', '4', '5'])
num = str(input('Advinhe qual número de 1 a 5 o computador vai escolher: '))
if pcnum == num:
    print(f'O número escolhido pelo computador foi {pcnum}! \nPARABÉNS, VOCÊ GANHOU!')
else:
    print(f'O número escolhido pelo computador foi {pcnum}! \nSinto muito, mais sorte na próxima vez.')
