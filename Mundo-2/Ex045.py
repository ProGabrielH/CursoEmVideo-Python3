# Crie um programa que faça o computador jogar jokenpo com você.
from random import choice
from time import sleep

sn = input('Você quer jogar pedra, papel ou tesoura comigo? ').lower().strip()
jogadas = ['pedra', 'papel', 'tesoura']
jdnv = 'sim'

while jdnv == 'sim':
    if sn == 'sim':
        jogada = choice(jogadas)
        resp = input('Faça sua jogada: ').lower().strip()
        print('1'), sleep(1)
        print('2'), sleep(1)
        print('3'), sleep(1)
        if jogada == 'pedra':
            if resp == 'pedra':
                print('\nPEDRA!')
                print('Empatamos')
                jdnv = input('Deseja jogar de novo? ').lower().strip()
            elif resp == 'papel':
                print('\nPEDRA!')
                print('Você ganhou!')
                jdnv = input('Deseja jogar de novo? ').lower().strip()
            elif resp == 'tesoura':
                print('\nPEDRA!')
                print('HAHA GANHEI, CORNO')
                jdnv = input('Deseja jogar de novo? ').lower().strip()
        elif jogada == 'papel':
            if resp == 'pedra':
                print('\nPAPEL!')
                print('HAHA GANHEI, CORNO')
                jdnv = input('Deseja jogar de novo? ').lower().strip()
            elif resp == 'papel':
                print('\nPAPEL!')
                print('Empatamos')
                jdnv = input('Deseja jogar de novo? ').lower().strip()
            elif resp == 'tesoura':
                print('\nPAPEL!')
                print('Você ganhou!')
                jdnv = input('Deseja jogar de novo? ').lower().strip()
        elif jogada == 'tesoura':
            if resp == 'pedra':
                print('\nTESOURA!')
                print('Você ganhou!')
                jdnv = input('Deseja jogar de novo? ').lower().strip()
            elif resp == 'papel':
                print('\nTESOURA!')
                print('HAHA GANHEI, CORNO!')
                jdnv = input('Deseja jogar de novo? ').lower().strip()
            elif resp == 'tesoura':
                print('\nTESOURA!')
                print('Empatamos')
                jdnv = input('Deseja jogar de novo? ').lower().strip()
    else:
        print('Então tome no seu cu')
        jdnv = 'a'
sleep(3)