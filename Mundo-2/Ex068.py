# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

from random import randint
streak = 0

print('Vamos jogar impar ou par')
while True:
    numpc = randint(1,10)
    respplayer = input('\nImpar ou Par [I/P]: ').strip().upper()[0]
    numplayer = int(input('Digite seu número: '))

    if respplayer in 'Ii':
        if (numpc + numplayer)%2 == 0:
            print(f'Meu número foi: {numpc}')
            print(f'{numpc} + {numplayer} é PAR\nVOCÊ PERDEU COM UMA SEQUÊNCIA DE {streak}')
            break
        else:
            print(f'Meu número foi: {numpc}')
            print(f'{numpc} + {numplayer} é IMPAR \nVOCÊ GANHOU,VAMOS DE NOVO')
            streak += 1
    elif respplayer in 'Pp':
        if (numpc + numplayer)%2 == 0:
            print(f'Meu número foi: {numpc}')
            print(f'{numpc} + {numplayer} é PAR \nVOCÊ GANHOU,VAMOS DE NOVO')
            streak += 1
        else:
            print(f'Meu número foi: {numpc}')
            print(f'{numpc} + {numplayer} é IMPAR\nVOCÊ PERDEU COM UMA SEQUÊNCIA DE {streak}')
            break
    else:
        print('Resposta inválida, vamos de novo\n')

print('\nOBRIGADO POR JOGAR')
