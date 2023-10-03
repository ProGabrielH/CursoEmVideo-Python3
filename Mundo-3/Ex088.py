# Faça um programa que ajude um jogador da mega sena a criar palpites. O programa deve perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

cont = 0
palpite = []
usados = []

print('-='*30)
print(f'{"GERADOR DE JOGOS DA MEGASENA":^60}')
print('-='*30)

qnt = int(input('Quantos jogos deseja gerar? '))
for i in range(0, qnt):
    while cont <= 6:
        num = randint(1, 60)
        if num not in usados:
            palpite.append(num)
            usados.append(num)
            cont += 1
    cont = 0
    sleep(0.5)
    print(f'Jogo {i+1}: {sorted(palpite)}')
    palpite.clear()
    usados.clear()
