# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado

from random import randint
from time import sleep
from operator import itemgetter

jogada = {}

for i in range(0, 4):
    jogada[f'jogador{i}'] = randint(1, 6)
    sleep(0.7)
    print(f'Jogador{i}: ', end='')
    print(jogada[f'jogador{i}'])
rank = sorted(jogada.items(), key=itemgetter(1), reverse=True)
print('-='*15)
for i in range(0, 4):
    print(f'Em {i+1}º lugar: ', end='')
    print(rank[i][0])
